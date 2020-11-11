from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import dotenv


class driver:
    def __init__(self):
        path = os.getenv("exec_path")
        options = Options()
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(capabilities=cap, options=options, executable_path=path)

    def closeDriver(self):
        self.driver.close()

    def microsoftLogin(self, email, password):
        driver = self.driver
        driver.get("https://login.microsoftonline.com/")

        # input email address
        elem = driver.find_element_by_name("loginfmt")
        elem.send_keys(email)
        submitelem = driver.find_element_by_id("idSIButton9")
        submitelem.click()

        # input password
        try:
            elem = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "passwd"))
            )
        finally:
            elem.send_keys(password)
            elem.send_keys(Keys.ENTER)
            time.sleep(3)

    def getFormUrl(self):
        driver = self.driver

        driver.get("https://bphawks.schoology.com/course/2946961918/materials")

        # open "form"
        elem = driver.find_element_by_class_name("folder-title")
        elem = elem.find_element_by_tag_name("a")
        elem.click()

        # get embedded form
        elem = driver.find_element_by_tag_name("iframe")
        return elem.get_attribute("src")

    def googleLogin(self, email, password):
        driver = self.driver
        driver.get("https://accounts.google.com/ServiceLogin")

        # input email address
        elem = driver.find_element_by_name("identifier")
        elem.clear()
        elem.send_keys(email)
        elem.send_keys(Keys.ENTER)

        time.sleep(3)

        # input password
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys(password)
        elem.send_keys(Keys.ENTER)

        time.sleep(3)

    def submitForm(self, firstname, lastname, url):
        driver = self.driver

        driver.get(url)

        elem = driver.find_elements_by_tag_name("input")[2]
        elem.send_keys(firstname)

        elem = driver.find_elements_by_tag_name("input")[3]
        elem.send_keys(lastname)

        elem = driver.find_element_by_id("i9")
        elem.click()

        elem = driver.find_element_by_class_name(
            "freebirdFormviewerViewNavigationLeftButtons")
        elem = elem.find_element_by_tag_name("div")
        elem.click()

        time.sleep(3)
