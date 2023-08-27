from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from datetime import datetime
import os
import subprocess
import shutil
from moviepy.editor import VideoFileClip
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

#Code execution: web_scraping.py
with open('D:\\auto\\web_scraping.py', 'r') as file:
        code = file.read()
        exec(code)

#Code execution: filtr.py
with open('D:\\auto\\filtr.py', 'r') as file:
        code = file.read()
        exec(code)

#Code execution: processing.py
with open('D:\\auto\\processing.py', 'r') as file:
        code = file.read()
        exec(code)

#Code execution: youtube.py
with open('D:\\auto\\youtube.py', 'r') as file:
        code = file.read()
        exec(code)
