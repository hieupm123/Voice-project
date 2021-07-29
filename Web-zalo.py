from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import js2py
import time
from random import seed
from random import randint
from general_web import *

general = general_web()
output_check = general.lay_ten_nguoi_dung()



class zalo(object):

    trinhduyet = None
    def mo_trinh_duyet(self):
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

    def dang_nhap(self,user = '',pas = ''):
        try:
            self.trinhduyet.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/ul/li[2]/a').click()
            login_user = self.trinhduyet.find_element_by_id('input-phone')
            login_user.send_keys(user)
            login_user = self.trinhduyet.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/input')
            login_user.send_keys(pas)
            login_user.send_keys(Keys.RETURN)
            time.sleep(randint(1,2))
            sleep(1)
        except:
            pass

class tin_nhan(zalo):

    def mo_tin_nhan(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[0]).click(phu_luc[0]).perform()
            sleep(1)
        except:
            pass

    def chon_nhan_tin(self,a=''):
        try:
            chon_nhan_tin = self.trinhduyet.find_elements_by_class_name('msg-item')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_nhan_tin[a-1]).click(chon_nhan_tin[a-1]).perform()
            sleep(1)
        except:
            pass
        
class tim_kiem_zalo(zalo):

    def them_ban_be(self):
        try:
            them_ban_be = self.trinhduyet.find_element_by_class_name('fa-outline-add-new-contact-2')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(them_ban_be).click(them_ban_be).perform()
            sleep(1)
        except:
            pass

    def tim_kiem(self, nhap=''):
        try:
            tim_kiem = self.trinhduyet.find_element_by_id('contact-search-input')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tim_kiem).click(tim_kiem).perform()    
            tim_kiem.send_keys(nhap)
            sleep(1)   
        except:
            pass

    def chon_tim_kiem_TATCA(self):
        try:
            chon_tim_kiem = self.trinhduyet.find_elements_by_class_name('tab-bar-item')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_tim_kiem[0]).click(chon_tim_kiem[0]).perform()    
            sleep(1)   
        except:
            pass
    def chon_tim_kiem_TINNHAN(self):
        try:
            chon_tim_kiem = self.trinhduyet.find_elements_by_class_name('tab-bar-item')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_tim_kiem[1]).click(chon_tim_kiem[1]).perform()    
            sleep(1)   
        except:
            pass
    def chon_tim_kiem_FILE(self):
        try:
            chon_tim_kiem = self.trinhduyet.find_elements_by_class_name('tab-bar-item')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_tim_kiem[2]).click(chon_tim_kiem[2]).perform()    
            sleep(1)   
        except:
            pass

    def chon_tin_nhan(self, a=''):
        try:
            chon_tin_nhan = self.trinhduyet.find_elements_by_class_name('zl-avatar__photo')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_tin_nhan[a+2]).click(chon_tin_nhan[a+2]).perform()    
            sleep(1)   
        except:
            pass

class danh_ba(zalo):

    def mo_danh_ba(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[1]).click(phu_luc[1]).perform()
            sleep(1)
        except:
            pass

    def danh_sach_ket_ban(self):
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

    def ban_be(self,a=''):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('zl-avatar__photo')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[a+3]).click(danh_sach[a+3]).perform()
            sleep(1)
        except:
            pass

class thong_bao(zalo):

    def mo_thong_bao(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[2]).click(phu_luc[2]).perform()
            sleep(1)
        except:
            pass

    def thong_bao_uu_tien(self):
        try:
            cac_muc = self.trinhduyet.find_elements_by_class_name('noti-tab-btn')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc[0]).click(cac_muc[0]).perform()
            sleep(1)
        except:
            pass

    def thong_bao_khac(self):
        try:
            cac_muc = self.trinhduyet.find_elements_by_class_name('noti-tab-btn')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc[1]).click(cac_muc[1]).perform()
            sleep(1)
        except:
            pass

    def thong_bao_tat_ca(self):
        try:
            thongbaomuiten = self.trinhduyet.find_element_by_class_name('fa-caret-down ')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(thongbaomuiten).click(thongbaomuiten).perform()
            cac_muc = self.trinhduyet.find_element_by_xpath('/html/body/div[2]/div/div[1]/span[2]')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc).click(cac_muc).perform()
            sleep(1)
        except:
            pass

    def thong_bao_chua_doc(self):
        try:
            thongbaomuiten = self.trinhduyet.find_element_by_class_name('fa-caret-down ')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(thongbaomuiten).click(thongbaomuiten).perform()
            cac_muc = self.trinhduyet.find_element_by_xpath('/html/body/div[2]/div/div[6]/span[2]')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cac_muc).click(cac_muc).perform()
            sleep(1)
        except:
            pass
    
    def chon_thong_bao(self,a=''):
        try:
            chon_thong_bao = self.trinhduyet.find_elements_by_class_name('zl-avatar__alphabet')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_thong_bao[a+1]).click(chon_thong_bao[a+1]).perform()
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

    def chon_to_do(self,a=''):
        try:
            chon_to_do = self.trinhduyet.find_elements_by_class_name('td-gray-txt-v3')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_to_do[a-1]).click(chon_to_do[a-1]).perform()
            sleep(1)
        except:
            pass

class tin_danh_giau(zalo):
    def mo_tin_danh_giau(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[5]).click(phu_luc[5]).perform()
            sleep(1)
        except:
            pass

    def chon_tin_danh_giau(self,a=''):
        try:
            chon_tin_danh_giau = self.trinhduyet.find_elements_by_class_name('text-name')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_tin_danh_giau[a-1]).click(chon_tin_danh_giau[a-1]).perform()
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

    def cai_dat_chung(self):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('setting-menu__icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[0]).click(danh_sach[0]).perform()
            sleep(1)
        except:
            pass

    def cai_dat_giao_dien(self):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('setting-menu__icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[1]).click(danh_sach[1]).perform()
            sleep(1)
        except:
            pass

    def cai_dat_thong_bao(self):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('setting-menu__icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[2]).click(danh_sach[2]).perform()
            sleep(1)
        except:
            pass

    def cai_dat_tin_nhan(self):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('setting-menu__icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[3]).click(danh_sach[3]).perform()
            sleep(1)
        except:
            pass

    def cai_dat_tien_ich(self):
        try:
            danh_sach = self.trinhduyet.find_elements_by_class_name('setting-menu__icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(danh_sach[4]).click(danh_sach[4]).perform()
            sleep(1)
        except:
            pass
        
    def tat_cai_dat(self):
        try:
            tat_cai_dat = self.trinhduyet.find_element_by_class_name('fa-close')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tat_cai_dat).click(tat_cai_dat).perform()
            sleep(1)
        except:
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
    
    def chinh_sua_ten(self):
        try:
            chinh_sua_ten = self.trinhduyet.find_element_by_class_name('fa-edit-name')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chinh_sua_ten).click(chinh_sua_ten).perform()
            sleep(1)
        except:
            pass
    def chinh_anh(self):
        try:
            chinh_anh = self.trinhduyet.find_element_by_xpath('//*[@id="zl-modal__dialog-body"]/div/div/div/div[1]/img[2]')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chinh_anh).click(chinh_anh).perform()
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

class dang_xuat(zalo):

    def dang_xuat(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('internal-icon')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[6]).click(phu_luc[6]).perform()
            sleep(1)
            seting = self.trinhduyet.find_element_by_xpath('/html/body/div[2]/div/div[8]/div[2]/span')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(seting).click(seting).perform()
            sleep(1)
            out = self.trinhduyet.find_element_by_xpath('//*[@id="popup-dialog"]/div[3]/div[2]/div/div[2]/div')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(out).click(out).perform()
            sleep(1)
        except:
            pass


    



    