from sample_config import Config
from translation import Translation

class Development(Config):
  TG_BOT_TOKEN = "value"
  URL = "https://<appname>.herokuapp.com/"
  
  CHUNK_SIZE = 10280
  PORT = int(os.environ.get("PORT", 5000))
    # Python3 ReQuests CHUNK SIZ
    # MyTelegram.org
    # configurtion required while creating new application
  APP_TITLE = "Legend Api Scrapper Bot"
  APP_SHORT_NAME = "Legend Api Scrapper Bot"
  APP_URL = "https://telegram.dog/LegendApiScrapperBot"
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
    # https://github.com/SpEcHiDe/MyTelegramOrgRoBot/issues/3
  APP_DESCRIPTION = "created by @LegendBoy_XD"
    #
  FOOTER_TEXT = "❤️ @LegendBoy_XD"
    # the strings used in the different messages
    # in the bot
  START_TEXT = Translation.START_TEXT
  AFTER_RECVD_CODE_TEXT = Translation.AFTER_RECVD_CODE_TEXT
    
  BEFORE_SUCC_LOGIN = Translation.BEFORE_SUCC_LOGIN
    
  ERRED_PAGE = Translation.ERRED_PAGE
  CANCELLED_MESG = Translation.CANCELLED_MESG
    
  IN_VALID_CODE_PVDED = Translation.IN_VALID_CODE_PVDED
    
  IN_VALID_PHNO_PVDED = Translation.IN_VALID_PHNO_PVDED
  
    # the below strings are not meant to be configurable :\(
  VFCN_CHECKING_ONE = "\"It is a beautiful and terrible thing, and should therefore be treated with great caution.\""
  ORIGINAL_CODE = "aHR0cHM6Ly9naXRodWIuY29tL0xFR0VORC1BSS9BUEktU0NSQVBQRVIvcmF3L21haW4vYm90LnB5"
  VFCN_RETURN_STATUS = "'compareFiles' returned '{ret_status}'."
  
