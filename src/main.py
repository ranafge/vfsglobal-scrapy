import pandas as pd
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class vsfglobals:
    def __init__(self):
        self.driver = ""
        self.dataframe = ""
        self.credentials = {
            'email': 'ranafge@gmail.com',
            'password': 'Pass1478@'
        }
        self.questions = []
        self.answer = []
    def start_driver(self):
        options = Options()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Brave()
        self.driver.get('https://visa.vfsglobal.com/bgd/en/ita/dashboard')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]'))).click()
        # Wait to load the website 
       
        # WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "success-text")))
        # print(" Human varification checking success")
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,'//*[@id="onetrust-accept-btn-handler"]'))).click()
        print("Clicked accept cookies")    
        # self.driver.refresh_session()
        
       
      
    def stop_driver(self):
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)
    def initialize_columns(self, columns):
        self.dataframe = pd.DataFrame(columns=columns)
    def set_credentials(self, email, password):
        self.credentials['email'] = email
        self.credentials['password'] = password
    def login(self):
        # self.open_url('https://visa.vfsglobal.com/bgd/en/ita/application-detail')
        # self.open_url('https://visa.vfsglobal.com/bgd/en/ita/login')
        self.driver.implicitly_wait(10)
        # Wait to load the website 
        # print("Waiting for 10 seconds...")
       
        # WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "success-text")))
        # print(" Human varification checking success")
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,'//*[@id="onetrust-accept-btn-handler"]'))).click()
        # print("Clicked accept cookies")    
        # self.driver.refresh_session()
        #WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler"))).click()
        if self.credentials["email"] and self.credentials["password"]:
            # accept all cookies tab -click action
            
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "mat-input-0")))
            element.send_keys("ranafge@gmail.com")
            print("Enter email")
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "mat-input-1")))
            element.send_keys("Pass1478")
            print("Entered password")
            time.sleep(3)
            # svg success text appear to be 
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.ID, "success-text")))
            element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.mat-button-wrapper")))
            element.click()
            
            self.driver.refresh()

if __name__ == "__main__":
    scrapy = vsfglobals()
    scrapy.start_driver()
    time.sleep(10)
    # scrapy.set_credentials("ranafge@gmail.com", "Pass1478@")
    scrapy.login()
    scrapy.stop_driver()