from abc import ABC, abstractmethod

class LLMServicePort(ABC):
    @abstractmethod
    def consult(self, prompt: str) -> str:
        pass