import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\Danny\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
# 切换页面
window_handles = driver.window_handles
driver.switch_to.window(window_handles[0])

print(driver.title)

img = driver.find_element(By.CLASS_NAME, "usercenter_avatar_img ")
img.click()

driver.close()

# time.sleep(2)

window_handles = driver.window_handles
driver.switch_to.window(window_handles[0])

spans = driver.find_elements(By.TAG_NAME, "span")

# WebDriverWait(driver,10,0.1).until(EC.visibility_of_element_located((spans)))

for span in spans:
    if span.text == '个人设置':
        span.click()
        print('个人设置点击')
        break
aaas = driver.find_elements(By.TAG_NAME, "a")
for span in aaas:
    if span.text == '账号设置':
        span.click()
        print('账号设置点击')
        break

driver.close()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[0])
print(driver.title)
ass = driver.find_elements(By.CLASS_NAME, "btn-link")
ass[2].click()

iframe = driver.find_element(By.ID,'iframe1')
driver.switch_to.frame(iframe)

try:
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'J_GetCode')))
except:
    print('没有找到元素')
finally:
    # time.sleep(5)
    driver.find_element(By.ID,"J_GetCode").click()


# window_handles = driver.window_handles
# driver.switch_to.window(window_handles[0])
# yanzhengma = WebDriverWait(driver, 10,0.2).until(EC.visibility_of((By.ID, "J_GetCode")))
# yanzhengma = driver.find_element(By.ID, "J_GetCode")
# yanzhengma.click()

# bodys = driver.find_elements(By.CLASS_NAME, "subject-body")
#
# for body in bodys:
#     label = body.find_elements(By.TAG_NAME, "label")
#     label[0].click()


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
