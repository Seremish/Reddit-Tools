from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)

driver.get("https://www.reddit.com/login/")
time.sleep(5)
driver.find_element(By.NAME , "username").send_keys('YOUR USERNAME')
driver.find_element(By.NAME , "password").send_keys('YOUR PASSWORD')
driver.find_element(By.XPATH,'''//button[@type = 'submit']''').click()
time.sleep(5)

driver.get("https://www.reddit.com/subreddits/")
time.sleep(5)

subreddits = driver.find_elements(By.XPATH,'''//ul/li/span/a[contains(text(), "leave")]''')

i=0
for subreddit in subreddits:
    try:
        subreddit.click()
        time.sleep(2)
    except Exception as e:
        time.sleep(2)
    i = i + 1
    print(f'Progress {i} out of {len(subreddits)}')

driver.quit()
