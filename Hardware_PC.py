from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

file = open("out.txt",'r')
lines = file.readlines()
M = {}
cnt = 0
for a in range(0,len(lines)):
	lines[a].replace("\n","")
	M[cnt] = float(lines[a])
	cnt += 2
file.close()	


class Hardware:
	def change_volume(self,ok,value = 0):
		if(value % 2):
			value += 1
		devices = AudioUtilities.GetSpeakers()
		interface = devices.Activate(
		    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
		volume = cast(interface, POINTER(IAudioEndpointVolume))

		currentVolumeDb = volume.GetMasterVolumeLevel()
		_VALUE = [currentVolumeDb + 6,currentVolumeDb -6,M[value]] 
		# 0 : tăng
		# 1 : giảm
		# 2 : set
		try:
			volume.SetMasterVolumeLevel(_VALUE[ok], None)
		except:
			pass
		
