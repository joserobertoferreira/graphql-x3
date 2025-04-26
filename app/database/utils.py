import inspect

from sqlalchemy.orm import class_mapper

from app.core.settings import DB_SCHEMA


def generate_select_query(model, strawberry_type, is_core: bool = False):
    """
    Is is_core True, the function will generate the access to the columns in the format Model.__table__.c.column_name.
    If is_core False, the function will generate a query based on the fields of a SQLAlchemy model and a
    Strawberry type.
    """

    # Obter os campos do modelo SQLAlchemy
    model_fields = [column.name for column in class_mapper(model).columns]

    # Obter os campos do tipo Strawberry
    strawberry_fields = [field[0] for field in inspect.getmembers(strawberry_type) if not field[0].startswith('__')]

    print(f'Model fields: {model_fields}')

    # Filtrar os campos comuns entre o modelo e o tipo
    common_fields = set(model_fields).intersection(set(strawberry_fields))

    print(f'Common fields: {common_fields}')

    # Gerar a query SQL (SELECT)
    if is_core:
        query = [f'{model.__name__}.__table__.c.{field}' for field in common_fields]
    else:
        select_columns = ', '.join(common_fields)
        query = f'SELECT {select_columns} FROM {DB_SCHEMA}.{model.__tablename__}'

    return query
