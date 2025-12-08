
from pydantic import BaseModel


class AuthPayloadDTO(BaseModel):

    user_id: str
    role: str
