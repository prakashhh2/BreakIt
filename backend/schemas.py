from pydantic import BaseModel, Field


class CodeRequest(BaseModel):
	code: str = Field(..., min_length=1, description="C++ code to explain")


class CodeResponse(BaseModel):
	explanation: str
