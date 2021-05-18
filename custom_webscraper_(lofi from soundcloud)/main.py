from selenium import webdriver
import time

chrome_driver_path = "/Users/swayam/development_resources/chromedriver"
lofi_songs = []

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://soundcloud.com/search/sounds?q=LOFI")
time.sleep(2)

accept_cookie = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
accept_cookie.click()

last_height = driver.execute_script("return document.body.scrollHeight")
for n in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    last_height = new_height


title = driver.find_elements_by_css_selector('#content > div > div > div.l-main > div > div > div > ul > li > div > div > div > div.sound__content > div.sound__header > div > div > div.soundTitle__usernameTitleContainer > a')
links = driver.find_elements_by_css_selector('#content > div > div > div.l-main > div > div > div > ul > li > div > div > div > div.sound__content > div.sound__header > div > div > div.soundTitle__usernameTitleContainer > a')
creator_name = driver.find_elements_by_css_selector('#content > div > div > div.l-main > div > div > div > ul > li > div > div > div > div.sound__content > div.sound__header > div > div > div.soundTitle__usernameTitleContainer > div > a')

for n in range(len(title)):
    tune_title = title[n].text
    tune_link = links[n].get_attribute('href')
    tune_creator = creator_name[n].text
    tune = {
        "name": tune_title,
        "creator": tune_creator,
        "link": tune_link
    }
    lofi_songs.append(tune)

print(len(lofi_songs))

with open('lofi_tunes.csv', 'w') as file:
    file.write("Title,Creator,Link")
    for song in lofi_songs:
        title = song.get('name')
        creator = song.get('creator')
        link = song.get('link')
        file.write(f"\n{title},{creator},{link}")