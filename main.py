from pack_and_run import speech_and_say
from Hardware_PC import Hardware
import psutil
import os
import sys
import wmi
import screen_brightness_control as sbc
from pyfacebook import GraphAPI
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.chrome.options import Options


import js2py

# lay thong tin web khong can truy cap = js or selenium with js

# js = """
# function escramble_758(){
# var a,b,c
# a = 1
# b = 2
# c = 3
# return a + b + c
# }
# escramble_758()
# """.replace("document.write", "return ")

# result = js2py.eval_js(js)
# print(result)

test = Hardware();


# options = webdriver.ChromeOptions()
# options.add_argument(r"C:\Users\OOP\AppData\Local\Google\Chrome\User Data\Profile 2")
# driver = webdriver.Chrome(executable_path=r'./chromedriver.exe',chrome_options=options)
# driver.get("https://www.lambdatest.com/blog/selenium-with-python/




# lay frofile
# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\OOP\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
# driver.get("https://www.google.com")
# time.sleep(4)
# driver.maximize_window()


# driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div/div[3]/a[2]")
# to fire up a new tab using javascript and load google.com
# driver.execute_script('''window.open("https://www.google.com", "_blank");''') # tạo mới 1 tab
# driver.switch_to.window(driver.window_handles[0]) # chuyen tab
# titles = driver.title

# pyautogui.press('f6')
# pyautogui.hotkey('ctrl', 'c') # for copying the selected url
# import pyperclip # pip install pyperclip required
# url = pyperclip.paste()
# print(url)
# print(titles)

# driver.quit()

