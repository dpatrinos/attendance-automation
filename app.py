import dotenv
import os
from webdriver import driver
import time
import schedule

dotenv.load_dotenv()

email = os.getenv("email")
password = os.getenv("password")
firstname = os.getenv("first")
lastname = os.getenv("last")

main_driver = driver()

def takeAttendance():
    main_driver.microsoftLogin(email, password)
    url = main_driver.getFormUrl()
    print(url)

    main_driver.googleLogin(email, password)

    main_driver.submitForm(firstname, lastname, url)


if(__name__ == "__main__"):
    schedule.every().monday.at("07:30").do(takeAttendance)
    schedule.every().tuesday.at("07:30").do(takeAttendance)
    schedule.every().wednesday.at("07:30").do(takeAttendance)
    schedule.every().thursday.at("07:30").do(takeAttendance)
    schedule.every().friday.at("07:30").do(takeAttendance)
    while True:
        schedule.run_pending()
        time.sleep(1)

    main_driver.closeDriver()

    


