import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI(title="BreakTheCode API")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


class CodeRequest(BaseModel):
	code: str = Field(..., min_length=1, description="C++ code to explain")


class CodeResponse(BaseModel):
	explanation: str


prompt = ChatPromptTemplate.from_messages(
	[
		(
			"system",
			"You explain C++ code to beginners. Use simple language and return "
			"clear headings: What it does, How it works, Problems, and Better version. "
			"If the code has no problem, say so. Do not invent errors.",
		),
		("human", "Explain this C++ code:\n\n{code}"),
	]
)


def get_chain():
	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		raise HTTPException(
			status_code=500,
			detail="OPENAI_API_KEY is not configured. Add it to backend/.env.",
		)

	model = ChatOpenAI(
		model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
		temperature=0,
		api_key=api_key,
	)
	return prompt | model


@app.get("/")
def health_check():
	return {"message": "BreakTheCode API is running"}


@app.post("/explain", response_model=CodeResponse)
def explain_code(request: CodeRequest):
	result = get_chain().invoke({"code": request.code})
	return CodeResponse(explanation=result.content)
