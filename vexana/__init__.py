import logging
import os
import spamwatch
import sys
import telegram.ext as tg
import time
from Python_ARQ import ARQ
from aiohttp import ClientSession
from inspect import getfullargspec
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import *
from pyrogram import Client
from pyrogram import Client, errors
from pyrogram.types import Message
from telethon import TelegramClient

StartTime = time.time()
CMD_HELP = {}

# enable logging
FORMAT = "[Vexana] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)
LOGGER.info("Vexana is starting. | An VexanaFanClub Project. | Licensed under GPLv3.")
LOGGER.info("Not affiliated to Shie Hashaikai or Villain in any way whatsoever.")
LOGGER.info("Project maintained by: Itzz_axel11 (t.me/Itzz_Axel)")

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)
TOKEN = "5369769829:AAH84a7Wdtth8XaZKGHhOnXDwU731yV53eE"

try:
        OWNER_ID = int(Config.OWNER_ID)
except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

JOIN_LOGGER = "-1532103402"
OWNER_USERNAME = "DEBOJYOTI_IZ_OP"
try:
        DRAGONS = []
        DEV_USERS = [2069126270]
except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

try:
        DEMONS = [2069126270]
except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

try:
        WOLVES = []
except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

try:
        TIGERS = []
except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

EVENT_LOGS = "-1532103402"
WEBHOOK = False
URL = None
PORT = 5000
CERT_PATH = None
API_ID = 12771791
API_HASH = "50af18f49c357d4e53b74c4b8d38b59e"
ARQ_API_URL = "RVLOWH-KMDHXW-QQCPAC-EFICND-ARQ"

DB_URI = "postgresql://postgres:rnOdrDgO0Mhrm6AxwN7q@containers-us-west-58.railway.app:7505/railway"
MONGO_DB_URI = "mongodb://mongo:8RR2A3CfpRsy2hqXipnS@containers-us-west-58.railway.app:7602"
TEMP_DOWNLOAD_DIRECTORY = "/tmp"
OPENWEATHERMAP_ID = ""
BOT_ID = 5369769829
VIRUS_API_KEY = ""
DONATION_LINK = ""
LOAD = []
NO_LOAD = []
DEL_CMDS = True
STRICT_GBAN = True
WORKERS = (8)
BAN_STICKER = ""
ALLOW_EXCL = True
CASH_API_KEY = ""
TIME_API_KEY = ""
AI_API_KEY = ""
WALL_API = ""
SUPPORT_CHAT = "OLiviasupportbot"
SPAMWATCH_SUPPORT_CHAT = "OLiviasupportbot"
SPAMWATCH_API = ""
INFOPIC = True
REDIS_URL = "redis://default:53twL1GHGn4eceqj5I4i@containers-us-west-60.railway.app:5988"

try:
        BL_CHATS = []
except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")

# MongoDB client
print("[INFO]: INITIALIZING DATABASE")
mongo_client = MongoClient(MONGO_DB_URI)
db = mongo_client.vexana

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
session_name = TOKEN.split(":")[0]
pgram = Client(
    session_name,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
)
telethn = TelegramClient("Vexana", API_ID, API_HASH)
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ("https://thearq.tech", "YIECCC-NAJARO-OLLREW-SJSRIP-ARQ", aiohttpsession)
pbot = Client("robot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher

DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from vexana.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
