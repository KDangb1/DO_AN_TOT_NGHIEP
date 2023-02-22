import argparse
from cellphoneS_scraper import CellphoneS_scraper
import get_env
from get_logger import telegram_sendtext, get_logger_format, get_datefmt, get_logger, info_n_telegram_sendtext, error_n_telegram_sendtext


env_dict = get_env.get_env()

#env variable
CellphoneS_url = env_dict.get('CellphoneS_url')         # Google maps URL + '/search/'
bin_location = env_dict.get('bin_location')             # Path to 'Firefox' broswer
web_driver = env_dict.get('web_driver')                  # Path to 'geckodriver'
data_CellphoneS_dir = env_dict.get('data_CellphoneS_dir')

#telegram logger

logger = get_logger()
logger_format = get_logger_format()
datefmt = get_datefmt()


if __name__ == "__main__":
    cellphoneS_scraper = CellphoneS_scraper(CellphoneS_url=CellphoneS_url, bin_location=bin_location, web_driver=web_driver, logger=logger, data_storage_dir=data_CellphoneS_dir)
    
    cellphoneS_scraper.mobile_collector()