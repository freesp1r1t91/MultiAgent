from src.domain.ports.llm_service_port import LLMServicePort


class AskPromptUseCase:
    def __init__(self, llm_service: LLMServicePort):
        self.llm_service = llm_service

    def execute(self, pregunta: str):
        # Aquí podría haber reglas de negocio (validaciones, logging, etc.)
        return self.llm_service.consult(pregunta)
        