import strawberry
from sqlalchemy.orm import Session
from strawberry.types import Info

from app.graphql.types.editor import EditorInput, EditorType
from app.models.editor import Editor as EditorModel
from app.services.counters import get_next_counter

ContextType = dict


# --- Função Síncrona Auxiliar para Lógica de DB ---
def _create_editor(db: Session, editor_input: EditorInput, current_user: str) -> EditorModel:
    """Função síncrona que executa toda a lógica de banco de dados."""
    try:
        # 1. Obter o próximo editor_id sequencial (chamada síncrona)
        next_id_str = get_next_counter(db, 'ZRDX')

        if not next_id_str:
            raise ValueError('Não foi possível obter o próximo ID do contador.')

        new_editor = EditorModel(
            name=editor_input.name,
            contact=editor_input.contact,
            email=editor_input.email,
            is_active=editor_input.is_active,
            editor_id=next_id_str,
            createUser=current_user,
            updateUser=current_user,
        )

        db.add(new_editor)
        db.flush()
        db.commit()
        db.refresh(new_editor)

        print(f'Editor criado com ROWID: {new_editor.id} e EditorID: {new_editor.editor_id}')

        return new_editor

    except Exception as e:
        # logging.error(f'Erro dentro de _create_editor_sync: {e}', exc_info=True)
        db.rollback()  # Desfaz tudo se houve erro
        # Re-levanta a exceção para ser pega pelo run_sync/resolver
        raise ValueError(f'Não foi possível criar o editor: {e}') from e


# --- Classe de Mutação Strawberry ---
@strawberry.type
class EditorMutation:
    @strawberry.field
    def create_editor(  # O resolver ainda é async  # noqa: PLR6301
        self, info: Info[ContextType, None], editor_input: EditorInput
    ) -> EditorType:
        """Cria um novo registro de Editor (usando DB síncrono)."""
        # 1. Obter a SESSÃO SÍNCRONA do contexto
        db: Session = info.context.get('db')
        if not db:
            raise ValueError('Sessão do banco de dados (sync) não encontrada.')

        current_user = 'INTER'

        try:
            # 2. Executar a função síncrona auxiliar em um thread separado
            new_editor_instance = _create_editor(db=db, editor_input=editor_input, current_user=current_user)
            # Alternativa Python 3.9+:
            # new_editor_instance = await asyncio.to_thread(
            #     _create_editor, db, editor_input, current_user
            # )

            # 3. Retornar o resultado (Strawberry mapeará para EditorType)
            return new_editor_instance

        except Exception as e:
            # Captura exceções levantadas por _create_editor
            # logging.error(f'Erro no resolver create_editor chamando run: {e}', exc_info=True)
            # Retorne um erro GraphQL apropriado
            # Você pode querer usar um tipo de erro GraphQL customizado
            raise Exception(f'Erro ao processar a criação do editor: {e}')
