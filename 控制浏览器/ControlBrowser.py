import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome.exe --remote-debugging-port=9222 --user-data-dir="F:\selenium\AutomationProfile"
from selenium.webdriver.common.service import Service

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# s = Service(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# driver = webdriver.Chrome(service=s, options=chrome_options)

# text = driver.find_elements("deferredfeedback")
# print(driver.title)
# print(text[0].find_elements("r0")[0].text)
# r0 = driver.find_elements("r0")
#
# for inputElement in r0:
#     inputElement.find_element_by_tag_name("input").click()
# browser = webdriver.Chrome()
# browser.get("http://www.baidu.com")

# browser.quit()

browser = webdriver.Chrome()  # 创建实例，支持Chrome，Firefox等等
browser.get('https://www.baidu.com/')  # 访问百度
browser.maximize_window()  # 窗口最大化
browser.find_element(By.NAME, 'wd').send_keys('Apple')  # 按name查找.传字符串
browser.find_element(By.ID, 'su').click()  # 按id查找.单击
#
# time.sleep(2)  # 百度跳太快23333
# actions = ActionChains(browser)  # 创建事件链
# element = browser.find_element_by_id('result_logo')  # 找到元素
# actions.move_to_element_with_offset(element, 210, 180)  # 相对位置移动鼠标
# actions.click()  # 单击
# actions.perform()  # 执行以上步骤
#
# browser.switch_to.window(browser.window_handles[-1])  # 切换到新打开的页面
# browser.find_element_by_css_selector('.ac-gn-link.ac-gn-link-mac').click()
# # Compound class names 用 css selector
#
# browser.delete_all_cookies()  # Cookie操作详见文档
browser.refresh()  # 刷新页面
