from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from prettytable import PrettyTable


def job_table(jobs):
    table = PrettyTable()
    table.field_names = ["Job Title", "Link"]

    for job in jobs:
        title = job.find_element(by=By.TAG_NAME, value="span").get_attribute("innerHTML")
        link = job.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
        table.add_row([title, link])

    print(table)


class Bot(webdriver.Chrome):
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        # keeps browser on
        self.teardown = False
        # makes window full screen
        super(Bot, self).__init__(service=Service(ChromeDriverManager().install()), options=options)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def open_page(self):
        print("Opening indeed")
        self.get("https://indeed.com")

    def search(self, ):
        print("Enter job type")
        job = input()
        print("Enter location")
        location = input()

        # finding input id for job and location input
        job_input = self.find_element(by=By.ID, value="text-input-what")
        location_input = self.find_element(by=By.ID, value="text-input-where")
        job_input.clear()
        # passing args as input
        job_input.send_keys(job)
        location_input.send_keys(location)
        job_input.send_keys(Keys.ENTER)
        self.get_jobs()

    def get_jobs(self):
        job_list = self.find_elements(by=By.CLASS_NAME, value="resultContent")

        if not job_list:
            print("No results found, Do you want to do another search?")
            res = input()
            if res.lower() == "yes":
                self.search()
            else:
                print("Thank you for using, have a nice day")
        else:
            job_table(job_list)
