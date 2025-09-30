from fastapi import APIRouter, Depends

from src.infrastructure.output.adapters.llama3_service_adapter import Llama3ServiceAdapter
from src.application.use_cases.ask_prompt import AskPromptUseCase
from src.domain.ports.llm_service_port import LLMServicePort
from src.infrastructure.input.web.dto.promt_dto import QueryRequest



llm_service: LLMServicePort = Llama3ServiceAdapter(temperature=0.7)
use_case = AskPromptUseCase(llm_service)

# Crear router
router = APIRouter()

def get_llm_routes():
    
    @router.post("/query")
    def query_llama3(
        request: QueryRequest
    ):
        return use_case.execute(request.pregunta)
    
    return router