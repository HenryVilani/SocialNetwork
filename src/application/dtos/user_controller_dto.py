
from typing import List, Optional
from pydantic import BaseModel


class CreateUserControllerInDTO(BaseModel):

    username: str
    email: str
    password: str

class CreateUseControllerOutDTO(BaseModel):

    id: str

    username: str
    email: str

    role: str

class LoginUserControllerInDTO(BaseModel):

    email: str
    password: str

class LoginUserControllerOutDTO(BaseModel):

    token: str

class GetUserControllerOutDTO(BaseModel):

    id: str
    username: str
    email: str
    role: str
    
class UpdateUserControllerInDTO(BaseModel):
    
    username: str
    
class UpdateUserControllerOutDTO(BaseModel):
    
    id: str

    username: str
    email: str

    role: str
    
class DeleteUserControllerOutDTO(BaseModel):
    
    status: str
    
class SearchUserControllerOutDTO(BaseModel):
    
    users: List[GetUserControllerOutDTO]
    next_segment: Optional[int]