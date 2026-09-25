import os

from fastapi import HTTPException
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

from prompts import code_explanation_prompt


load_dotenv()


def get_code_explanation_chain():
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
	return code_explanation_prompt | model


def explain_code(code: str) -> str:
	result = get_code_explanation_chain().invoke({"code": code})
	return result.content
