import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\Danny\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
# 切换页面
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])

print(driver.title)

bodys = driver.find_elements(By.CLASS_NAME, "subject-body")

for body in bodys:
    label = body.find_elements(By.TAG_NAME, "label")
    label[0].click()


# print(label[1].click())
# text = driver.find_elements(By.CLASS_NAME, "answer")
# print(driver.title)
# print(text[0].find_elements(By.CLASS_NAME, "r0")[0].text)
#
#
# r0 = driver.find_elements(By.CLASS_NAME, "r0")
#
# for inputElement in r0:
#     inputElement.find_element(By.TAG_NAME,"input").click()


# chrome --remote-debugging-port=9222 --user-data-dir="F:\chrome_config"  打开浏览器
