from pack_and_run import speech_and_say
from Hardware_PC import Hardware
# while(1):
# 	pyautogui.press("volumeup")
# 	test = Hardware()
# 	f = open('out.txt','a')
# 	f.write(str(test.change_volume(2)))
# 	f.write("\n")
# 	f.close()
# 	if(test.change_volume(2) == 0.0):
# 		break
import psutil
import os
import sys
import wmi
import screen_brightness_control as sbc
sbc.set_brightness('+10')
	
	
# from __future__ import print_function

# def get_cpu_temp():
#     t = psutil.sensors_temperatures()
#     for x in ['cpu-thermal', 'cpu_thermal']:
#         if x in t:
#             return t[x][0].current
#     print("Warning: Unable to get CPU temperature!")
#     return 0 


# Hieu sua
# ádasdasdasdasdas