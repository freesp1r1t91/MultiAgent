

# Mapper de DTO a dominio
from src.infrastructure.input.web.dto.user_dto import InUserDto
from src.infrastructure.output.persistence.user_repository_sqlite import User


def dto_to_domain(user_dto: InUserDto) -> User:
    return User(
        name=user_dto.name,
        email=user_dto.email
    )

# Mapper de dominio a DTO
def domain_to_dto(user: User) -> InUserDto:
    return InUserDto(
        id=0,  # Pydantic no acepta None en id
        name=user.name,
        email=user.email
    )