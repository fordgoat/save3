from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29486311")
    API_HASH = environ.get("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7300347870:AAEd4rWeuOwiLaVh70RuyTSNxDOB4IVXV6I") 
    BOT_SESSION = environ.get("BOT_SESSION", "eyon") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "eyon-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6396921435').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
