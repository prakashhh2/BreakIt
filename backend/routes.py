from fastapi import APIRouter

from schemas import CodeRequest, CodeResponse
from services import explain_code


router = APIRouter()


@router.get("/")
def health_check():
	return {"message": "BreakTheCode API is running"}


@router.post("/explain", response_model=CodeResponse)
def explain_code_route(request: CodeRequest):
	return CodeResponse(explanation=explain_code(request.code))
