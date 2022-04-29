import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "xxxxxxxx"))
API_HASH = getenv("API_HASH", "xxxxxxxx")
BOT_TOKEN = getenv("BOT_TOKEN", "xxxxxxxx")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "xxxxxxxx")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256 702821224 5390904232").split()))
aiohttpsession = aiohttp.ClientSession()
