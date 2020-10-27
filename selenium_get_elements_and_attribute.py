# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.select import Select

WINDOW_SIZE = "1920,1080"


chrome_options = Options()

chrome_options.add_argument("--headless")
# https://peter.sh/experiments/chromium-command-line-switches/#user-agent
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument("--user-agent=%s" % "MicroMessenger")

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = "MicroMessenger"


def get_info():
    #browser = webdriver.Chrome(executable_path=r'C:\Users\tsj\chromedriver.exe', options=chrome_options)
    browser = webdriver.PhantomJS(executable_path=r'C:\Users\tsj\phantomjs\bin\phantomjs.exe', desired_capabilities=dcap)
    browser.set_window_size(1920, 1080)
    browser.get("target_url")

    browser.get_screenshot_as_file(r'C:\Users\tsj\selenium_screenshot_before.png')
    WebDriverWait(driver=browser, timeout=120, poll_frequency=0.5, ignored_exceptions=None).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/a/img')))
    # # div1 = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]").get_attribute("outerHTML")

    browser.get_screenshot_as_file(r'C:\Users\tsj\selenium_screenshot_after.png')
    div1 = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div[1]/*")
    banner_dict = {}
    for i in div1:
        # print(i.get_attribute("data-swiper-slide-index"))
        # i.find_element_by_xpath("./a").get_attribute("data-name"))
        banner_dict[i.get_attribute("data-swiper-slide-index")] = i.find_element_by_xpath("./a").get_attribute("data-name").encode("utf-8").decode("utf-8")
    sorted_banner_dict = sorted(banner_dict.items(), key=lambda x: x[0], reverse=False)
    return sorted_banner_dict


if __name__ == '__main__':
    get_info()
