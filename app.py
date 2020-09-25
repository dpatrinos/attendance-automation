import dotenv
import os
from webdriver import driver

dotenv.load_dotenv()

email = os.getenv("email")
password = os.getenv("password")
firstname = os.getenv("first")
lastname = os.getenv("last")

main_driver = driver()

main_driver.microsoftLogin(email, password)
url = main_driver.getFormUrl()
print(url)

main_driver.googleLogin(email, password)

main_driver.submitForm(firstname, lastname, url)

main_driver.closeDriver()
