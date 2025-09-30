from src.domain.ports.user_repository_port import UserRepositoryPort

class CreateUserUseCase:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def execute(self, user):
        return self.repository.save(user)
