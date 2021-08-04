from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import pyautogui
import sys
from datetime import datetime
import psutil
import screen_brightness_control as sbc
from pack_and_run import os,time,schedule

# Note: Tất cả các hàm và class có thể gọi = str nên nếu chắc năng nào cần viết nhiều hàm
# thì chúng ta sẽ gọi hàm = srt

class Hardware:
	def __init__(self):
		# Thông số volume
		self.file_volume = open("in_volume.txt",'r')
		self.lines_volume = self.file_volume.readlines()
		self.M_volume = {}
		self.index_volume = 0
		for a in range(0,len(self.lines_volume)):
			self.lines_volume[a].replace("\n","")
			self.M_volume[self.index_volume] = float(self.lines_volume[a])
			self.index_volume += 2
		self.file_volume.close()

					

	# Hàm cho phép tắt phần mềm = task_manager	
	def killer(self,process_name):
		os.system('taskkill /f /im ' + process_name)

	# Hàm thay đổi âm lượng
	def change_volume(self,ok,value = 0):
		if(value % 2):
			value += 1
		devices = AudioUtilities.GetSpeakers()
		interface = devices.Activate(
		    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
		volume = cast(interface, POINTER(IAudioEndpointVolume))

		currentVolumeDb = volume.GetMasterVolumeLevel()
		_VALUE = [currentVolumeDb + 6,currentVolumeDb - 6,self.M_volume[value]] 

		# 0 : tăng, 1 : giảm, 2 : set âm thanh 
		try:
			volume.SetMasterVolumeLevel(_VALUE[ok], None)
		except:
			pass

	# Hàm về đổi unikey
	def change_unikey(self):
		pyautogui.hotkey('ctrl', 'shift')
		pyautogui.hotkey('alt', 'z')


	# Xem giờ
	def get_time(self):
		now = datetime.now()
		a = [now.strftime("%H"),now.strftime("%M"),now.strftime("%S")]
		return a

	# Xem ngày
	def get_day(self):
		now = datetime.now()
		a = [now.strftime("%d"),now.strftime("%m"),now.strftime("%Y")]
		return a

	# Hàm cho máy đi ngủ
	def sleep_computer(self):
		os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")

	# Hàm tắt máy tính
	def turn_off_computer(self):
		os.system("shutdown /s /t 1")

	# get ram
	def get_ram(self):
		return psutil.virtual_memory()[2]

	# get cpu
	def get_cpu(self):
		return psutil.cpu_percent(4)

	# get pin
	def get_battery(self):
		battery = psutil.sensors_battery()
		plugged = battery.power_plugged
		percent = str(battery.percent)
		plugged_EL = "Plugged In" if plugged else "Not Plugged In"
		plugged_VN = "Đang sạc" if plugged else "Không sạc"
		return [percent,plugged_EL,plugged_VN]


	# Bật tiết kiệm pin
	def battery_saving_on(self):
		os.system("powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 100")
		os.system("powercfg /setactive scheme_current")

	# Tắt tiết kiệm pin
	def battery_saving_off(self):
		os.system("powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 5")
		os.system("powercfg /setactive scheme_current")

	# Tăng độ sáng
	def screen_brightness_up(self,light = '+10'):
		sbc.set_brightness(light)

	# Giảm độ sáng
	def screen_brightness_down(self,light = '-10'):
		sbc.set_brightness(light)

	# Cài đặt độ sáng
	def screen_brightness_set(self,light):
		sbc.set_brightness(str(light))
