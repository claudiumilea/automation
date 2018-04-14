from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
import datetime
from random import randint
import base64
import selenium.webdriver.support.ui as ui




driver = webdriver.Chrome("chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.youtube.com")

driver.maximize_window()
driver.implicitly_wait(20)
screenshot_path = "E:\\toolz\\selenium\\youtube"
wait = ui.WebDriverWait(driver,20)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True

def check_exists_by_xpath_wait(xpath):
    try:
        wait.until(lambda driver: ec.element_to_be_clickable((By.XPATH,xpath)))
    except NoSuchElementException:
        return False

    return True

def get_screenshot(screenshot_path):
    driver.get_screenshot_as_file(screenshot_path + time.strftime(" %d %m %Y %H %M %S") + ".png")

def click_on_youtube():
    driver.find_element(By.XPATH, '//*[@id="logo-icon-container"]').click()
    get_screenshot(screenshot_path)



try:
    if check_exists_by_xpath('//*[@id="text"]'):
        driver.find_elements(By.XPATH,'//*[@id="text"]')[2].click()
        time.sleep(2)
        get_screenshot(screenshot_path)

    if check_exists_by_xpath('//*[@id="yt-masthead-signin"]/div/button/span'):
        element = driver.find_element(By.XPATH,'//*[@id="yt-masthead-signin"]/div/button/span')
        element.click()
        time.sleep(2)
        get_screenshot(screenshot_path)

    if check_exists_by_xpath('//*[@id="identifierLink"]/div[2]'):
        driver.find_element(By.XPATH,'//*[@id="identifierLink"]/div[2]').click()
        time.sleep(2)
        get_screenshot(screenshot_path)
        

    if check_exists_by_xpath('//*[@id="headingSubtext"]'):
        driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys('claudius.milea')
        driver.find_element(By.XPATH,'//*[@id="identifierNext"]/content').click()
        time.sleep(2)
        get_screenshot(screenshot_path)
        

    if check_exists_by_xpath('//*[@id="forgotPassword"]/content/span'):
        driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(base64.b64decode('QG01NzNyZEBt').decode())
        driver.find_element(By.XPATH,'//*[@id="passwordNext"]/content/span').click()
        time.sleep(2)
        get_screenshot(screenshot_path)
        

    if check_exists_by_xpath('//*[@id="appbar-nav"]/ul/li[2]/a/span'):
        driver.find_element(By.XPATH,'//*[@id="appbar-nav"]/ul/li[2]/a/span').click()
        time.sleep(2)
        get_screenshot(screenshot_path)
    
    
    
    for i in range(1, 100):
    
        element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="video-title"]')))
        
        #click pe video din lista aleatoriu
        if check_exists_by_xpath_wait('//*[@id="video-title"]'):
            driver.find_elements(By.XPATH,'//*[@id="video-title"]')[randint(0,4)].click()
            time.sleep(2)
            get_screenshot(screenshot_path)

        click_on_youtube()
        time.sleep(randint(1,14))

finally:
    driver.quit()