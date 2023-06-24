# ----------------------------
#
#   创建日期：2023/6/20
#   创建人：danny
#
# ----------------------------
from selenium import webdriver

options = webdriver.ChromeOptions()
options.debugger_address = "127.0.1:9222"
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")

browser.maximize_window()
