# bofetch 1.0 - read Github page :
# https://github.com/gabrielmchiapetti/bofetch

import os
from os import system as sy
import datetime
import platform
import time

try:
	import psutil
except Exception:
        print("Downloading dependencies (psutil)...")
        time.sleep(1.2)
	sy("pip3 install psutil")
	import psutil

try:
	import distro
except Exception:
	print("Downloading dependecies (distro)...")
        time.sleep(1.2)
	sy("pip3 install distro")
	import distro

def conv(bytes, suffix="B"):
    fact = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < fact:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= fact

inf = platform.uname()
mem = psutil.virtual_memory()
frq = psutil.cpu_freq()

distro = str.capitalize(str(distro.name(pretty=True)))
datetime = str(datetime.datetime.now())

usr = psutil.users()[0]
usrname = usr.name
usrhost = platform.node()
realusr = str(usrname) + "@" + str(usrhost)
fullusr = f"\033[1;36m{str(usrname)}\033[m" + f"\033[1;35m@\033[m" + f"\033[1;32m{str(usrhost)}\033[m"

calc_user = (50 - len(realusr)) // 2

print("    .--.    " + "  " + "\033[1;33m=\033[m"*calc_user + " " + fullusr + " " + "\033[1;33m=\033[m"*calc_user)
print("   |o_o |   " + "  " + f"\033[37;1m• System:           \033[1;34m{distro}\033[m")
print("   |:_/ |   " + "  " + f"\033[37;1m• Kernel:           \033[1;36m{platform.release()}\033[m")
print("  //   \ \  " + "  " + f"\033[37;1m• Architecture:     \033[1;35m{inf.machine}\033[m")
print(" (|     | ) " + "  " + f"\033[37;1m• RAM:              \033[1;32m{conv(mem.used)} / {conv(mem.total)} ({mem.percent}%)\033[m")
print("/'\_   _/'\ " + "  " + f"\033[37;1m• CPU frequency:    \033[1;33m{frq.current:.2f}Mhz ({psutil.cpu_count(logical=False)} cores)\033[m")
print("\___)=(___/ " + "  " + "\033[1;33m=\033[m"*12 + " " + datetime + " " + "\033[1;33m=\033[m"*12)
