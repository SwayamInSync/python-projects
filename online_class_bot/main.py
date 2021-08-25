import time
import os
import pyautogui
import webbrowser
import pandas as pd
from datetime import datetime, timedelta

pyautogui.FAILSAFE = True

"""
Before using it remember it only work for google meet, also you need to change the path to your chrome browser.
replace the (x,y) coordinated inside pyautogui.click() to your screen's respective coordinates.
"""


def open_chrome(meet_code, duration):
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'  # replcae the path to your chrome browser
    print("class found, joining")
    if webbrowser.get(chrome_path).open("https://meet.google.com/"):
        pyautogui.sleep(3)
        pyautogui.click(323, 570)  # coordinate for meet_code input
        pyautogui.write(meet_code)
        pyautogui.sleep(1.2)
        pyautogui.press('enter')
        pyautogui.sleep(5)
        pyautogui.hotkey('command', 'e')  # stop the video
        pyautogui.hotkey('command', 'd')  # mute yourself
        pyautogui.sleep(5)
        pyautogui.click(1029, 488)  # coordinate for joining class button

        joining_time = datetime.now()
        ending_time = joining_time + timedelta(seconds=duration)
        while True:
            if datetime.now().time().hour == ending_time.hour and datetime.now().minute == ending_time.minute and datetime.now().second == ending_time.second:
                os.system("killall -9 'Google Chrome'")
                break
            else:
                time.sleep(60*10) # modify it according to your ram usage and common sense for timing check


def find_class():
    duration_in_seconds = 0
    df = pd.read_csv('class_links.csv')
    today = datetime.now()
    time_ = today
    diff_time = timedelta(minutes=5)
    upper_time_range = time_ + diff_time
    lower_time_range = time_ - diff_time

    meet_code = ""
    for row in df.itertuples():
        Index, hour, minute, code, duration_in_seconds = row
        new_time = datetime(hour=hour, minute=minute, year=datetime.now().year, month=datetime.now().month,
                            day=datetime.now().day)
        if lower_time_range.time() <= new_time.time() <= upper_time_range.time():
            meet_code = code

    if meet_code:
        open_chrome(meet_code, duration_in_seconds)
        return duration_in_seconds
    return False


"""
for windows crontab don't work so use while loop below
"""

while True:
    print("searching class...")
    sec = find_class()
    if sec:
        time.sleep(10) # waiting for 10 seconds before searching for a new class
    else:
        print("class not found")
        print("sleeping for 1 hour")
        time.sleep(60 * 60)
