from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains



class open_youtube:
    def mo_trinh_duyet(self):
        try:
            global trinhduyet
            options = webdriver.ChromeOptions() 
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            trinhduyet = webdriver.Chrome(options=options, executable_path=r"C:\ProgramData\chromedriver_10\chromedriver.exe")
            trinhduyet.maximize_window() 
            trinhduyet.implicitly_wait(20)
            trinhduyet.get('https://www.youtube.com/')
        except:
            pass  

def scroll_down(self,a=''):
    try:
        trinhduyet.execute_script("window.scrollTo(0, window.scrollY + " + str(a) + " )")
    except:
        pass

def scroll_up(self,a=''):
    try:
        trinhduyet.execute_script("window.scrollTo(0, window.scrollY + " - str(a) + " )")
    except:
            pass

#Thao tác phụ lục bên phải youtube---------------------------------------------------------------------------------------------------------------------------------


def trang_chu(self):
    try:
        phu_luc = trinhduyet.find_elements_by_class_name('title')
        trinhduyet.implicitly_wait(10)
        ActionChains(trinhduyet).move_to_element(phu_luc[0]).click(phu_luc[0]).perform()
    except:
            pass

def kham_pha(self):
    try:
        phu_luc = trinhduyet.find_elements_by_class_name('title')
        trinhduyet.implicitly_wait(10)
        ActionChains(trinhduyet).move_to_element(phu_luc[1]).click(phu_luc[1]).perform()
    except:
            pass

def kenh_dang_ky(self):
    try:
        phu_luc = trinhduyet.find_elements_by_class_name('title')
        trinhduyet.implicitly_wait(10)
        ActionChains(trinhduyet).move_to_element(phu_luc[2]).click(phu_luc[2]).perform()
    except:
            pass

def thu_vien(self):
    try:
        phu_luc = trinhduyet.find_elements_by_class_name('title')
        trinhduyet.implicitly_wait(10)
        ActionChains(trinhduyet).move_to_element(phu_luc[3]).click(phu_luc[3]).perform()
    except:
            pass
    
#Chọn video trên trang chủ---------------------------------------------------------------------------------------------------------------------------


def chon_video_o_trang_chu(self,a=''):
    try:
        chon_video_o_trang_chu = trinhduyet.find_elements_by_id('content')
        trinhduyet.implicitly_wait(10)
        ActionChains(trinhduyet).move_to_element(chon_video_o_trang_chu[a]).click(chon_video_o_trang_chu[a]).perform()
    except:
            pass

#Chọn vidoe trên khám phá---------------------------------------------------------------------------------------------------------------------------------
class vidoe_kham_pha:
    def trending(self):
        try:
            trending = trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(trending[1]).click(trending[1]).perform()
        except:
            pass

    def music(self):
        try:
            music = trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(music[2]).click(music[2]).perform()
        except:
            pass

    def gaming(self):
        try:
            gaming = trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(gaming[3]).click(gaming[3]).perform()
        except:
            pass

    def news(self):
        try:
            news = trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(news[4]).click(news[4]).perform()
        except:
            pass
        
    def sports(self):
        try:
            sports = trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(sports[5]).click(sports[5]).perform()
        except:
            pass

    def chon_video_o_kham_pha(self,a=''):
        try:
            chon = trinhduyet.find_elements_by_class_name('ytd-expanded-shelf-contents-renderer')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(chon[a]).click(chon[a]).perform()
        except:
            pass 


#Thao tác trên tìm kiếm-------------------------------------------------------------------------------------------------------------------------

class search_youtube:


    def search(self,nhap=''):
        try:
            nhan = trinhduyet.find_element_by_xpath('//*[@id="search"]')
            nhan.send_keys(nhap)
            nhan.send_keys(Keys.RETURN)
        except:
            pass

    def chon_video_tim_kiem(self,a=''):
        try:
            chon = trinhduyet.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(chon[a-1]).click(chon[a-1]).perform()
        except:
            pass

    def quay_lai_tim_kiem(self,nhap=''):
        try:
            tim_kiem_lai =  trinhduyet.find_element_by_id('search')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(tim_kiem_lai).click(tim_kiem_lai).perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('backspace')
            sleep(1)
            tim_kiem_lai.send_keys(nhap)
            tim_kiem_lai.send_keys(Keys.RETURN)
        except:
            pass

    def next_video_khi_xem_video(self,b=''):
        try:
            next_video = trinhduyet.find_elements_by_class_name('style-scope ytd-compact-video-renderer')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(next_video[b-1]).click(next_video[b-1]).perform()
        except:
            pass

    def truy_cap_kenh(self):
        try:
            truy_cap_kenh = trinhduyet.find_element_by_xpath('//*[@id="top-row"]/ytd-video-owner-renderer/a')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(truy_cap_kenh).click(truy_cap_kenh).perform()
        except:
            pass

    def phong_to_nho(self):
        try:
            pause_phong_to_nho = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_phong_to_nho).perform()
            sleep(1)
            phong_to_nho = trinhduyet.find_element_by_class_name('ytp-fullscreen-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(phong_to_nho).click(phong_to_nho).perform()
        except:
            pass

    def bat_tat_phat_tren_TV(self):
        try:
            pause_phat_tren_TV = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_phat_tren_TV).perform()
            sleep(1)
            phat_tren_TV = trinhduyet.find_element_by_class_name('ytp-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(phat_tren_TV).click(phat_tren_TV).perform()
        except:
            pass

    def bat_tat_che_do_rap_chieu_phim(self):
        try:
            pause_che_do_rap_chieu_phim = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_che_do_rap_chieu_phim).perform()
            sleep(1)
            che_do_rap_chieu_phim = trinhduyet.find_element_by_class_name('ytp-size-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(che_do_rap_chieu_phim).click(che_do_rap_chieu_phim).perform()
        except:
            pass


    def bat_trinh_phat_thu_nho(self):
        try:
            pause_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_trinh_phat_thu_nho).perform()
            sleep(1)
            bat_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-miniplayer-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(bat_trinh_phat_thu_nho).click(bat_trinh_phat_thu_nho).perform()
        except:
            pass

    def tat_video_cua_trinh_phat_thu_nho(self):
        try:
            pause_tat_video_cua_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_tat_video_cua_trinh_phat_thu_nho).perform()
            sleep(1)
            tat_video_cua_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-miniplayer-close-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(tat_video_cua_trinh_phat_thu_nho).click(tat_video_cua_trinh_phat_thu_nho).perform()
        except:
            pass

    def video_tiep_theo_trinh_phat_thu_nho(self):
        try:
            pause_video_tiep_theo_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_video_tiep_theo_trinh_phat_thu_nho).perform()
            sleep(1)
            video_tiep_theo_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-next-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(video_tiep_theo_trinh_phat_thu_nho).click(video_tiep_theo_trinh_phat_thu_nho).perform()
        except:
            pass

    def dung_video_trinh_phat_thu_nho(self):
        try:
            pause_dung_video_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_dung_video_trinh_phat_thu_nho).perform()
            sleep(1)
            dung_video_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-play-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(dung_video_trinh_phat_thu_nho).click(dung_video_trinh_phat_thu_nho).perform()
        except:
            pass

    def tat_trinh_phat_thu_nho(self):
        try:
            pause_tat_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_tat_trinh_phat_thu_nho).perform()
            sleep(1)
            tat_trinh_phat_thu_nho = trinhduyet.find_element_by_class_name('ytp-miniplayer-expand-watch-page-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(tat_trinh_phat_thu_nho).click(tat_trinh_phat_thu_nho).perform()            
        except:
            pass


    def bat_tat_phu_de(self):
        try:
            pause_phu_de = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_phu_de).perform()
            sleep(1)
            phu_de = trinhduyet.find_element_by_class_name('ytp-subtitles-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(phu_de).click(phu_de).perform()
        except:
            pass

    def bat_tat_tu_dong_phat(self):
        try:
            pause_tu_dong_phat = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_tu_dong_phat).perform()
            sleep(1)
            tu_dong_phat = trinhduyet.find_element_by_class_name('ytp-autonav-toggle-button-container')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(tu_dong_phat).click(tu_dong_phat).perform()
        except:
            pass

    def bat_tat_pause_video(self):
        try:
            pause_pause_video = trinhduyet.find_element_by_class_name('video-stream')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(pause_pause_video).click(pause_pause_video).perform()
        except:
            pass

    def video_tiep_theo(self):
        try:
            pause_video_tiep_theo = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_video_tiep_theo).perform()
            sleep(1)
            video_tiep_theo = trinhduyet.find_element_by_class_name('ytp-next-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(video_tiep_theo).click(video_tiep_theo).perform()
        except:
            pass

    def bat_tat_am_luong(self):
        try:
            pause_am_luong = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_am_luong).perform()
            sleep(1)
            am_luong = trinhduyet.find_element_by_class_name('ytp-mute-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(am_luong).click(am_luong).perform()
        except:
            pass

    def bat_tat_cai_dat(self):
        try:
            pause_cai_dat = trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(trinhduyet)
            action.move_to_element(pause_cai_dat).perform()
            sleep(1)
            cai_dat = trinhduyet.find_element_by_class_name('ytp-settings-button')
            trinhduyet.implicitly_wait(10)
            ActionChains(trinhduyet).move_to_element(cai_dat).click(cai_dat).perform()
        except:
            pass

    #def chat_luong_video(self):
        use = trinhduyet.find_element_by_xpath("//div[contains(text(),'Quality')]")
        trinhduyet.execute_script("arguments[0].click();",use)
        sleep()
        use = trinhduyet.find_element_by_xpath("//span[contains(string(),'144p')]")
        trinhduyet.execute_script("arguments[0].click();",use)
        sleep(3)

    #def toc_do_video(self)





        


    
    