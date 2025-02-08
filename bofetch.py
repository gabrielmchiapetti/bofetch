import os
from os import system as sy
import datetime
import platform

try:
	import psutil
except Exception:
	sy("pip3 install psutil")
	import psutil

try:
	import distro
except Exception:
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


print("    .--.    " + "  " + "\033[33;1m=\033[m"*64)
print("   |o_o |   " + "  " + f"\033[37;1m• System:           \033[34;1m{distro}\033[m")
print("   |:_/ |   " + "  " + f"\033[37;1m• Version:          \033[36;1m{platform.release()}\033[m")
print("  //   \ \  " + "  " + f"\033[37;1m• Architecture:     \033[35m{inf.machine}\033[m")
print(" (|     | ) " + "  " + f"\033[37;1m• RAM:              \033[32;1m{conv(mem.used)} / {conv(mem.total)} ({mem.percent}%)\033[m")
print("/'\_   _/'\ " + "  " + f"\033[37;1m• CPU frequency:    \033[33;1m{frq.current:.2f}Mhz ({psutil.cpu_count(logical=False)} cores)\033[m")
print("\___)=(___/ " + "  " + "\033[33;1m=\033[m"*18 + " " + datetime + " " + "\033[33;1m=\033[m"*18)
