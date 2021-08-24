import time
import pyautogui
import webbrowser
import pandas as pd
from datetime import datetime, timedelta

pyautogui.FAILSAFE = True


def open_chrome(meet_code):
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    if webbrowser.get(chrome_path).open("https://meet.google.com/"):
        pyautogui.sleep(3)
        pyautogui.click(323, 570)
        pyautogui.write(meet_code)
        pyautogui.sleep(1.2)
        pyautogui.press('enter')
        pyautogui.sleep(5)
        pyautogui.hotkey('command', 'e')
        pyautogui.hotkey('command', 'd')
        pyautogui.sleep(5)
        pyautogui.click(1029, 488)


def find_class():
    df = pd.read_csv('class_links.csv')
    today = datetime.now()
    time_ = today
    diff_time = timedelta(minutes=5)
    upper_time_range = time_ + diff_time
    lower_time_range = time_ - diff_time

    meet_code = ""
    for row in df.itertuples():
        Index, hour, minute, code = row
        new_time = datetime(hour=hour, minute=minute, year=datetime.now().year, month=datetime.now().month,
                            day=datetime.now().day)
        if lower_time_range.time() <= new_time.time() <= upper_time_range.time():
            meet_code = code

    if meet_code:
        open_chrome(meet_code)
        return True
    return False


while True:
    print("searching class...")
    if find_class():
        print("class found, joining")
        break
    else:
        print("class not found")
        print("sleeping for 1 minute")
        time.sleep(60)
