import os
from dotenv import load_dotenv

load_dotenv(f'./.env')


def get_env():
    env_dict = {
        'logger_name': os.getenv('logger_name')
        ,'logger_level': int(os.getenv('logger_level'))
        ,'telegram_bot_token': os.getenv('telegram_bot_token')
        ,'telegram_default_alert_roomID': os.getenv('telegram_default_alert_roomID')
        ,'bin_location': os.getenv('bin_location')
        , 'web_driver': os.getenv('web_driver')
        , 'data_CellphoneS_dir': os.getenv('data_CellphoneS_dir')
        , 'CellphoneS_url': os.getenv('CellphoneS_url')
    }
    
    return env_dict