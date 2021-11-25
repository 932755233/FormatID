import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

text = driver.find_elements(By.CLASS_NAME, "answer")
print(driver.title)
print(text[0].find_elements(By.CLASS_NAME, "r1")[0].text)

r0 = driver.find_elements(By.CLASS_NAME, "r1")

for inputElement in r0:
    inputElement.find_element(By.TAG_NAME,"input").click()


# chrome --remote-debugging-port=9222 --user-data-dir="F:\chrome_config"  打开浏览器