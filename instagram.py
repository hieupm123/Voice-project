from general_web import *

general = general_web()
output_check = general.lay_ten_nguoi_dung()

class Instagram(object):
    browser = None

    def init(self):
        options =   webdriver.ChromeOptions()
        PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
        PATH1 = PATH[:9] + output_check + PATH[9:]
        options.add_argument("user-data-dir=" + PATH1)
        self.browser = webdriver.Chrome(executable_path=r'.//chrome_driver/chromedriver.exe',chrome_options=options)
        self.browser.get("https://www.instagram.com/")
        time.sleep(randint(1,2));

    def login(self):
        try:
            self.us = self.browser.find_element_by_name("username")
            self.us.send_keys("0968522012")
            self.ps = self.browser.find_element_by_name("password")
            self.ps.send_keys("17122004")
            self.ps.send_keys(Keys.RETURN)
            time.sleep(randint(1,2))
        except:
            pass

    def home(self):
        try:
            self.browser.get('https://www.instagram.com/')
            time.sleep(randint(1,2))
        except:
            pass

class operation_ins(Instagram):
    def type_in_search(self,nhap='cutra04'):
        try:
            timkiem = None;
            try:
                timkiem = self.browser.find_element_by_xpath('//input[@placeholder="Tìm kiếm"]')
            except:
                timkiem = self.browser.find_element_by_xpath('//input[@placeholder="Search"]')
            timkiem.send_keys(nhap)
            timkiem.send_keys(Keys.RETURN)
            time.sleep(randint(1,2))
        except:
            pass

    def chon_nguoi_muon_tim(self, id = 0):
        try:
            use = self.browser.find_elements_by_class_name('-qQT3')
            self.browser.execute_script("arguments[0].click();",use[id]);
            time.sleep(randint(1,2))
        except:
            pass

    def turn_compass(self):
        try:
            self.browser.get('https://www.instagram.com/explore/');
            time.sleep(randint(1,2))
        except:
            pass

    def message(self):
        try:
            self.browser.get('https://www.instagram.com/direct/inbox/')
            time.sleep(randint(1,2))
        except:
            pass
class story_ins(Instagram):
    def chon_video(self, id = 0):
        try:
            use = self.browser.find_elements_by_class_name('_6q-tv')
            self.browser.execute_script("arguments[0].click();",use[id]);
            time.sleep(randint(1,2))
        except:
            pass

class story_ins_in(Instagram):
    def next_video(self):
        try:
            use = self.browser.find_element_by_class_name('coreSpriteRightChevron')
            self.browser.execute_script("arguments[0].click();",use);
            time.sleep(randint(1,2)) 
        except:
            pass

    def comment(self, text = 'Thử comment tý thôi!'):
        try:
            use = self.browser.find_element_by_class_name('Xuckn');
            use.send_keys(text);
            time.sleep(randint(1,2))
            use.send_keys(Keys.RETURN)
            time.sleep(randint(1,2))
        except:
            pass
class status_ins(Instagram):
    def find_index(self):
        click1 = 0; click2 = 0; click3 = 0; click4 = 0;
        for i in range(1,350):
            try:
                click1_use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[' + str(i) + ']/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div')
                click1 = general.kiem_tra_trong_view(drivers = '')
            except:
                pass

            try:
                click2_use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[' + str(i)+ ']/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]/div/div')
                click2 = general.kiem_tra_trong_view(drivers = '')
            except:
                pass

            try:
                click3_use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[' + str(i) + ']/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div')
                click3 = general.kiem_tra_trong_view(drivers = '')
            except:
                pass

            try:
                click4_use = self.driver_web.find_elements_by_xpath('//div[@aria-label="Thích"]')
                click4 = general.kiem_tra_trong_view(drivers = '')
            except:
                pass

            if(click1 or click2 or click3 or click4):
                return i
        return -10;        

