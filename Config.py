import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23094989"))
    API_HASH = os.environ.get("API_HASH", "b4fecfae36c7567d9a5460704152648e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "lad_ROBOT")
    SUPPORT = os.environ.get("SUPPORT", "hamoddi")
    CHANNEL = os.environ.get("CHANNEL", "algafoyr")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dbf06043e1a68449e403b.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9373d70c437048394a897.jpg")
