from general_web import *

general = general_web()
output_check = general.lay_ten_nguoi_dung()

class zalo(object):

    trinhduyet = None
    def init(self):
        try:
            options = webdriver.ChromeOptions() 
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
            PATH1 = PATH[:9] + output_check + PATH[9:]
            options.add_argument("user-data-dir=" + PATH1)
            self.trinhduyet = webdriver.Chrome(executable_path=r'D:\Laptrinh\test\chromedriver\chromedriver.exe',chrome_options=options)
            self.trinhduyet.maximize_window() 
            self.trinhduyet.implicitly_wait(20)
            self.trinhduyet.get('https://id.zalo.me/')
            sleep(3)
        except:
            pass

class tin_nhan_zalo(zalo):

    def mo_tin_nhan(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[0]).click(phu_luc[0]).perform()
            sleep(1)
        except:
            return;

    def search_by_index(self,a=1):
        try:
            self.mo_tin_nhan()
            chon_nhan_tin = self.trinhduyet.find_elements_by_class_name('msg-item')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_nhan_tin[a-1]).click(chon_nhan_tin[a-1]).perform()
            sleep(1)
        except:
            pass
        
class tim_kiem_zalo(zalo):

    def type_in_search(self, nhap=''):
        try:
            tim_kiem = self.trinhduyet.find_element_by_id('contact-search-input')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tim_kiem).click(tim_kiem).perform()    
            tim_kiem.send_keys(nhap)
            sleep(1)   
        except:
            pass

    # a là một số hãy giải quyết số đó 
    def chon_nguoi_muon_tim(self, a=1):
        try:
            chon_tin_nhan = self.trinhduyet.find_elements_by_class_name('zl-avatar__photo')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_tin_nhan[a+2]).click(chon_tin_nhan[a+2]).perform()    
            sleep(1)   
        except:
            pass

class danh_ba_zalo(zalo):

    def home_friend(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[1]).click(phu_luc[1]).perform()
            sleep(1)
        except:
            pass

    def list_friend(self):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('fr-conv-item-avatar')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[0]).click(danh_sach[0]).perform()
            sleep(1)
        except:
            pass
    def danh_sach_nhom(self):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('fr-conv-item-avatar')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[1]).click(danh_sach[1]).perform()
            sleep(1)
        except:
            pass
        
    def truyen_file(self):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('zl-avatar__photo')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[3]).click(danh_sach[3]).perform()
            sleep(1)
        except:
            pass

class to_do(zalo):

    def mo_to_do(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[3]).click(phu_luc[3]).perform()
            sleep(1)
        except:
            pass

    def to_do_toi_giao(self):
        try:
            cac_muc = self.trinhduyet.find_elements_by_class_name('td-tab')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc[0]).click(cac_muc[0]).perform()
            sleep(1)
        except:
            pass

    def to_do_can_lam(self):
        try:
            cac_muc = self.trinhduyet.find_elements_by_class_name('td-tab')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc[1]).click(cac_muc[1]).perform()
            sleep(1)
        except:
            pass

    def to_do_theo_gioi(self):
        try:
            cac_muc = self.trinhduyet.find_elements_by_class_name('td-tab')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc[2]).click(cac_muc[2]).perform()
            sleep(1)
        except:
            pass
 
    def to_do_chua_xong(self):
        try:
            cac_muc = self.trinhduyet.find_elements_by_class_name('td-sub-tab')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc[0]).click(cac_muc[0]).perform()
            sleep(1)
        except:
            pass

    def to_do_da_xong(self):
        try:
            cac_muc = self.trinhduyet.find_elements_by_class_name('td-sub-tab')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc[1]).click(cac_muc[1]).perform()
            sleep(1)
        except:
            pass

    def chon_to_do(self,a=1):
        try:
            chon_to_do = self.trinhduyet.find_elements_by_class_name('td-gray-txt-v3')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_to_do[a-1]).click(chon_to_do[a-1]).perform()
            sleep(1)
        except:
            pass

class cai_dat(zalo):

    def mo_cai_dat(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[6]).click(phu_luc[6]).perform()
            sleep(1)
            seting = self.trinhduyet.find_elements_by_class_name('fa-outline-settings')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(seting[1]).click(seting[1]).perform()
            sleep(1)
        except:
            pass

    def dong_cai_dat(self):
        pass

class tai_khoan(zalo):

    def mo_tai_khoan(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[6]).click(phu_luc[6]).perform()
            sleep(1)
            seting = self.trinhduyet.find_elements_by_class_name('fa-outline-contact')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(seting[1]).click(seting[1]).perform()
            sleep(1)
        except:
            pass

    def tat_tai_khoan(self):
        try:
            tat_tai_khoan = self.trinhduyet.find_element_by_class_name('fa-close')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tat_tai_khoan).click(tat_tai_khoan).perform()
            sleep(1)
        except:
            pass



=======> cái này vào 1 class tên tùy ý
--> kiếm tra tin nhắn mới lấy cái số rồi xử lí chuỗi nháy cái rồi đọc kết quả cho người dùng
-==> tên hàm check_tin_nhan(self) trả một đoạn text thông  báo
--> viết hàm kiếm tra thông báo mới lấy cái số rồi xử lí chuỗi nháy cái rồi đọc kết quả cho người dùng
-==> check_thong_bao(self) trả một đoạn text thông  báo
--> hàm kiếm tra người nhắn tin gần nhất
-==> lay_ten_nguoi_gan_nhat(self) trả một đoạn text thông báo
=======> cái này vào 1 class tên tùy ý
--> Thiếu phần nhắn với người kia
-==> chat(self,text = '')
--> Thiếu gọi với người kia
-==> call_nor(self)
--> Thiếu phần thả like cho người kia
-==> click_like(self)
--> gọi video với người kia
-==> call_vid(self)
========> trong class cai_dat luôn
--> 1 hàm đóng cài đặt
-==> dong_cai_dat(self)