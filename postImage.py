import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#from pynput.keyboard import Key, Controller
#import autoit

def sleep(time_to_sleep):
    time.sleep(time_to_sleep)

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

def post(image, caption):
    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    passed = False
    while passed == False:
        passed = True
        try:
            autoit.win_active("Open")
            sleep(0.5)
        except:
            passed = False
            sleep(0.5) 
    passed = False
    while passed == False:
        passed = True
        try:
            autoit.control_send("Open","Edit1",image) 
            sleep(0.5)
        except:
            passed = False
            sleep(0.5) 
    passed = False
    while passed == False:
        passed = True
        try:
            autoit.control_send("Open","Edit1",image)
            sleep(1)
        autoit.control_send("Open","Edit1","{ENTER}")
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
    while passed == False:
        passed = True
        try:
            write_a_caption = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
            sleep(0.5)
            write_a_caption.send_keys(caption)
            sleep(0.5)
            share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
        except:
            passed = False
            sleep(0.5)
    

with open('auth.json') as json_file:
    data = json.load(json_file)
    user = data['user']
    password = data['password']

options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", { "deviceName": "Galaxy S5" })
#options.add_argument("headless")
driver = webdriver.Chrome(executable_path=r"./chromedriver",options=options)
driver.get("https://www.instagram.com")
login(user, password)
imagh = os.path.dirname(os.path.abspath(__file__)) + "\\cat.png"
caption = "picture of a #cat"
post(image, caption)
sleep(10)
driver.close()