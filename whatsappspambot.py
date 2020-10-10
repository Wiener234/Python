from selenium import webdriver
from time import sleep
import keyboard


f = open("beemove", "r")

#

driver = webdriver.Chrome(executable_path="I:\Download\chromedriver_win32\chromedriver.exe")

# executable_path="I:\Download\chromedriver_win32\chromedriver.exe"

driver.get("https://web.whatsapp.com/")
sleep(6)

#
# Replace what stand in '' white the name of the Chat
driver.find_element_by_css_selector("[title^='Selbsthilfegruppe']")\
    .click()

sleep(3)



for word in f:
    driver.find_element_by_class_name('_3uMse')\
        .send_keys(word)
    if keyboard.is_pressed("Esc"):
        break
