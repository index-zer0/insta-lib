from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#from pynput.keyboard import Key, Controller
#import autoit

def login(user, password):
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

with open('auth.json') as json_file:
    data = json.load(json_file)
    user = data['user']
    password = data['password']

mobile_emulation = { "deviceName": "Galaxy S5" }
opts = webdriver.ChromeOptions()
opts.add_experimental_option("mobileEmulation", mobile_emulation)
#opts.add_argument("headless")
driver = webdriver.Chrome(executable_path=r"./chromedriver",options=opts)
driver.get("https://www.instagram.com")
login(user, password)

