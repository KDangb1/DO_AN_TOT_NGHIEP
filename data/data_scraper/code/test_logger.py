from get_logger import telegram_sendtext, get_logger_format, get_datefmt, get_logger, info_n_telegram_sendtext, error_n_telegram_sendtext
import argparse
from cellphoneS_scraper import CellphoneS_scraper
import get_env
from get_logger import telegram_sendtext, get_logger_format, get_datefmt, get_logger, info_n_telegram_sendtext, error_n_telegram_sendtext


env_dict = get_env.get_env()
"""{
#env variable
CellphoneS_url = env_dict.get('CellphoneS_url')         # Google maps URL + '/search/'
bin_location = env_dict.get('bin_location')             # Path to 'Firefox' broswer
web_driver = env_dict.get('web_driver')                  # Path to 'geckodriver'
data_CellphoneS_dir = env_dict.get('data_CellphoneS_dir')
}"""
#telegram logger

logger = get_logger()
logger_format = get_logger_format()
datefmt = get_datefmt()

roomID = env_dict.get("telegram_default_alert_roomID")
logger_level = env_dict.get("logger_level")
if __name__ == "__main__":
    try:
        info_n_telegram_sendtext(logger, message="hello", roomID=roomID, logger_level=logger_level)
    except:
        print("error")