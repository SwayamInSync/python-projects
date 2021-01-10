from selenium import webdriver
import time

url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

chrome_driver_path = "<Your chrome driver location path>"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)

sign_in_btn = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")
sign_in_btn.click()

time.sleep(2)

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("your linkdin email")
password.send_keys("linkedin password")
driver.find_element_by_css_selector("button").click()

time.sleep(5)

all_jobs = driver.find_elements_by_css_selector(".jobs-search-results__list li")
for job in all_jobs:
    job.click()
    time.sleep(1)
    apply_btn = driver.find_element_by_class_name("jobs-apply-button")
    apply_btn.click()
    time.sleep(1)
    submit_button = driver.find_element_by_css_selector("footer button")
    if submit_button.get_attribute("aria-label") != "Submit application":
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
        time.sleep(1)
        discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
        continue
    else:
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        phone.send_keys("Your phone number")
        submit_button.click()
        break

