from pack_and_run import speech_and_say
from Hardware_PC import Hardware
import psutil
import os
import sys
import wmi
import screen_brightness_control as sbc
from pyfacebook import GraphAPI
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains 


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

# test = Hardware();


# options = webdriver.ChromeOptions()
# options.add_argument(r"C:\Users\OOP\AppData\Local\Google\Chrome\User Data\Profile 2")
# driver = webdriver.Chrome(executable_path=r'./chromedriver.exe',chrome_options=options)
# driver.get("https://www.lambdatest.com/blog/selenium-with-python/




# lay frofile
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\OOP\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
driver = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe', chrome_options=options)
driver.get("https://www.facebook.com/")
time.sleep(3)
# lg = driver.find_element_by_id('search')

# driver.execute_script('''window.open("https://www.google.com", "_blank");''') # tạo mới 1 tab
# print(userName.text)
# print(driver.execute_script('return arguments[0]',userName))
# time.sleep(5)


# use = driver.find_elements_by_class_name("_d61")
# print(len(use))

# tim
# --------------------------------------

# time.sleep(2)


def element_in_viewport(drivers, elem):
    elem_left_bound = elem.location.get('x')
    elem_top_bound = elem.location.get('y')
    elem_width = elem.size.get('width')
    elem_height = elem.size.get('height')
    elem_right_bound = elem_left_bound + elem_width
    elem_lower_bound = elem_top_bound + elem_height

    win_upper_bound = drivers.execute_script('return window.pageYOffset')
    win_left_bound = drivers.execute_script('return window.pageXOffset')
    win_width = drivers.execute_script('return document.documentElement.clientWidth')
    win_height = drivers.execute_script('return document.documentElement.clientHeight')
    win_right_bound = win_left_bound + win_width
    win_lower_bound = win_upper_bound + win_height

    return all((win_left_bound <= elem_left_bound,
                win_right_bound >= elem_right_bound,
                win_upper_bound <= elem_top_bound,
                win_lower_bound >= elem_lower_bound)
               )



use = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]')
print(use.get_attribute("aria-label"))
# driver.execute_script("arguments[0].click();",nhan)



# ---------------------------------------




# ok texxt--------------------------
# element_to_hover_over = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div/div[1]/div/span[1]/div/div/span/div[1]")
# time.sleep(2)
# hover = ActionChains(driver).move_to_element(element_to_hover_over)
# time.sleep(2)
# hover.perform()
# time.sleep(1)
# use = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/span[2]')
# time.sleep(2)
# driver.execute_script("arguments[0].click();",use)
# ---------------------------------

# use = driver.find_elements_by_class_name('k4urcfbm')
# for i in use:
# 	print(i)
# check in viewpoint


# while(1):
# 	use = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[5]')
# 	print(element_in_viewport(driver,use))
# 	time.sleep(1)

# # use.click()
# # print(use)
# # print(len(use))
# driver.execute_script("arguments[0].click();",use)

# time.sleep(3)

# use = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div[3]/div[2]/form/div/div/div[1]/p")

# time.sleep(3)

# use.send_keys('Nhìn ok quá nhỉ ?')
# use.send_keys(Keys.RETURN)

# while(1):
# 	print(driver.execute_script('return document.documentElement.scrollTop;'))
# 	time.sleep(1)
	

# print(driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a").text)


time.sleep(2)
driver.quit()

exit()
# lg.send_keys('Hieu')
# lg.send_keys(Keys.RETURN)
# driver.maximize_window()


# driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div/div[3]/a[2]")
# to fire up a new tab using javascript and load google.com
# driver.switch_to.window(driver.window_handles[0]) # chuyen tab
# titles = driver.title

# pyautogui.press('f6')
# pyautogui.hotkey('ctrl', 'c') # for copying the selected url
# import pyperclip # pip install pyperclip required
# url = pyperclip.paste()
# print(url)
# print(titles)

# driver.quit()


