from abc import ABC, abstractmethod
from typing import List
from src.domain.models.user import User

class UserRepositoryPort(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass
