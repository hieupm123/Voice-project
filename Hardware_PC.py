from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import pyautogui
import os,sys
import time
from datetime import datetime
import psutil
import screen_brightness_control as sbc

# Lấy thông số volume từ file in_volume.txt
file_volume = open("in_volume.txt",'r')
lines_volume = file_volume.readlines()
M_volume = {}
index_volume = 0
for a in range(0,len(lines_volume)):
	lines_volume[a].replace("\n","")
	M_volume[index_volume] = float(lines_volume[a])
	index_volume += 2
file_volume.close()	

# Note: Tất cả các hàm và class có thể gọi = str nên nếu chắc năng nào cần viết nhiều hàm
# thì chúng ta sẽ gọi hàm = srt

class Hardware:
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
		_VALUE = [currentVolumeDb + 6,currentVolumeDb -6,M_volume[value]] 
		# 0 : tăng, 1 : giảm, 2 : set âm thanh 
		try:
			volume.SetMasterVolumeLevel(_VALUE[ok], None)
		except:
			pass

	# Hàm về unikey
	def unikey(self,func):
		def open_table_unikey():
			pyautogui.hotkey('ctrl', 'shift', 'f5')

		def change_unikey():
			pyautogui.hotkey('ctrl', 'shift')
			pyautogui.hotkey('alt', 'z')

		return locals()[func]()

	# Hàm lấy thời gian
	def get_current_time(self, func):
		now = datetime.now()
		def get_time():
			a = [now.strftime("%H"),now.strftime("%M"),now.strftime("%S")]
			return a
		def get_day():
			a = [now.strftime("%d"),now.strftime("%m"),now.strftime("%Y")]
			return a
		return locals()[func]()

	# Hàm cho máy đi ngủ
	def sleep_computer(self):
		os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")

	# Hàm tắt máy tính
	def turn_off_computer(self):
		os.system("shutdown /s /t 1")

	# Hàm về cpu,ram,battery
	def get_cpu_ram_battery(self,func):

		def get_ram():
			return psutil.virtual_memory()[2]

		def get_cpu():
			return psutil.cpu_percent(4)

		def get_battery():
			battery = psutil.sensors_battery()
			plugged = battery.power_plugged
			percent = str(battery.percent)
			plugged_EL = "Plugged In" if plugged else "Not Plugged In"
			plugged_VN = "Đang sạc" if plugged else "Không sạc"
			return [percent,plugged_EL,plugged_VN]

		return locals()[func]()

	# Hàm tăng giảm độ sáng, và tắt mở tiết kiệm pin
	def battery_saving_and_screen_brightness(self,func):
		def battery_saving_on():
			os.system("powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 100")
			os.system("powercfg /setactive scheme_current")

		def battery_saving_off():
			os.system("powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 5")
			os.system("powercfg /setactive scheme_current")

		def screen_brightness_up(light = '+10'):
			sbc.set_brightness(light)

		def screen_brightness_down(light = '-10'):
			sbc.set_brightness(light)

		def screen_brightness_set((str)light):
			sbc.set_brightness(light)

		locals()[func]()










		
