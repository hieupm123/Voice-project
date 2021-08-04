from general_web import *

general = general_web()
output_check = general.lay_ten_nguoi_dung()

class youtube(object):
    trinhduyet = None
    def mo_trinh_duyet(self):
        try:
            options = webdriver.ChromeOptions()
            PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
            PATH1 = PATH[:9] + output_check + PATH[9:]
            options.add_argument("user-data-dir=" + PATH1)
            self.trinhduyet = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
            self.trinhduyet.get("https://www.youtube.com/watch?v=Lz8G_Hwc8B8")
            self.trinhduyet.maximize_window() 
            time.sleep(3)
        except:
            pass  

    def trang_chu(self):
        try:
            self.trinhduyet.get('https://www.youtube.com/')
            time.sleep(2)
        except:
                pass

    def kham_pha(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('title')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[1]).click(phu_luc[1]).perform()
        except:
                pass

    def kenh_dang_ky(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('title')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[2]).click(phu_luc[2]).perform()
        except:
                pass

    def thu_vien(self):
        try:
            phu_luc = self.trinhduyet.find_elements_by_class_name('title')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_luc[3]).click(phu_luc[3]).perform()
        except:
            pass
        
    #Chọn video trên trang chủ---------------------------------------------------------------------------------------------------------------------------


    def chon_video_o_trang_chu(self,a=''):
        try:
            chon_video_o_trang_chu = self.trinhduyet.find_elements_by_id('content')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon_video_o_trang_chu[a]).click(chon_video_o_trang_chu[a]).perform()
        except:
                pass
def scroll_down(self,a=''):
    try:
        self.trinhduyet.execute_script("window.scrollTo(0, window.scrollY + " + str(a) + " )")
    except:
        pass

def scroll_up(self,a=''):
    try:
        self.trinhduyet.execute_script("window.scrollTo(0, window.scrollY + " - str(a) + " )")
    except:
            pass

#Thao tác phụ lục bên phải youtube---------------------------------------------------------------------------------------------------------------------------------



#Chọn vidoe trên khám phá---------------------------------------------------------------------------------------------------------------------------------
class vidoe_kham_pha(youtube):
    def trending(self):
        try:
            trending = self.trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(trending[1]).click(trending[1]).perform()
        except:
            pass

    def music(self):
        try:
            music = self.trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(music[2]).click(music[2]).perform()
        except:
            pass

    def gaming(self):
        try:
            gaming = self.trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(gaming[3]).click(gaming[3]).perform()
        except:
            pass

    def news(self):
        try:
            news = self.trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(news[4]).click(news[4]).perform()
        except:
            pass
        
    def sports(self):
        try:
            sports = self.trinhduyet.find_elements_by_class_name('ytd-destination-shelf-renderer')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(sports[5]).click(sports[5]).perform()
        except:
            pass

    def chon_video_o_kham_pha(self,a=''):
        try:
            chon = self.trinhduyet.find_elements_by_class_name('ytd-expanded-shelf-contents-renderer')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon[a]).click(chon[a]).perform()
        except:
            pass 


#Thao tác trên tìm kiếm-------------------------------------------------------------------------------------------------------------------------

class search_youtube(youtube):


    def search(self,nhap=''):
        try:
            nhan = self.trinhduyet.find_element_by_xpath('//*[@id="search"]')
            nhan.send_keys(nhap)
            nhan.send_keys(Keys.RETURN)
        except:
            pass

    def chon_video_tim_kiem(self,a=''):
        try:
            chon = self.trinhduyet.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(chon[a-1]).click(chon[a-1]).perform()
        except:
            pass

    def quay_lai_tim_kiem(self,nhap=''):
        try:
            tim_kiem_lai =  self.trinhduyet.find_element_by_id('search')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tim_kiem_lai).click(tim_kiem_lai).perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('backspace')
            sleep(1)
            tim_kiem_lai.send_keys(nhap)
            tim_kiem_lai.send_keys(Keys.RETURN)
        except:
            pass

    def next_video_khi_xem_video(self,b=''):
        try:
            next_video = self.trinhduyet.find_elements_by_class_name('style-scope ytd-compact-video-renderer')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(next_video[b-1]).click(next_video[b-1]).perform()
        except:
            pass

    def truy_cap_kenh(self):
        try:
            truy_cap_kenh = self.trinhduyet.find_element_by_xpath('//*[@id="top-row"]/ytd-video-owner-renderer/a')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(truy_cap_kenh).click(truy_cap_kenh).perform()
        except:
            pass

    def phong_to_nho(self):
        try:
            pause_phong_to_nho = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_phong_to_nho).perform()
            sleep(1)
            phong_to_nho = self.trinhduyet.find_element_by_class_name('ytp-fullscreen-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phong_to_nho).click(phong_to_nho).perform()
        except:
            pass

    def bat_tat_phat_tren_TV(self):
        try:
            pause_phat_tren_TV = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_phat_tren_TV).perform()
            sleep(1)
            phat_tren_TV = self.trinhduyet.find_element_by_class_name('ytp-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phat_tren_TV).click(phat_tren_TV).perform()
        except:
            pass

    def bat_tat_che_do_rap_chieu_phim(self):
        try:
            pause_che_do_rap_chieu_phim = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_che_do_rap_chieu_phim).perform()
            sleep(1)
            che_do_rap_chieu_phim = self.trinhduyet.find_element_by_class_name('ytp-size-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(che_do_rap_chieu_phim).click(che_do_rap_chieu_phim).perform()
        except:
            pass


    def bat_trinh_phat_thu_nho(self):
        try:
            pause_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_trinh_phat_thu_nho).perform()
            sleep(1)
            bat_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(bat_trinh_phat_thu_nho).click(bat_trinh_phat_thu_nho).perform()
        except:
            pass

    def tat_video_cua_trinh_phat_thu_nho(self):
        try:
            pause_tat_video_cua_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_tat_video_cua_trinh_phat_thu_nho).perform()
            sleep(1)
            tat_video_cua_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-close-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tat_video_cua_trinh_phat_thu_nho).click(tat_video_cua_trinh_phat_thu_nho).perform()
        except:
            pass

    def video_tiep_theo_trinh_phat_thu_nho(self):
        try:
            pause_video_tiep_theo_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_video_tiep_theo_trinh_phat_thu_nho).perform()
            sleep(1)
            video_tiep_theo_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-next-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(video_tiep_theo_trinh_phat_thu_nho).click(video_tiep_theo_trinh_phat_thu_nho).perform()
        except:
            pass

    def dung_video_trinh_phat_thu_nho(self):
        try:
            pause_dung_video_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_dung_video_trinh_phat_thu_nho).perform()
            sleep(1)
            dung_video_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-play-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(dung_video_trinh_phat_thu_nho).click(dung_video_trinh_phat_thu_nho).perform()
        except:
            pass

    def tat_trinh_phat_thu_nho(self):
        try:
            pause_tat_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-scrim')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_tat_trinh_phat_thu_nho).perform()
            sleep(1)
            tat_trinh_phat_thu_nho = self.trinhduyet.find_element_by_class_name('ytp-miniplayer-expand-watch-page-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tat_trinh_phat_thu_nho).click(tat_trinh_phat_thu_nho).perform()            
        except:
            pass


    def bat_tat_phu_de(self):
        try:
            pause_phu_de = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_phu_de).perform()
            sleep(1)
            phu_de = self.trinhduyet.find_element_by_class_name('ytp-subtitles-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(phu_de).click(phu_de).perform()
        except:
            pass

    def bat_tat_tu_dong_phat(self):
        try:
            pause_tu_dong_phat = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_tu_dong_phat).perform()
            sleep(1)
            tu_dong_phat = self.trinhduyet.find_element_by_class_name('ytp-autonav-toggle-button-container')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(tu_dong_phat).click(tu_dong_phat).perform()
        except:
            pass

    def bat_tat_pause_video(self):
        try:
            pause_pause_video = self.trinhduyet.find_element_by_class_name('video-stream')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(pause_pause_video).click(pause_pause_video).perform()
        except:
            pass

    def video_tiep_theo(self):
        try:
            pause_video_tiep_theo = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_video_tiep_theo).perform()
            sleep(1)
            video_tiep_theo = self.trinhduyet.find_element_by_class_name('ytp-next-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(video_tiep_theo).click(video_tiep_theo).perform()
        except:
            pass

    def bat_tat_am_luong(self):
        try:
            pause_am_luong = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_am_luong).perform()
            sleep(1)
            am_luong = self.trinhduyet.find_element_by_class_name('ytp-mute-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(am_luong).click(am_luong).perform()
        except:
            pass

    def bat_tat_cai_dat(self):
        # try:
            pause_cai_dat = self.trinhduyet.find_element_by_class_name('video-stream')
            action = ActionChains(self.trinhduyet)
            action.move_to_element(pause_cai_dat).perform()
            time.sleep(1)
            cai_dat = self.trinhduyet.find_element_by_class_name('ytp-settings-button')
            self.trinhduyet.implicitly_wait(10)
            ActionChains(self.trinhduyet).move_to_element(cai_dat).click(cai_dat).perform()
        # except:
        #     pass

    def chat_luong_video(self,index = 3):
        try:
<<<<<<< HEAD
            # Sử lí giọng nói để lấy chất lượng video
=======
>>>>>>> e678d32719d972692f9e27850fb62bd1c617d45a
            quality = ['144p','240p','360p','480p','720p','1080p','1440p']
            use = self.trinhduyet.find_element_by_xpath("//div[contains(text(),'Quality')]")
            self.trinhduyet.execute_script("arguments[0].click();",use)
            time.sleep(2)
            ans = quality[index]
            Xpath_quality = "//span[contains(string(),'" + ans + "')]"
            print(Xpath_quality)
            use = self.trinhduyet.find_element_by_xpath(Xpath_quality)
            self.trinhduyet.execute_script("arguments[0].click();",use)
            time.sleep(3)
        except:
            pass
    def toc_do_video(self,index = 3):
<<<<<<< HEAD
        # Sử lí giọng nói để xử lí toc_do_video
=======
        # out  = 
        # Normal
>>>>>>> e678d32719d972692f9e27850fb62bd1c617d45a
        speed = ['0.25','0.5','0.75','Chuẩn','1.25','1.5','1.75','2']
        use = self.trinhduyet.find_element_by_xpath("//div[contains(text(),'Playback speed')]")
        self.trinhduyet.execute_script("arguments[0].click();",use)
        time.sleep(2)
        ans = speed[index]
        Xpath_quality = "//span[contains(string(),'" + ans + "')]"
        use = self.trinhduyet.find_element_by_xpath(Xpath_quality)
        self.trinhduyet.implicitly_wait(10)
        ActionChains(self.trinhduyet).move_to_element(use).click(use).perform()
        time.sleep(3)
I = youtube()
I.mo_trinh_duyet()
# time.sleep(1)
B = search_youtube()
B.trinhduyet = I.trinhduyet
time.sleep(3)
B.bat_tat_cai_dat()
time.sleep(2)
B.toc_do_video(index = 7)
# time.sleep(3)
# B.chat_luong_video()
# 




        


    
    