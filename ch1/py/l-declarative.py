#LCEL: LangChain Expression Language

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import header

from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# the building blocks

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)

model = ChatOpenAI()

# combine them with the | operator

chatbot = template | model

# use it

response = chatbot.invoke({"question": "Which model providers offer LLMs?"})
print(response.content)

# streaming

for part in chatbot.stream({"question": "Which model providers offer LLMs?"}):
    print(part)
