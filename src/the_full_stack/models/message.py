from pydantic import BaseModel, Field, validator


# Define the class for individual messages
class Message(BaseModel):
    role: str = Field(default=None, examples=["system", "user"])
    content: str = Field(
        default=None,
        examples=[
            "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
            "Compose a poem that explains the concept of recursion in programming.",
        ],
    )

    @validator("content")
    def content_must_not_be_empty(cls, value):
        if not value or value.strip() == "":
            raise ValueError("Content must not be empty")
        return value
