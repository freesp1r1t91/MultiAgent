from src.domain.ports.user_repository_port import UserRepositoryPort
from typing import List
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional

# Modelo
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

# Crear motor
engine = create_engine("sqlite:///users.db")
SQLModel.metadata.create_all(engine)

# Función que devuelve el repositorio (inyección de dependencias)
def get_repository():
    with Session(engine) as session:
        yield UserRepositorySQLite(session)


class UserRepositorySQLite(UserRepositoryPort):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def get_all(self) -> List[User]:
        stmt = select(User)
        return self.session.exec(stmt).all()