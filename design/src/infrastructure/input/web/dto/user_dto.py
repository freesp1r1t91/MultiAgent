from pydantic import BaseModel

# DTO para entrada
class InUserDto(BaseModel):
    name: str
    email: str