from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Crear instancia FastAPI
app = FastAPI(title="Hola Mundo LangChain API")

# Modelo en Ollama (asegúrate que Ollama esté corriendo: ollama serve)
llm = Ollama(model="llama3")  # Cambia el modelo si usas otro

# Prompt básico
prompt = PromptTemplate(
    input_variables=["pregunta"],
    template="Responde de forma breve: {pregunta}"
)

# Cadena LLM
chain = LLMChain(llm=llm, prompt=prompt)

# Modelo para la petición
class QueryRequest(BaseModel):
    pregunta: str

# Endpoint API
@app.post("/consulta")
def consulta_llm(body: QueryRequest):
    respuesta = chain.run(body.pregunta)
    return {"respuesta": respuesta}
