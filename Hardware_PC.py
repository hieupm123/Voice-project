from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
# import pya

class Hardware:
	def change_volume(self,ok,value = 0):
		devices = AudioUtilities.GetSpeakers()
		interface = devices.Activate(
		    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
		volume = cast(interface, POINTER(IAudioEndpointVolume))

		currentVolumeDb = volume.GetMasterVolumeLevel()
		_VAlUE = [currentVolumeDb + 6,currentVolumeDb -6,0,-65.25] 
		# 0 : tăng
		# 1 : giảm
		# 2 : max
		# 3 : min
		try:
			volume.SetMasterVolumeLevel(_VAlUE[ok], None)
		except:
			pass
		


