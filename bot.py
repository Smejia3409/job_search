from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Bot:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # makes window full screen
        self.driver.get("https://www.indeed.com/")


    def open_page(self):
        print("openning indeed")


    # def search(self, job, location):
    #     # finding input id for job and location input
    #     job_input = self.driver.find_element(by=By.ID, value="text-input-what")
    #     location_input = self.driver.find_element(by=By.ID, value="text-input-where")
    #
    #     # passing args as input
    #     job_input.send_keys(job)
    #     location_input.send_keys(location)
    #     location_input.click()

