from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from queue import Queue
from random import seed
from random import randint


output_check = ''
file_check_chrome = open('check_chrome_version.txt','r+');
output_check = file_check_chrome.read()
if(output_check == ''):
	driver = webdriver.Chrome('./chromedriver.exe')
	driver.get('chrome://version/')
	profile_path = driver.find_element_by_id('profile_path').text
	def cleanup_str_profile_path():
		ans = ''
		str(profile_path)
		for i in range (9,len(profile_path),1):
			if(profile_path[i] != '\\'):
				ans += profile_path[i]
			else:
				break
		return ans

	file_check_chrome.write(cleanup_str_profile_path())
	driver.close()
	output_check = cleanup_str_profile_path() 
file_check_chrome.close()
# để lấy tên người dùng phục vụ chức năng lưu cookie sau này

class Web_chat:
	pass



class facebook: 

	driver_web = None
	queue_running_process = Queue()

	def __init__(self):
		options = webdriver.ChromeOptions()
		PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
		PATH1 = PATH[:9] + output_check + PATH[9:]
		options.add_argument("user-data-dir=" + PATH1)
		driver = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
		driver.get("https://www.facebook.com/")
		self.driver_web = driver
		# self.running_and_control_facebook()


	def running_and_control_facebook(self):
		while(1):
			if(self.queue_running_process.empty() == 0):
				func = self.queue_running_process.get()
				self.locals()[func]()

			time.sleep(1)

	def login(self,user = '',pas = ''):
		login_user = self.driver_web.find_element_by_id('email')
		login_user.send_keys(user)
		login_user = self.driver_web.find_element_by_id('pass')
		login_user.send_keys(pas)
		login_user.send_keys(Keys.RETURN)


	def search_in_facebook(self,name = ''): # lưu ý driver là biến, func là tên hàm
		search_button = self.driver_web.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input")
		print(search_button)
		time.sleep(randint(0, 10))
		# for option in search_button:
			# print("Value is: %s" % option.get_attribute("value"))
			# option.click()



class messenger:
	pass

I = facebook()
I.search_in_facebook()
