import os
from translation import Translation

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1778555256:AAE38G7btdkDdbJFM9sM95IN53AdurPbQgk")
    # required for running on Heroku
    URL = os.environ.get("URL", "")
    PORT = int(os.environ.get("PORT", 5000))
    # Python3 ReQuests CHUNK SIZE
    CHUNK_SIZE = 10280
    # MyTelegram.org
    # configurtion required while creating new application
    APP_TITLE = os.environ.get("APP_TITLE", "Shizutg")
    APP_SHORT_NAME = os.environ.get("APP_SHORT_NAME", "Shizutg")
    APP_URL = os.environ.get("APP_URL", "http://t.me/MyTelegramORG_herobot")
    # these platform informations were obtained
    # on 27.01.2020 21:15:50 IST
    APP_PLATFORM = [
        "android",
        "ios",
        "wp",
        "bb",
        "desktop",
        "web",
        "ubp",
        "other"
    ]
    # if any of the platform, does not work
    # please reopen
    # https://github.com/TeamShizu/TelegramORG/issues/3
    APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION", "created using http://t.me/MyTelegramORG_herobot")
    #
    FOOTER_TEXT = os.environ.get("FTEXT", "Please Subscribe ❤️ @ShizuSupport_Official")
    # the strings used in the different messages
    # in the bot
    START_TEXT = os.environ.get("START_TEXT", Translation.START_TEXT)
    AFTER_RECVD_CODE_TEXT = os.environ.get(
        "AFTER_RECVD_CODE_TEXT",
        Translation.AFTER_RECVD_CODE_TEXT
    )
    BEFORE_SUCC_LOGIN = os.environ.get(
        "BEFORE_SUCC_LOGIN",
        Translation.BEFORE_SUCC_LOGIN
    )
    ERRED_PAGE = os.environ.get("ERRED_PAGE", Translation.ERRED_PAGE)
    CANCELLED_MESG = os.environ.get("CANCELLED_MESG", Translation.CANCELLED_MESG)
    IN_VALID_CODE_PVDED = os.environ.get(
        "IN_VALID_CODE_PVDED",
        Translation.IN_VALID_CODE_PVDED
    )
    IN_VALID_PHNO_PVDED = os.environ.get(
        "IN_VALID_PHNO_PVDED",
        Translation.IN_VALID_PHNO_PVDED
    )


class Development(Config):
    pass
