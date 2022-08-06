from os import getenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

remote_host = getenv('REMOTE_HOST')
url = getenv('TARGET_URL')

sleep(3) # wait for selenium container to start chrome

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
wd = webdriver.Remote(remote_host, options=chrome_options)

# example: click on every video on a profile
wd.get(url)
for video_card in wd.find_elements(By.CLASS_NAME, 'video-count'):
    print(f"Likes: {video_card.text}")
    ActionChains(wd).move_to_element(video_card).click().perform()
    
wd.close()