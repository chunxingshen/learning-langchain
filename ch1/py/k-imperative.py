import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import header

from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain

# the building blocks

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant with attitude."),
        ("human", "{question}"),
    ]
)

model = ChatOpenAI(model="gpt-3.5-turbo")

# combine them in a function
# @chain decorator adds the same Runnable interface for any function you write


@chain
def chatbot(values):
    prompt = template.invoke(values)
    return model.invoke(prompt)


# use it

response = chatbot.invoke({"question": "Which model providers offer LLMs?"})
print(response.content)

"""
Answer:
There are various institutions and universities around the world that offer LLM (Master of Laws) programs. Some well-known providers include:

1. Harvard Law School
2. Yale Law School
3. Stanford Law School
4. University of Oxford
5. University of Cambridge
6. New York University (NYU) School of Law
7. London School of Economics and Political Science (LSE)
8. University of California, Berkeley School of Law
9. University of Michigan Law School
10. Georgetown University Law Center

These are just a few examples of prestigious institutions that offer LLM programs. It is important to research and consider various factors such as program structure, faculty, specialized areas of study, and location when choosing a program that suits your academic and career goals.

Gemini:
is LLM and master of laws the same?

Yes, an LLM and a Master of Laws are the exact same thing. "LLM" is just the widely used abbreviation for the degree, which comes from the Latin phrase Legum Magister, where the doubled "L" indicates the plural word for laws.

"""