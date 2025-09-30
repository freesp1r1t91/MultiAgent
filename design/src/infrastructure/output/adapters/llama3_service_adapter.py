from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from src.domain.ports.llm_service_port import LLMServicePort

class Llama3ServiceAdapter(LLMServicePort):
    def __init__(self, temperature: float = 0.7):
        self.temperature = temperature
    
        # Configuración del LLM
        self.llm = OllamaLLM(
            model="llama3", 
            temperature=self.temperature
            )  # Asegúrate de que Ollama esté corriendo
        prompt = PromptTemplate(
            input_variables=["pregunta"],
            template="Responde de forma breve: {pregunta}"
        )

        self.resultado = prompt | self.llm

    def consult(self, prompt: str):
        respuesta = self.resultado.invoke({prompt})
        return {"pregunta": prompt, "respuesta": respuesta}