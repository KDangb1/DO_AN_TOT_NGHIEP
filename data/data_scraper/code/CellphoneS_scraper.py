from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random
import pandas as pd
from datetime import date
import get_env
import os
import csv
from selenium.webdriver.common.keys import Keys
from get_logger import telegram_sendtext, get_logger_format, get_datefmt, get_logger, info_n_telegram_sendtext, error_n_telegram_sendtext


env_dict = get_env.get_env()


class CellphoneS_scraper:
    def __init__(self, CellphoneS_url, bin_location, web_driver, logger, data_storage_dir, roomID, data_scraping_speed):
        self.class_name = "CellphoneS_Crawler"
        self.CellphoneS_url = CellphoneS_url           # Google maps URL + '/search/'
        self.bin_location = bin_location               # Path to 'Firefox' broswer
        self.web_driver = web_driver                   # Path to 'geckodriver'

        self.logger = logger
        self.roomID = roomID
        
        self.data_storage_dir = data_storage_dir           # Directory path to the directory containing the data
        self.data_scraping_speed = data_scraping_speed
        
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
                return 1
        except:
            return 0
        

    #Show all items in this(CellphoneS) page
    def show_all_items_in_this_page(self):
        not_show_all_items_yet = True
        popup_banner_closed = False

        while not_show_all_items_yet:
            try:
                try:
                    #set to stop this function
                    not_show_all_items_yet = False
                    #
                    btn_show_more_element = self.driver.find_element(By.CLASS_NAME, "cps-block-content_btn-showmore").find_element(By.CSS_SELECTOR, "a.button")

                    if btn_show_more_element.text:
                        btn_show_more_element.click()
                        time.sleep(self.data_scraping_speed + random.randrange(3,5))
                        #set to continue this function
                        not_show_all_items_yet = True

                except Exception as e:
                    #
                    if popup_banner_closed == False:
                        popup_banner_closed= self.close_popup_banner()
                        not_show_all_items_yet = True
                    #
                    else:
                        not_show_all_items_yet = False
                        break        
                
            except Exception as e:
                error_n_telegram_sendtext(logger=self.logger, message=f"{self.class_name} | show all items in page | Encounter error: {str(e)}", roomID=self.roomID)
                raise


    def get_all_items_in_page(self):
           
        all_products_info_ele = self.driver.find_elements(By.CLASS_NAME, "product-info")
        list_products = []
        for product_element in all_products_info_ele:
            try:
                product_src_image = product_element.find_element(By.CLASS_NAME, "product__img").get_attribute("src")
                product_name = product_element.find_element(By.CLASS_NAME, 'product__name').text
                product_price_new = product_element.find_element(By.CLASS_NAME, 'product__price--show').text
                try:
                    product_price_old = product_element.find_element(By.CLASS_NAME, 'product__price--through').text   
                except:
                    product_price_old = "0"
                product_info = [product_name, product_src_image, product_price_new, product_price_old]
                list_products.append(product_info)
                
            except Exception as e:
                error_n_telegram_sendtext(logger=self.logger, message=f"{self.class_name} | show all items in page | Encounter error: {str(e)}", roomID=self.roomID)
                raise
            
        df_products = pd.DataFrame(list_products, columns =["product_name", "product_src_image", "product_price_new", "product_price_old"])
        return df_products

    def save_crawled_data(self, df_products, category, columns = ["product_name", "product_src_image", "product_price_new", "product_price_old"]):
        
        df_products.to_csv(f"{self.data_storage_dir}/CellphoneS_{category}.csv", index=False, columns=columns, mode="w")
        
        info_n_telegram_sendtext(logger=self.logger, message=f"{self.class_name} | Collect {category} | {len(df_products)} items", roomID=self.roomID)
    """
    
    """ 
    def collect_products_by_category(self, category):
        """
        All category in cellphoneS:
        mobile, laptop, tablet, watch, audio, smarthome, accessory, screen_pc, tv
        """
        
        self.driver.get(f'{self.CellphoneS_url}{category}.html')
        time.sleep(self.data_scraping_speed + random.randrange(5,7))
        #Show all phones in this(CellphoneS) page
        self.show_all_items_in_this_page()
        try:
            df_all_items_in_page = self.get_all_items_in_page()

            self.save_crawled_data(df_products=df_all_items_in_page)
            
        except Exception as e:
            error_n_telegram_sendtext(logger=self.logger, message=f"{self.class_name} | Collect {category} | Encounter error: {str(e)}", roomID=self.roomID)
            raise
        

    def mobile_collector(self):
        #Chat bot send message to chat box logging run time
        
        #Go to the phone sales page
        self.driver.get(f'{self.CellphoneS_url}mobile.html')
        time.sleep(self.data_scraping_speed + random.randrange(5,7))
        #Show all phones in this(CellphoneS) page
        self.show_all_items_in_this_page()
        try:
            df_all_items_in_page = self.get_all_items_in_page()
            #Save data
            print(df_all_items_in_page)
            self.save_crawled_data(df_products=df_all_items_in_page)
            #logging
            print("Success")
        except Exception as e:
            
            #logging
            print("error")
            pass
  