from pydantic import BaseModel

# DTO para salida
class OutUserDto(BaseModel):
    id: int
    name: str
    email: str