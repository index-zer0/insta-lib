import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller
if os.name == 'nt':
    import autoit
else:
    from pynput.keyboard import Key, Controller

def sleep(time_to_sleep):
    time.sleep(time_to_sleep)

def login(user, password):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", { "deviceName": "Galaxy S5" })
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com")
    passed = False
    while passed == False:
        passed = True
        try:
            driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()
            sleep(0.5)
        except:
            passed = False
            sleep(0.5)
    driver.find_element_by_xpath("//input[@name='username']").send_keys(user)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//input[@name='password']").submit()
    for i in range(2):
        passed = 5
        while passed > 0:
            try:
                driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
            except:
                passed-=1
                sleep(0.5)
            else:
                passed = 0
    passed = 5
    while passed > 0:
        try:
            driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
        except:
            passed-=1
            sleep(0.5)
        else:
            passed = 0
    return driver

def post(user, password, image, caption):
    if os.name != 'nt':
        keyboard = Controller()
    driver = login(user, password)
    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    passed = False
    while passed == False:
        passed = True
        try:
            if os.name == 'nt':
                autoit.win_active("Open")
                sleep(1)
                autoit.control_send("Open","Edit1",image)
                sleep(1)
                autoit.control_send("Open","Edit1","{ENTER}")
                sleep(0.5)
            else:
                keyboard.type(image)
                sleep(1)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                sleep(0.5)
        except:
            passed = False
            sleep(0.5) 
    passed = False
    while passed == False:
        passed = True
        try:
            driver.find_element_by_xpath("//button[@class='pHnkA']").click()
            sleep(0.5)
        except:
            passed = False
            sleep(0.5)
    passed = False
    while passed == False:
        passed = True
        try:
            driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
            sleep(0.5)
        except:
            passed = False
            sleep(0.5)
    passed = False
    while passed == False:
        passed = True
        try:
            write_a_caption = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
        except:
            passed = False
            sleep(0.5)
    sleep(0.5)
    write_a_caption.send_keys(caption)
    sleep(0.5)
    exit()
    driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
    sleep(10)
    driver.close()