from pydantic import BaseModel

# Modelo de petición
class QueryRequest(BaseModel):
    pregunta: str