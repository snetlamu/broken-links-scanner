import datetime
import sys
import requests
from selenium import webdriver
from pyshadow.main import Shadow
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException

# function to check the status code of a URL


def check_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        # print(url + " - " + status_code)
        if status_code == 999:  # 999 is for linkedin blocks
            return True, status_code
        if status_code >= 200 and status_code < 400:
            return True, status_code
        else:
            return False, status_code
    except:
        return False, 0


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
shadow = Shadow(driver)
z = shadow.chrome_driver.get(
    sys.argv[1])
driver.implicitly_wait(10)
elements = shadow.find_elements("a")

print("Timestamp: ", datetime.datetime.now())

try:
    for e in elements:
        if e:
            if e.get_attribute("href") is not None:
                href = e.get_attribute("href").replace(" ", "")
                if href != "":
                    status, code = check_status(href)
                    print(href + " - " + str(code))
except StaleElementReferenceException:
    pass
