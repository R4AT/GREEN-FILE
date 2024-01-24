import os, platform, time, sys
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 import FILE 
elif bit == '32bit':
 import SEX 
