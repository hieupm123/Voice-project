from general_web import *
from pack_and_run import *
general = general_web()
output_check = general.lay_ten_nguoi_dung()

# để lấy tên người dùng phầnục vụ chức năng lưu cookie sau này
speech = speech_and_say();

def speech_catch_error():
	text_catch = 'Có gì đó không đúng bạn vui lòng xem lại yêu cầu của mình'
	speech.say_VN_by_Google(text_catch)

class facebook(object): 
	driver_web = None

	# Khởi tạo facebook
	def init(self):
		options = webdriver.ChromeOptions()
		PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
		PATH1 = PATH[:9] + output_check + PATH[9:]
		options.add_argument("user-data-dir=" + PATH1)
		self.driver_web = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
		self.driver_web.get("https://www.facebook.com")
		time.sleep(3)


	def click_to_any_button(self, PATH):
		self.driver_web.execute_script("arguments[0].click();",self.driver_web.find_element_by_xpath(PATH))
		time.sleep(randint(1,2))

	# Quay lại trang chủ facebook
	def home_facebook(self):
		self.driver_web.get("https://www.facebook.com")
		time.sleep(randint(1,2))


	def element_in_viewport(self,drivers, elem):
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



class Search_in_facebook(facebook):

	# Gõ và tìm trên thanh tìm kiếm bạn bè
	def type_in_search(self,name = 'Vũ Minh Hiếu'): # lưu ý driver là biến, func là tên hàm
		try:
			text = speech.speech_none_pause();
			if(text != ''):
				name = text;
			search_buttons = self.driver_web.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input")
			for button in search_buttons:
				button.send_keys(name)
				time.sleep(1)
				button.send_keys(Keys.RETURN)
			time.sleep(randint(1,2))
		except:
			speech.say_VN_by_Google(text_catch);

	# Nhấn vào thanh tìm kiếm bạn bè
	def click_in_search(self):
		try:
			self.driver_web.execute_script("arguments[0].click();",self.driver_web.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/label/input"))
		except:
			speech_catch_error()
	# Chọn bạn bè trên facebook
	def chose_when_find(self, number_of_tab = 1):
		text = speech.speech_none_pause();
		number_of_tab = general.get_number()
		PATH = '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/ul/li[' + str(number_of_tab) + ']/div/a'
		try:
			self.driver_web.execute_script("arguments[0].click();",self.driver_web.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/label/input"))
			time.sleep(randint(1,2));
			self.click_to_any_button(PATH)
			time.sleep(randint(1,2))
		except:
			speech_catch_error()

class story_facebook(facebook):
	# Xem story
	def watch_story(self,number_of_tab = 1):
		text = speech.speech_none_pause();
		number_of_tab = general.get_number(text)
		PATH = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[' + str(number_of_tab + 1) + ']/div/div/div/a'
		try:
			self.click_to_any_button(PATH)
		except:
			speech_catch_error() # sau xử lý bug với âm thanh
		time.sleep(randint(1,2))


	# Chọn story trong các story ở trong
	def chose_story(self,number_of_tab = 1):
		try:
			text = speech.speech_none_pause();
			number_of_tab = general.get_number(text)
			PATH = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[' + str(number_of_tab + 1) + ']/div/div/div'
			self.click_to_any_button(PATH)
			time.sleep(randint(1,2));
		except:
			speech_catch_error()

	# Chọn story tiếp theo
	def next_story(self):
		PATH = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div[3]/div/div/div/div[1]/div[1]/div[3]/div/div/div[2]'
		try:
			self.click_to_any_button(PATH)
		except:
			speech_catch_error()
	# Bình luận trong story
	def comment(self,text = 'Bạn cute thế!'):
		try:
			text_ = speech.speech_none_pause();
			if(text_ != ''):
				text = text_;
			comment = self.driver_web.find_element_by_xpath('//div[@aria-label="Trả lời..."]');
			comment.send_keys(text);
			time.sleep(randint(1,2));
			comment.send_keys(Keys.RETURN);
			time.sleep(randint(1,2));
		except:
			speech_catch_error()

	# Thả biểu cảm story
	def bieu_cam_facebook(self, stt_bieu_cam = 2):
		bieu_cam = ['Thích','Yêu thích','Thương thương','Haha','Wow','Buồn','Phẫn nộ']
		try:
			if(stt_bieu_cam == 0):
				like = self.driver_web.find_elements_by_xpath('//div[@aria-label="' + bieu_cam[stt_bieu_cam] + '"]')
				ActionChains(self.driver_web).move_to_element(like[0]).click(like[0]).perform()	
			else:
				like = self.driver_web.find_elements_by_xpath('//div[@aria-label="' + bieu_cam[stt_bieu_cam] + '"]')
				ActionChains(self.driver_web).move_to_element(like[0]).click(like[0]).perform()
			time.sleep(randint(1,2));
		except:
			speech_catch_error()

class Friend_facebook(facebook):
	# Mở list friend
	PATH = 'https://www.facebook.com/friends'


	# Chuyển sang tab bạn bè
	def trang_chu_ban_be(self):
		self.driver_web.get(self.PATH)
		time.sleep(randint(1,2))

	# Chuyển sang tab ưu tiên bạn bè
	def open_suggestions(self):
		self.driver_web.get(self.PATH +  '/suggestions/')
		time.sleep(randint(1,2))

	# Show list friend
	def list_friend(self):
		self.driver_web.get(self.PATH + '/list/')
		time.sleep(randint(1,2))

class watch_facebook(facebook):	

	# Tạm dừng và tiếp tục khi xem video ở ngoài watch
	def tat_mo_tam_dung_facebook(self):
		for i in range(1,100):
			try:
				use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[' + str(i) + ']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[5]')
				if(self.element_in_viewport(self.driver_web,use)):
					hover = ActionChains(self.driver_web).move_to_element(use);
					time.sleep(randint(1,2))
					try:
						self.click_to_any_button('//div[@aria-label="Tạm dừng"]')
					except:
						self.click_to_any_button('//div[@aria-label="Phát"]')
					time.sleep(randint(1,2))
					return
			except:
				speech_catch_error()
				return;

	# bật tắt loa ở ngoài
	def bat_tat_loa_facebook(self):
		for i in range(1,100):
			try:
				use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[' + str(i) + ']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[5]')
				if(self.element_in_viewport(self.driver_web,use)):
					time.sleep(randint(1,2))
					click = self.driver_web.find_elements_by_xpath('//div[@aria-label="Bật tiếng"]')
					self.driver_web.execute_script('arguments[0].click()',click[i - 1])
					return
			except:
				speech_catch_error()
				return		


	# Comment vào video trong watch
	def comment(self,text = 'Bạn kia cute thế!'):
		# text là phần người ta muốn comment
		use = None
		text_ = speech.speech_none_pause()
		if(text_ != ''):
			text = text_;
		try:
			use = self.driver_web.find_elements_by_xpath('//div[@aria-label="Viết bình luận"]')
			time.sleep(randint(1,2))
		except:
			speech_catch_error()
			return;
		for i in range(1,100):
			try:

				if(self.element_in_viewport(self.driver_web,self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[' + str(i) + ']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[5]'))):
					self.driver_web.execute_script('arguments[0].click()',use[i - 1])
					time.sleep(randint(2,3))
					button = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[' + str(i) + ']/div/div/div/div/div[2]/div[3]/div[3]/div[2]/form/div/div/div[1]/p')
					time.sleep(randint(1,2))
					button.send_keys(text)
					time.sleep(randint(1,2))
					button.send_keys(Keys.RETURN)
					time.sleep(randint(1,2))
					return;
			except:
				speech_catch_error()
				return
				
	# Cảm xúc khi xem video
	def bieu_cam_facebook(self,stt_bieu_cam = 0):
		#Tính từ 0
		bieu_cam = ['Thích','Yêu thích','Thương thương','Haha','Wow','Buồn','Phẫn nộ']
		for i in range(1,200):
			try:
				if(self.element_in_viewport(self.driver_web,self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[' + str(i) + ']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[4]'))):
					like = self.driver_web.find_elements_by_xpath('//div[@aria-label="Thích"]')
					hover = ActionChains(self.driver_web).move_to_element(like[i - 1])
					time.sleep(randint(1,2))
					hover.perform()
					time.sleep(1)
					like = self.driver_web.find_element_by_xpath('//span[@aria-label="' + bieu_cam[stt_bieu_cam] + '"]')
					time.sleep(randint(1,2))
					self.driver_web.execute_script("arguments[0].click();",like)
					return;
			except:
				speech_catch_error()
				return

	# Lưu và follow
	def save_and_follow(self,chose = 1):
		# 1 : save , 3 follow
		for i in range(1,300):
			try:
				if(self.element_in_viewport(self.driver_web,self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[' + str(i) + ']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[4]'))):
					self.click_to_any_button('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[' + str(i) + ']/div/div/div/div/div[2]/div[1]/div[1]/div[3]/div/div')
					time.sleep(2)
					use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[' + str(chose) + ']/div[2]/div/div[1]/span')
					if(use.text[0] != 'B'):
						self.click_to_any_button('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[' + str(chose) + ']')
						webdriver.ActionChains(self.driver_web).send_keys(Keys.ESCAPE).perform()
					return
			except:
				speech_catch_error()
				return

	def trang_chu_watch(self):
		self.driver_web.get('https://www.facebook.com/watch')
		time.sleep(randint(1,2))

	def find_video(self,text = 'meo'):
		text_ = speech.speech_none_pause();
		if(text_ != ''):
			text = text_
		self.driver_web.get('https://www.facebook.com/watch/search/?q=' + text)
		time.sleep(randint(1,2))


class watch_facebook_in(facebook):
	# Tạm dừng và tiếp tục khi xem video trong watch
	def tat_mo_tam_dung_facebook(self):
		time.sleep(randint(1,2))
		ActionChains(self.driver_web).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()


	# Thả biểu cảm khi xem video
	def bieu_cam_facebook(self,stt_bieu_cam = 0):
		#tinh từ 0 là like
		bieu_cam = ['Thích','Yêu thích','Thương thương','Haha','Wow','Buồn','Phẫn nộ']
		try:
			like = self.driver_web.find_element_by_xpath('//div[@aria-label="Thích"]')
			time.sleep(randint(1,2))
			hover = ActionChains(self.driver_web).move_to_element(like)
			time.sleep(randint(1,2))
			hover.perform()
			time.sleep(randint(1,2))
			self.click_to_any_button('//span[@aria-label="' + bieu_cam[stt_bieu_cam] + '"]')
		except:
			speech_catch_error()


class status_facebook(facebook):

	# Tìm số thứ tự của bài
	def find_index(self):
		click1 = 0; click2 = 0; click3 = 0; click4 = 0;
		for i in range(1,350):
			try:
				click1_use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[' + str(i) + ']/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div')
				click1 = self.element_in_viewport(self.driver_web,click1_use)
			except:
				pass

			try:
				click2_use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[' + str(i)+ ']/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]/div/div')
				click2 = self.element_in_viewport(self.driver_web,click2_use)
			except:
				pass

			try:
				click3_use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[' + str(i) + ']/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div')
				click3 = self.element_in_viewport(self.driver_web,click3_use)
			except:
				pass

			try:
				click4_use = self.driver_web.find_elements_by_xpath('//div[@aria-label="Thích"]')
				click4 = self.element_in_viewport(self.driver_web,click4_use[i - 1])
			except:
				pass

			if(click1 or click2 or click3 or click4):
				return i
		return -10;

	# Thả biểu cảm trong status
	def bieu_cam_facebook(self, stt_bieu_cam = 0):
		#Tính từ 0
		bieu_cam = ['Thích','Yêu thích','Thương thương','Haha','Wow','Buồn','Phẫn nộ']
		
		try:
			i = self.find_index()
			like = self.driver_web.find_elements_by_xpath('//div[@aria-label="Thích"]')
			hover = ActionChains(self.driver_web).move_to_element(like[i - 1])
			time.sleep(randint(1,2))
			hover.perform()
			time.sleep(2)
			like = self.driver_web.find_element_by_xpath('//div[@aria-label="' + bieu_cam[stt_bieu_cam] + '"]')
			self.driver_web.execute_script("arguments[0].click();",like)
		except:
			speech_catch_error()
			return

	# Lưu status
	def save_and_follow(self):
		try:
			i = self.find_index();
			time.sleep(randint(1,2))
			save = self.driver_web.find_elements_by_xpath('//div[@aria-label="Hành động với bài viết này"]')
			self.driver_web.execute_script("arguments[0].click();",save[i - 1])
			time.sleep(1);
			save = self.driver_web.find_element_by_xpath('//div[@role="menuitem"]')
			self.driver_web.execute_script("arguments[0].click();",save)
			time.sleep(randint(1,2));
			save = self.driver_web.find_element_by_xpath('//div[@aria-label="Xong"]')
			self.driver_web.execute_script("arguments[0].click();",save)
			time.sleep(randint(1,2));
		except:
			speech_catch_error()

class check_tin_nhan_thong_bao(facebook):
	# Kiểm tra tin nhắn mới
	def check_tin_nhan(self):
		text = 'Có gì đó không ổn'
		if(self.driver_web == None):
			try:
				options = webdriver.ChromeOptions()
				PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
				PATH1 = PATH[:9] + output_check + PATH[9:]
				options.add_argument("user-data-dir=" + PATH1)
				driver = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
				driver.get("https://www.facebook.com")
				time.sleep(1)
				use = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]')
				time.sleep(2)
				text = use.get_attribute("aria-label")
				text = text.replace('Messenger','Không có tin nhắn mới')
				text = text.replace('Không có tin nhắn mới,' ,'')
				driver.quit()
				speech.say_VN_by_Google(text.strip())
				return;
			except:
				speech_catch_error()
				return;

		try:
			use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]')
			text = use.get_attribute("aria-label")
			text = text.replace('Messenger','Không có tin nhắn mới')
			text = text.replace('Không có tin nhắn mới,' ,'')
		except:
			speech_catch_error()
			return;
		speech.say_VN_by_Google(text)


	# Kiếm tra thông báo mới	
	def check_thong_bao(self):
		text = 'Có gì đó không ổn'
		if(self.driver_web == None):
			try:
				options = webdriver.ChromeOptions()
				PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
				PATH1 = PATH[:9] + output_check + PATH[9:]
				options.add_argument("user-data-dir=" + PATH1)
				driver = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
				driver.get("https://www.facebook.com")
				time.sleep(1)
				use = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[1]/span/div/a')
				time.sleep(2)
				text = use.get_attribute("aria-label")
				text = text.replace('Thông báo','Không có thông báo mới')
				text = text.replace('Không có thông báo mới,' ,'')
				driver.quit()
				speech.say_VN_by_Google(text.strip())
				return;
			except:
				speech_catch_error()
				return;

		try:
			use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[1]/span/div/a')
			text = use.get_attribute("aria-label")
			text = text.replace('Thông báo','Không có thông báo mới')
			text = text.replace('Không có thông báo mới,' ,'')
		except:
			speech_catch_error()
			return;
		speech.say_VN_by_Google(text)

	

# chức năng về mess
class messenger:

	driver_web = None

		
	def init(self):
		options = webdriver.ChromeOptions()
		PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
		PATH1 = PATH[:9] + output_check + PATH[9:]
		options.add_argument("user-data-dir=" + PATH1)
		self.driver_web = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
		self.driver_web.get("https://www.messenger.com/")
		time.sleep(2)

	# Tìm kiếm bạn bè theo tên trên mess
	def type_in_search(self, name = 'Vũ Minh Hiếu'):
		try:
			text_ = speech.speech_none_pause()
			if(text_ != ''):
				name = text_;
			time.sleep(randint(1,2))
			use = self.driver_web.find_element_by_xpath('//input[@type="search"]')
			use.send_keys(name)
			time.sleep(randint(1,2))
		except:
			speech_catch_error()

	# Chọn thứ tự người muốn tìm trong danh sách
	def chon_nguoi_muon_tim(self, id = 0):
		try:
			text = speech.speech_none_pause()
			id = general.get_number(text)
			time.sleep(randint(1,2))
			use = self.driver_web.find_elements_by_xpath('//a[@role="presentation"]')
			self.driver_web.execute_script("arguments[0].click();",use[id])
			time.sleep(randint(1,2))
		except:
			speech_catch_error()
		
	# Tìm kiếm bạn bè trong danh sách
	def search_by_index(self,id):
		try:
			text = speech.speech_none_pause()
			id = general.get_number(text)
			time.sleep(randint(1,2))
			use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[' + str(id) + ']/div/div/a')
			time.sleep(randint(1,2))
			self.driver_web.execute_script("arguments[0].click();",use)
		except:
			speech_catch_error()	

	# nhắn tin với người bên kia
	def chat(self, text = 'Bạn bên kia cute thế'):
		try:
			text_ = speech.speech_none_pause()
			if(text_ != ''):
				text = text_;
			time.sleep(randint(1,2))
			use = self.driver_web.find_element_by_xpath('//div[@role="textbox"]')
			use.send_keys(text)
			time.sleep(randint(1,2))
			use.send_keys(Keys.RETURN)
		except:
			speech_catch_error()

	# Gọi điện với người bên kia
	def call_nor(self):
		try:
			time.sleep(randint(1,2))
			use = self.driver_web.find_element_by_xpath('//div[@aria-label="Bắt đầu gọi thoại"]')
			self.driver_web.execute_script('arguments[0].click()',use)
			time.sleep(randint(1,2))
		except:
			speech_catch_error()

	# Gọi video với người bên kia
	def call_vid(self):
		try:
			time.sleep(randint(1,2))
			use = self.driver_web.find_element_by_xpath('//div[@aria-label="Bắt đầu gọi video"]')
			self.driver_web.execute_script('arguments[0].click()',use)
			time.sleep(randint(1,2))
		except:
			speech_catch_error()

	# Nhấn vào nút like
	def click_like(self):
		try:
			time.sleep(randint(1,2))
			use = self.driver_web.find_element_by_xpath('//div[@aria-label="Gửi lượt thích"]')
			self.driver_web.execute_script('arguments[0].click()',use)
			time.sleep(randint(1,2))
		except:
			speech_catch_error()
	# Lấy tên người nhắn tin gần nhất
	def lay_ten_nguoi_gan_nhat(self):
		text = 'Có gì đó không ổn'
		if(self.driver_web == None):
			try:
				options = webdriver.ChromeOptions()
				PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
				PATH1 = PATH[:9] + output_check + PATH[9:]
				options.add_argument("user-data-dir=" + PATH1)
				driver = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
				driver.get("https://www.messenger.com/")
				time.sleep(4)
				use = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div[1]/h2/span/span/a')
				text = use.text
				driver.quit()
				speech.say_VN_by_Google(text.strip());
				return;
			except:
				speech.say_VN_by_Google(text);
				return;

		try:
			use = self.driver_web.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div[1]/h2/span/span/a')
			text = use.text
		except:
			speech.say_VN_by_Google(text);
			return;
		speech.say_VN_by_Google(text);