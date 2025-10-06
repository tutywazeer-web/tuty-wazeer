#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8249098387:AAG8f71BFd68ikKqaU81GcWRXA3bCCRomhw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27642526"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8bc14441805c29b64843165c1d73ce31")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002874991507"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7653921320"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://tutywazeer:12345@cluster0.xmhbooi.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "tutywazeer")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1003192767149"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","https://i.ibb.co/671SqSMt/x.jpg")
START_MSG = os.environ.get("START_MESSAGE", "Hi {mention}, This bot provides Anime Episodes.\n\nIf you want any other anime then message here 👉 @ATX_Anime_Tamil")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hey {mention}, Please join our <a href='https://t.me/Tamil_Animes_channel'>channel</a> and try again 👇👇👇")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "900"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "Hi, I'm alive and ready to store and share files.\n\n<b>⏱ UPTIME : </b>{uptime}"
USER_REPLY_TEXT = "If you have any problems in the episodes or need any other animes inform it in our group @ATX_Anime_Tamil"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
