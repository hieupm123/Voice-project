from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import pyautogui
import os
import time

# Lấy thông số volume
file_volume = open("in_volume.txt",'r')
lines_volume = file_volume.readlines()
M_volume = {}
index_volume = 0
for a in range(0,len(lines_volume)):
	lines_volume[a].replace("\n","")
	M_volume[index_volume] = float(lines_volume[a])
	index_volume += 2
file_volume.close()	

#
class Hardware:
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

	def unikey(self,ok):
		# 0 : chuyển đổi chế độ
		# 1 : Bật bảng mã unikey

		def open_unikey():
			pyautogui.hotkey('ctrl', 'shift', 'f5')
		def change_unikey():
			pyautogui.hotkey('ctrl', 'shift')
			pyautogui.hotkey('alt', 'z')
		if(ok):
			open_unikey();
		else:
			change_unikey();


		
