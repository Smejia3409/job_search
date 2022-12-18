from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Bot(webdriver.Chrome):
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        #keeps browser on
        self.teardown = False
        # makes window full screen
        super(Bot, self).__init__( service=Service(ChromeDriverManager().install()), options=options)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()



    def open_page(self):
        print("openning indeed")
        self.get("https://indeed.com")




    def search(self, job, location):
        # finding input id for job and location input
        job_input = self.find_element(by=By.ID, value="text-input-what")
        location_input = self.find_element(by=By.ID, value="text-input-where")
        job_input.clear()
        # passing args as input
        job_input.send_keys(job)
        location_input.send_keys(location)
        job_input.send_keys(Keys.ENTER)


    def get_jobs(self):
        job_list = self.find_elements(by=By.CLASS_NAME, value="resultContent")

        for job in job_list:
            title = job.find_element(by=By.TAG_NAME, value="span")
            link = job.find_element(by=By.TAG_NAME, value="a")
            print(title.get_attribute("innerHTML"), link.get_attribute("href"))
        if(len(job)==0):
            print("No results found")
