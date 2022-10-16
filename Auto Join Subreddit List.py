from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")

service = Service(executable_path="PATH TO CHROME DRIVER")

with open("PATH TO SUBREDDIT LIST FILE", "r", encoding="utf-8") as f:
    subreddits = f.readlines()

driver = webdriver.Chrome(options=options, service=service)

driver.get("https://www.reddit.com/login/")
time.sleep(5)
driver.find_element(By.NAME , "username").send_keys('YOUR USERNAME')
driver.find_element(By.NAME , "password").send_keys('YOUR PASSWORD')
driver.find_element(By.XPATH,'''//button[@type = 'submit']''').click()
time.sleep(5)

i=0
for subreddit in subreddits:
    try:
        driver.get(f'https://www.reddit.com/r/{subreddit.strip()}')
        time.sleep(5)
        driver.find_element(By.XPATH,'''//div/button[contains(text(), "Join")]''').click()
        time.sleep(2)
        with open("subreddits joined.txt", "a", encoding="utf-8") as f:
            f.write(subreddit)
    except Exception as e:
        with open("subreddits error.txt", "a", encoding="utf-8") as f:
            f.write(subreddit)
        time.sleep(2)
    i = i + 1
    print(f'Progress {i} out of {len(subreddits)}', flush=True)

driver.quit()
