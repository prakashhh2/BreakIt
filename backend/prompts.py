from langchain_core.prompts import ChatPromptTemplate


code_explanation_prompt = ChatPromptTemplate.from_messages(
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
