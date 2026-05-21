import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_core.globals import set_verbose
set_verbose(True)

from langchain_core.globals import set_debug
set_debug(True)


from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_openai.chat_models import ChatOpenAI

from langchain_core.globals import set_verbose
set_verbose(True)

from langchain_core.globals import set_debug
set_debug(True)

model = ChatOpenAI(model="gpt-3.5-turbo") # type: ignore[call-arg]

response = model.invoke("The houston sky now is")
print(response.content)
