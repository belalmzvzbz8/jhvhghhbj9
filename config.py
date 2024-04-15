import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("7181506064:AAEk-DTK_BiM3DoatNDcVfpITLgQCkdnE7s", "")

    APP_ID = int(os.environ.get("22865033", 22865033))

    API_HASH = os.environ.get("API_HASH", "62ba116490803164ee88d4e477d5da84")
