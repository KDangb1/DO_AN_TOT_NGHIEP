from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random
import pandas as pd
from datetime import date
import get_env
import os
from selenium.webdriver.common.keys import Keys

env_dict = get_env.get_env()


class CellphoneS_scraper:
    def __init__(self, CellphoneS_url, bin_location, web_driver, logger, data_storage_dir):
        self.CellphoneS_url = CellphoneS_url           # Google maps URL + '/search/'
        self.bin_location = bin_location               # Path to 'Firefox' broswer
        self.web_driver = web_driver                   # Path to 'geckodriver'

        self.logger = logger
        
        self.data_storage_dir = data_storage_dir           # Directory path to the directory containing the data
        
        options = Options()
        options.binary_location = self.bin_location
        # options.headless = True                       
        self.driver = webdriver.Firefox(executable_path=web_driver, service_log_path=os.devnull ,options=options)
    
    #Close the popup banner in this(CellphoneS) page
    def close_popup_banner(self):
        try:
            cancel_popup_banner_element = self.driver.find_element(By.CLASS_NAME, "cancel-button-top")
            if cancel_popup_banner_element:
                cancel_popup_banner_element.click()
        except:
            pass
    
    #Show all items in this(CellphoneS) page
    def show_all_items_in_this_page(self):
        not_show_all_items_yet = True
        while not_show_all_items_yet:
            try:
                try:
                    btn_show_more_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/div/div[7]/div[5]/div/div[2]/a")
                    if btn_show_more_element:
                        btn_show_more_element.click()
                        time.sleep(random.randrange(4,8))
                    else:
                        break
                except:
                    self.close_popup_banner()
            except:
                break

    """
    
    """ 
    def mobile_collector(self):
        #Go to the phone sales page
        self.driver.get(f'{self.CellphoneS_url}mobile.html')
        #Show all phones in this(CellphoneS) page
        self.show_all_items_in_this_page()
            
        #
    
    def laptop_collector(self):
        pass
    
    def tablet_collector(self):
        pass
    
    def watch_collector(self):
        pass

    def audio_collector(self):
        pass
    
    def smarthome_collector(self):
        pass
    
    def accessory_collector(self):
        pass
    
    def screen_collector(self):
        pass
    
    def television_collector(self):
        pass
        