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
roomID = env_dict.get("telegram_default_alert_roomID")
#telegram logger
logger = get_logger()
logger_format = get_logger_format()
datefmt = get_datefmt()


# Define argument parser
parser = argparse.ArgumentParser(description='Crawl Data on CellphoneS')

parser.add_argument('-c', '--categorys', dest='categorys', help='Categorys crawled, i.e. mobile, laptop, tablet, watch, audio, smarthome, accessory, screen_pc, tv', type=str)

parser.add_argument('-s', '--speed', dest='speed', help='data scraping speed, fastest: 0, slowest: 4. Default: 0', type=int, default=0)

args = parser.parse_args()

if __name__ == "__main__":
    #argument parser
    categoryList =  ((args.categorys).lower().replace(' ', '')).split(',')
    speed = int(args.speed) % 5
    
    cellphoneS_scraper = CellphoneS_scraper(CellphoneS_url=CellphoneS_url, bin_location=bin_location, web_driver=web_driver, logger=logger, data_storage_dir=data_CellphoneS_dir, roomID=roomID, data_scraping_speed=speed)
    
    for category in categoryList:
        try:
            cellphoneS_scraper.collect_products_by_category(category)
            
        except Exception as e:
            print(f"{str(e)}")
            
            raise
    