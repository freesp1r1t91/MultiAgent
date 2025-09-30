from fastapi import APIRouter, Depends
from typing import List
from src.infrastructure.input.web.mapper.user_mapper import dto_to_domain
from src.infrastructure.output.dto.user_dto import OutUserDto
from src.infrastructure.input.web.dto.user_dto import InUserDto
from src.infrastructure.output.persistence.user_repository_sqlite import get_repository
from src.application.use_cases.create_user import CreateUserUseCase
from src.domain.ports.user_repository_port import UserRepositoryPort

router = APIRouter()



def get_user_routes():
    @router.post("/users", response_model=OutUserDto)
    def create_user(
        request: InUserDto,
        repository: UserRepositoryPort = Depends(get_repository)
    ):
        uc = CreateUserUseCase(repository)
        user = uc.CreateUser(dto_to_domain(request))
        return OutUserDto(**user.__dict__)

    @router.get("/users", response_model=List[OutUserDto])
    def list_users(
        repository: UserRepositoryPort = Depends(get_repository)
    ):
        users = repository.get_all()
        return [OutUserDto(**u.__dict__) for u in users]

    return router
