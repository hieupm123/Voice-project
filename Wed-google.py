from general_web import *
# from pack_and_run import *
general = general_web()
output_check = general.lay_ten_nguoi_dung()

speech = speech_and_say();

def speech_catch_error():
    text_catch = 'Có gì đó không đúng bạn vui lòng xem lại yêu cầu của mình'
    speech.say_VN_by_Microsoft(text_catch)

class google:
  
    def init(self):
        try:
            options = webdriver.ChromeOptions()
            PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
            PATH1 = PATH[:9] + output_check + PATH[9:]
            options.add_argument("user-data-dir=" + PATH1)
            self.driver_web = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
            self.driver_web.get("https://www.google.com/")
            time.sleep(3)
        except:
            pass

    def home(self):
        self.driver_web.get('https://www.google.com/')
        time.sleep(2)

    def type_in_search(self,nhap = ''):
        try:
            search = self.driver_web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            search.send_keys(nhap)
            search.send_keys(Keys.RETURN)
            sleep(2)
        except:
            pass

    def select_link(self,a=1):
        try:
            chon = self.driver_web.find_elements_by_class_name("LC20lb")
            self.driver_web.implicitly_wait(10)
            ActionChains(self.driver_web).move_to_element(chon[a-1]).click(chon[a-1]).perform()
        except:
            pass