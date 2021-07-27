from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains


class google:
  
    def mo_trinh_duyet(self):
        try:
            global trinhduyet
            options = webdriver.ChromeOptions() 
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            trinhduyet = webdriver.Chrome(options=options, executable_path=r"C:\ProgramData\chromedriver_10\chromedriver.exe")
            trinhduyet.maximize_window() 
            trinhduyet.implicitly_wait(20)
            trinhduyet.get('https://www.google.com/')
            sleep(3)
        except:
            pass
    def open_new_window(self):
        try:
            pyautogui.hotkey('ctrl', 'n')
        except:
            pass
    def open_new_tab(self):
        try:
           pyautogui.hotkey('ctrl', 't')
        except:
            pass
    def reload(self):
        try:
           pyautogui.hotkey('f5')
        except:
            pass
    def on_off_full_screen(self):
        try:
         pyautogui.hotkey('f11')
        except:
            pass
    def size_content_big(self):
        try:
            pyautogui.hotkey('ctrl', '+')
        except:
            pass
    def size_content_small(self):
        try:
            pyautogui.hotkey('ctrl', '-')
        except:
            pass
    def size_content_normal(self):
        try:
          pyautogui.hotkey('ctrl', '0')
        except:
            pass
    def move_link_back(self):
        try:
           pyautogui.hotkey('alt', 'left')
        except:
            pass
    def move_link_up(self):
        try:
           pyautogui.hotkey('alt', 'right')
        except:
            pass
    def close_tab(self):
        try:
           pyautogui.hotkey('ctrl', 'w')
        except:
            pass
    def close_program(self):
        try:
           pyautogui.hotkey('alt', 'f4')   
        except:
            pass 
    def box_search(self,nhap = ''):
        try:
            search = trinhduyet.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            search.send_keys('abc')
            search.send_keys(Keys.RETURN)
            sleep(2)
        except:
            pass
    def move_down (self,a=''):
        try:
          trinhduyet.execute_script("window.scrollTo(0, window.scrollY + " + str(a) + " )")
        except:
            pass
    def move_up (self,a=''):
        try:
          trinhduyet.execute_script("window.scrollTo(0, window.scrollY + " - str(a) + " )")
        except:
            pass
    def select_link(self,a=''):
        try:
            chon = trinhduyet.find_elements_by_class_name("LC20lb")
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(chon[a-1]).click(chon[a-1]).perform()
        except:
            pass
    def back_search(self,nhap = ''):
        try:
            xoatimkiem = trinhduyet.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[3]/div[1]/span[1]')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(xoatimkiem).click(xoatimkiem).perform()
            sleep(1)
            timkiem = trinhduyet.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
            timkiem.send_keys(nhap) 
            timkiem.send_keys(Keys.RETURN)
            sleep(1)
        except:
            pass
        

    

        
    
    
    







