import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

text = driver.find_elements_by_class_name("deferredfeedback")
print(driver.title)
print(text[0].find_elements_by_class_name("r1")[0].text)


r0 = driver.find_elements_by_class_name("r1")

for inputElement in r0:
    inputElement.find_element_by_tag_name("input").click()