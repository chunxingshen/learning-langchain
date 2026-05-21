import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_core.globals import set_verbose
set_verbose(True)

from langchain_core.globals import set_debug
set_debug(True)