# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.support.select import Select

WINDOW_SIZE = "1920,1080"


chrome_options = Options()

# chrome_options.add_argument("--headless")
# https://peter.sh/experiments/chromium-command-line-switches/#user-agent
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument("--user-agent=%s" % "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 MicroMessenger")

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 MicroMessenger"


def second_click():
    browser = webdriver.Chrome(executable_path=r'C:\Users\tsj\chromedriver.exe', options=chrome_options)
    #browser = webdriver.PhantomJS(executable_path=r'C:\Users\tsj\phantomjs\bin\phantomjs.exe', desired_capabilities=dcap)
    browser.set_window_size(1920, 1080)
    browser.get("file:///C:/Users/tsj/Desktop/michelin/index.html")
    while True:
        click_button = browser.find_element_by_xpath("/html/body/button")
        print("Wait for button can be clickable.")
        WebDriverWait(driver=browser, timeout=3000, poll_frequency=0.005, ignored_exceptions=None).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/button')))
        click_button.click()
        time.sleep(7)
        break


if __name__ == '__main__':
    second_click()
