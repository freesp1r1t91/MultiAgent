from fastapi import FastAPI, Depends
from src.infrastructure.output.persistence.user_repository_sqlite import UserRepositorySQLite, get_repository
from src.application.use_cases.create_user import CreateUserUseCase
from src.infrastructure.input.web.user_controller import get_user_routes
from src.infrastructure.input.web.llm_controller import get_llm_routes

def create_app() -> FastAPI:
    app = FastAPI(title="Design Agent")

    # Use case se crea por request usando Depends
    def get_create_user_uc(repository: UserRepositorySQLite = Depends(get_repository)):
        return CreateUserUseCase(repository)

    # Registrar rutas
    app.include_router(get_user_routes())
    app.include_router(get_llm_routes(), prefix="/llm")
    return app

app = create_app()
