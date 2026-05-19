import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_core.globals import set_verbose
set_verbose(True)

from langchain_core.globals import set_debug
set_debug(True)

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai.chat_models import ChatOpenAI

model = ChatOpenAI()
system_msg = SystemMessage(
    "You are a helpful assistant that responds to questions in Chinese."
)
human_msg = HumanMessage("What is the capital of France?")

response = model.invoke([system_msg, human_msg])
print(response.content)
