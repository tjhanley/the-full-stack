from pydantic import BaseModel, Field, validator
from typing import List, Optional
from .message import Message


# Define the class for the GPT request
class GPTRequest(BaseModel):
    gpt_model: Optional[str] = "gpt-3.5-turbo"
    messages: List[Message]

    @validator("gpt_model", pre=True, always=True)
    def set_gpt_model(cls, v):
        return v.lower() if v is not None else "gpt-3.5-turbo"

    @validator("messages")
    def validate_roles(cls, messages):
        if not any(msg.role.lower() == "system" for msg in messages):
            raise ValueError("At least one message with the 'system' role is required")
        if not any(msg.role.lower() == "user" for msg in messages):
            raise ValueError("At least one message with the 'user' role is required")
        return messages
