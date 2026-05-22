import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import header

from langchain_core.runnables import chain
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


model = ChatOpenAI(model="gpt-3.5-turbo")


template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)


@chain
def chatbot(values):
    prompt = template.invoke(values)
    for token in model.stream(prompt):
        yield token


for part in chatbot.stream({"question": "Which model providers offer LLMs?"}):
    print(part)

# Output: Several providers offer LLM (Line Loss Model) services for industries that require accurate estimation and management of losses in their power systems. Some of the top model providers include:\n1. Siemens\n2. GE Grid Solutions\n3. ABB\n4. Schneider Electric\n5. ETAP\n6. SKM Systems Analysis, Inc.\n\nThese providers offer a range of LLM tools and software solutions that can help industries optimize their power systems and manage losses effectively