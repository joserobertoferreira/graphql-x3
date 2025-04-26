import uuid
from datetime import date, datetime
from typing import Optional, Tuple

from sqlalchemy import text
from sqlalchemy.engine.row import Row
from sqlalchemy.orm import Session

from app.core import local_menus, settings


def get_next_counter(
    db: Session, counter_code: str, site: str = '', date: date = settings.DEFAULT_LEGACY_DATE, comp: str = ''
) -> str:
    """
    Retrieves the next sequential ID for Editor (SYNC), updates the counter,
    and formats it as a 4-character string.

    Args:
        db (Session): SQLAlchemy session object.
        counter_code (str): The code of the counter to retrieve.
        site (str, optional): The site code. Defaults to ''.
        date (date, optional): The date for the counter. Defaults to settings.DEFAULT_LEGACY_DATE.
        comp (str, optional): Additional string to append to the ID. Defaults to ''.
    """
    try:
        # Attempts to get the counter definition
        stmt_select = text(f'SELECT * FROM {settings.DB_SCHEMA}.ACODNUM WHERE CODNUM_0 = :code')

        result = db.execute(stmt_select, {'code': counter_code})
        counter_data = result.mappings().one_or_none()

        if counter_data is None:
            raise ValueError(f'Contador {counter_code} não encontrado.')

    except Exception as e:
        print(f'Erro ao obter código do contador: {e}')
        return ''

    value_ok, index = _check_value_in_columns(counter_data, 8, 'POSTYP', 'NBPOS_0')

    if not value_ok:
        return ''

    value_ok, _ = _check_value_in_columns(counter_data, 9, 'POSTYP', 'NBPOS_0')

    if not value_ok:
        comp = ''

    print('9' * counter_data[f'POSLNG_{index}'])

    # max_value = '9' * counter_data[f'POSLNG_{index}']

    final_counter = ''

    try:
        period = _determine_the_period(counter_data['NIVRAZ_0'], date)
        site_or_society = _determine_site_or_society(counter_data['NIVDEF_0'], site)
        counter = _create_next_counter(
            db,
            counter_code,
            site=site_or_society,
            period=period,
            complement=comp,
            length=counter_data['LNG_0'],
        )

        # Generate the final counter string
        if counter:
            final_counter = _attrib_number(
                counter=counter,
                counter_data=counter_data,
                date=date,
                site=site_or_society,
                complement=comp,
            )

    except Exception as e:
        # Log e re-levanta a exceção para ser pega pela função chamadora
        # logging.error(f'Erro ao obter próximo editor_id (sync): {e}', exc_info=True)
        print(f'Erro ao obter próximo editor_id: {e}')

        # NÃO faça rollback aqui, deixe a função principal decidir.
        raise

    print(f'Próximo valor do contador {counter_code}: {final_counter}')

    return final_counter


def _attrib_number(counter: str, counter_data: Row, date: date, site: str, complement: str) -> str:
    """
    Formats the counter number according to the specifications in the database.

    Args:
        counter (str): The counter number to format.
        counter_data (Row): The row containing the counter data from the database.

    Returns:
        str: The formatted counter number.
    """
    valeur = ''

    for i in range(counter_data['NBPOS_0']):
        if counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.CONSTANT:
            valeur += counter_data[f'POSCTE_{i}']
        elif counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.YEAR:
            valeur += _for_year(counter_data, i, date)
        elif counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.MONTH:
            valeur += _for_month(counter_data, i, date)
        elif counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.WEEK:
            valeur += f'{date.strftime("%W"):02d}'
        elif counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.DAY:
            valeur += _for_day(counter_data, i, date)
        elif counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.COMPANY:
            valeur += _for_site_or_company(counter_data, i, site)
        elif counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.SITE:
            valeur += _for_site_or_company(counter_data, i, site)
        elif counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.SEQUENCE_NUMBER:
            valeur += counter
        elif counter_data[f'POSTYP_{i}'] == local_menus.Chapter47.COMPLEMENT:
            valeur += _for_complement(counter_data, i, complement)

    if counter_data[f'TYP_{i}'] == local_menus.Chapter46.NUMERIC:
        valeur = str(int(valeur))

    return valeur


def _for_complement(counter_data: Row, index: int, complement: str) -> str:
    """
    Formats the complement part of the counter according to the specifications in the database.

    Args:
        counter_data (Row): The row containing the counter data from the database.
        index (int): The index of the current column being processed.
        complement (str): The complement string to use for formatting.

    Returns:
        str: The formatted complement part of the counter.
    """
    if counter_data[f'POSLNG_{index}'] == settings.LITERAL_ZERO:
        return complement
    else:
        return complement[: counter_data[f'POSLNG_{index}']]


def _for_site_or_company(counter_data: Row, index: int, site_or_society: str) -> str:
    """
    Formats the site or company part of the counter according to the specifications in the database.

    Args:
        counter_data (Row): The row containing the counter data from the database.
        index (int): The index of the current column being processed.
        site_or_society (str): The site or society code to use for formatting.

    Returns:
        str: The formatted site or company part of the counter.
    """
    if len(site_or_society) < counter_data[f'POSLNG_{index}'] and counter_data['CTLCHR_0'] == settings.LITERAL_TWO:
        return site_or_society + '_' * (counter_data[f'POSLNG_{index}'] - len(site_or_society))
    else:
        return site_or_society[: counter_data[f'POSLNG_{index}']]


def _for_year(counter_data: Row, index: int, date: date) -> str:
    """
    Formats the year part of the counter according to the specifications in the database.

    Args:
        counter_data (Row): The row containing the counter data from the database.
        index (int): The index of the current column being processed.
        date (date): The date to use for formatting.

    Returns:
        str: The formatted year part of the counter.
    """
    if counter_data[f'POSLNG_{index}'] == settings.LITERAL_ONE:
        return str(_determine_the_period(99, date))
    elif counter_data[f'POSLNG_{index}'] == settings.LITERAL_TWO:
        return f'{_determine_the_period(local_menus.Chapter48.ANNUAL, date):02d}'
    elif counter_data[f'POSLNG_{index}'] == settings.LITERAL_FOUR:
        return f'{date.year:04d}'
    return ''


def _for_month(counter_data: Row, index: int, date: date) -> str:
    """
    Formats the month part of the counter according to the specifications in the database.

    Args:
        counter_data (Row): The row containing the counter data from the database.
        index (int): The index of the current column being processed.
        date (date): The date to use for formatting.

    Returns:
        str: The formatted month part of the counter.
    """
    if counter_data[f'POSLNG_{index}'] == settings.LITERAL_TWO:
        return f'{date.month:02d}'
    elif counter_data[f'POSLNG_{index}'] == settings.LITERAL_THREE:
        return date.strftime('%b').upper()
    return ''


def _for_day(counter_data: Row, index: int, date: date) -> str:
    """
    Formats the day part of the counter according to the specifications in the database.

    Args:
        counter_data (Row): The row containing the counter data from the database.
        index (int): The index of the current column being processed.
        date (date): The date to use for formatting.

    Returns:
        str: The formatted day part of the counter.
    """
    if counter_data[f'POSLNG_{index}'] == settings.LITERAL_ONE:
        return f'{date.isoweekday():02d}'
    elif counter_data[f'POSLNG_{index}'] == settings.LITERAL_TWO:
        return f'{date.day:02d}'
    elif counter_data[f'POSLNG_{index}'] == settings.LITERAL_THREE:
        return f'{(date - date(date.year, 1, 1)).days + 1:03d}'
    return ''


def _create_next_counter(db: Session, counter_code: str, **kwargs) -> str:
    # Attempts to get the current value (with row locking)
    # The lock syntax may vary slightly or may require raw SQL
    # depending on the dialect and how it handles with_for_update in sync.
    # Using text might be more reliable for explicit locking.
    site = kwargs.get('site', '')
    period = kwargs.get('period', 0)
    complement = kwargs.get('complement', '')
    length = kwargs.get('length', 1)

    if not site:
        site = ''

    if not period:
        period = 0

    if not complement:
        complement = ''

    if not length:
        length = 1

    stmt_select = text(
        f'SELECT VALEUR_0 FROM {settings.DB_SCHEMA}.AVALNUM '
        f'WHERE CODNUM_0 = :code AND SITE_0 = :site '
        f'AND PERIODE_0 = :period AND COMP_0 = :comp'
    )

    result = db.execute(stmt_select, {'code': counter_code, 'site': site, 'period': period, 'comp': complement})
    current_value_record = int(result.scalar_one_or_none())

    if current_value_record is None:
        current_value = 1
    else:
        current_value = current_value_record

    next_value = current_value + 1

    if current_value > 1:
        stmt_update = text(
            f'UPDATE {settings.DB_SCHEMA}.AVALNUM SET VALEUR_0 = :next_val '
            f'WHERE CODNUM_0 = :code AND SITE_0 = :site '
            f'AND PERIODE_0 = :period AND COMP_0 = :comp'
        )

        try:
            result = db.execute(
                stmt_update,
                {
                    'next_val': next_value,
                    'code': counter_code,
                    'site': site,
                    'period': period,
                    'comp': complement,
                },
            )

            db.flush()
            db.commit()

        except Exception as e:
            raise ValueError(f'Erro ao atualizar o contador {counter_code}: {e}')
    else:
        stmt_insert = text(
            f'INSERT INTO {settings.DB_SCHEMA}.AVALNUM ('
            f'CODNUM_0, SITE_0, PERIODE_0, COMP_0, VALEUR_0, '
            f'CREUSR_0, UPDUSR_0, CREDATTIM_0, UPDDATTIM_0, AUUID_0) '
            f'VALUES (:code, :site, :period, :comp, :next_val, '
            f"'INTER', 'INTER', :current_date, :current_date, :unique_id)"
        )

        try:
            result = db.execute(
                stmt_insert,
                {
                    'code': counter_code,
                    'site': site,
                    'period': period,
                    'comp': complement,
                    'next_val': next_value,
                    'current_date': datetime.datetime.now(),
                    'unique_id': lambda: uuid.uuid4().bytes,
                },
            )

            db.flush()
            db.commit()

        except Exception as e:
            raise ValueError(f'Erro ao inserir o contador {counter_code}: {e}')

    formatted_id = f'{current_value:0{length}d}'

    print(f'Próximo do contador {counter_code} é {formatted_id}')

    if len(formatted_id) > length:
        raise ValueError(f'Próximo do contador {current_value} excede {length} dígitos.')

    return formatted_id


def _check_value_in_columns(
    row: Row, value_to_find: int, search_column: str = '', limit_column: str = ''
) -> Tuple[bool, Optional[int]]:
    """
    Checks if a specific value exists in any of the columns informed, where N+1 is determined by the value of the
    limit column in the same row.

    Args:
    row: The sqlalchemy.engine.row.Row object returned by the query.
    value_to_find: The value you are looking for (ex: 9).
    search_column: The base name of the columns to check (ex: POSTYP).
    limit_column: The name of the column that defines the limit (ex: NBPOS_0).

    Returns:
    Returns:
        A tuple containing:
            - bool: True if the value was found, False otherwise.
            - Optional[int]: The 0-based index of the first column where the value
                             was found, or None if not found or if an error occurred.
    """
    # 1. Obter o limite (número de colunas POSTYP a verificar)
    if limit_column not in row.keys():
        print(f"Erro: Coluna limite '{limit_column}' não encontrada na linha.")
        return False, 0

    limit = row[limit_column]

    # 2. Validar e converter o limite para inteiro
    if limit is None:
        print(f"Aviso: Valor da coluna limite '{limit_column}' é None. Nenhuma coluna POSTYP será verificada.")
        return False, 0

    if limit <= 0:
        # Se o limite for 0 ou negativo, não há colunas a verificar
        return False, 0

    # 3. Iterar e verificar as colunas POSTYP_x
    row_keys = row.keys()  # Obter as chaves da linha uma vez para eficiência

    for i in range(limit):  # Itera de 0 até limit - 1
        column_to_check = f'{search_column}_{i}'

        # 3.1 (Opcional, mas seguro): Verificar se a coluna existe na linha
        # Isso evita KeyErrors se a query não retornou todas as colunas esperadas
        if column_to_check not in row_keys:
            print(
                (
                    f'Aviso: Coluna "{column_to_check}" esperada '
                    f'(baseado em {limit_column}={limit}) não encontrada na linha.'
                )
            )
            continue

        # 3.2 Obter o valor da coluna atual
        current_value = row[column_to_check]

        # 3.3 Comparar com o valor desejado
        # Cuidado com tipos! Se value_to_find é int (9) e current_value
        # pode ser str ('9') ou Decimal(9), a comparação pode precisar de ajuste.
        # Esta comparação simples funciona se os tipos forem compatíveis.
        if current_value is not None and current_value == value_to_find:
            print(f'Valor {value_to_find} encontrado na coluna {column_to_check}.')
            return True, i

    # 4. Se o loop terminar sem encontrar o valor
    print(f'Valor {value_to_find} não encontrado nas colunas {search_column}_0 a {search_column}_{limit - 1}.')

    return False, 0


def _determine_the_period(raz_level: int, date: date) -> int:
    if raz_level == local_menus.Chapter48.NO_RTZ:
        return 0
    elif raz_level == local_menus.Chapter48.ANNUAL:
        return date.year % 100
    elif raz_level == local_menus.Chapter48.MONTHLY:
        return (100 * (date.year % 100)) + date.month
    elif raz_level == 99:  # noqa: PLR2004
        return date.year % 10


def _determine_site_or_society(def_level: int, site: str) -> str:
    if def_level == local_menus.Chapter45.FOLDER:
        return ''
    elif def_level == local_menus.Chapter45.COMPANY:
        # obter o valor do modelo de empresa (sociedade) do banco de dados
        pass
    elif def_level == local_menus.Chapter45.SITE:
        def_level = site
