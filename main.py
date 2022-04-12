from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
chrome_webdriver = "../chromedriver.exe"

browser = webdriver.Chrome(executable_path=chrome_webdriver)
browser.get(url="https://tinder.com/")
wait = WebDriverWait(browser, timeout=30)
browser.maximize_window()
main_page = browser.current_window_handle
# log in button
time.sleep(3)
login = browser.find_element(by=By.CLASS_NAME, value="button")
login.click()



try:
    time.sleep(3)
    facebook = browser.find_element(by=By.XPATH, value='//*[@id="u-1597322998"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook.click()
except:
    time.sleep(3)
    more_option = browser.find_element(by=By.XPATH, value='//*[@id="u-1597322998"]/div/div/div[1]/div/div[3]/span/button')
    more_option.click()

    time.sleep(3)
    facebook = browser.find_element(by=By.XPATH, value='//*[@id="u-1597322998"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook.click()

for handle in browser.window_handles:
    if handle != main_page:
        facebook_page = handle
        browser.switch_to.window(facebook_page)

time.sleep(3)
username = browser.find_element(by=By.XPATH, value='//*[@id="email"]')
username.send_keys("satyabhusanprusty@yahoo.com")

password = browser.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password.send_keys("satya9853")

login = browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]")
login.click()

time.sleep(7)
browser.switch_to.window(main_page)
location = browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div/div[3]/button[1]')
location.click()

cookies = browser.find_element(by=By.XPATH, value='//*[@id="u131058078"]/div/div[2]/div/div/div[1]/div[2]/button')
cookies.click()

try:
    not_interested = browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div/div[3]/button[2]')
    not_interested.click()
except:
    pass
while True:
    browser.implicitly_wait(30)
    try:
        cancel = browser.find_element(by=By.XPATH, value='//*[@id="u131058078"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button/span/span')
        cancel.click()
    except NoSuchElementException:
        time.sleep(10)
        print(1)
