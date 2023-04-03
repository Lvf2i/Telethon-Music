import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23094989"))
    API_HASH = os.environ.get("API_HASH", "b4fecfae36c7567d9a5460704152648e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5952607087:AAGA6X7_-FNGfSgbmV7EvP61mpbytyQGMu8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu7sqOtHAAknnKfdaxQOuwIWbjNDhHY7m7iiZ8iXKDnMlrErdD70R3OEJc1vR0lZsHAjWCYbPIRLOCEdruBI8-Z3C_JbuluvvGMZyVx3Hynxs4BmPRttRsRZm-Ie_hys54md_FxhJ8-bdEBiTaWTP22i_05Od0o-4Nb7Ikj9C797aoDZAKiqrWIEVj539IA4UwYZaRqWRzIbqCV5wxyt67TnYPhPu6WAwtfM02OY2gaKwyU6ctiVkh6_hZ_yPa-fgL3IpOQeuhDy2F3LRgVnQN-O-Q5tDRNJq-xzIjZTv6VbRpT6E9n0uKiF-SB1hGsLXPihtXjLQXDlUCGUYf2U0ob4=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "e088bot")
    SUPPORT = os.environ.get("SUPPORT", "hamoddi")
    CHANNEL = os.environ.get("CHANNEL", "algafoyr")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dbf06043e1a68449e403b.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9373d70c437048394a897.jpg")
