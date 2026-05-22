import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import header

from langchain_core.runnables import chain
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)

model = ChatOpenAI(model="gpt-3.5-turbo")


@chain
async def chatbot(values):
    prompt = await template.ainvoke(values)
    return await model.ainvoke(prompt)


async def main():
    return await chatbot.ainvoke({"question": "Which model providers offer LLMs?"})

if __name__ == "__main__":
    import asyncio
    print(asyncio.run(main()))
#Output: "Many law schools and universities around the world offer LLM (Master of Laws) programs...