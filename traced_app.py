from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "What is Python?",
    "What is LangChain?",
    "What is Retrieval Augmented Generation?"
]

for prompt in prompts:
    response = llm.invoke(prompt)
    print("\nPrompt:", prompt)
    print("Response:", response.content)