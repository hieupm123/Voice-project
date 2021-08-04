from general_web import *

general = general_web()
output_check = general.lay_ten_nguoi_dung()

class Instagram(object):
    browser = None

    def open_ins(self):
        options = webdriver.ChromeOptions()
        PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
        PATH1 = PATH[:9] + output_check + PATH[9:]
        options.add_argument("user-data-dir=" + PATH1)
        self.browser = webdriver.Chrome(executable_path=r'.//chrome_driver/chromedriver.exe',chrome_options=options)
        self.browser.get("https://www.instagram.com/")

    def close(self):
        self.browser.close()

	# hello

    def login(self):
        self.us = self.browser.find_element_by_name("username")
        self.us.send_keys("0968522012")
        self.ps = self.browser.find_element_by_name("password")
        self.ps.send_keys("17122004")
        self.ps.send_keys(Keys.RETURN)
class operation_ins(Instagram):
    def search(self,nhap='cutra04'):
        try:
            self.timkiem = self.browser.find_elements_by_class_name("XTCLo x3qfX")
            self.timkiem.send_keys(nhap)
            self.timkiem.send_keys(Keys.RETURN)
        except:
            pass
# def
I = Instagram()
I.open_ins()
sleep(5)
I.login()
sleep(7)
B = operation_ins()
B.browser = I.browser
B.search()
sleep(5)

I.close()
