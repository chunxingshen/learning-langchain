from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_core.globals import set_verbose
set_verbose(True)


from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage

model = ChatOpenAI()
prompt = [HumanMessage("What is the capital of France?")]

response = model.invoke(prompt)
print(response.content)
