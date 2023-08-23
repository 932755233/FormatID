import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import xlrd

# workbook = xlrd.open_workbook('/Users/danny/Desktop/common-documents/工作文档/采购入库/入库的编辑界面.xls')  # 打开Excel
# workbook = xlrd.open_workbook(r'C:\Users\Danny\Desktop\common-documents\工作文档\采购入库\入库的编辑界面.xls')  # 打开Excel

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\Danny\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()

driver.get("https://www.youku.com/channel/webhome?spm=a2hcb.collection.app.5~5~5~5~5~5~5~5!2~1~3~A")

# 切换页面
window_handles = driver.window_handles
driver.switch_to.window(window_handles[0])

print(driver.title)

startIndex = 1

workbook = xlrd.open_workbook(r'C:\Users\Danny\Desktop\账号.xls')  # 打开Excel
sheet = workbook.sheets()[0]
rows = sheet.nrows
print(f"一共{rows}个手机号")
username = ord('A')

password = ord('B') - username


def loginUsernameAndPassword(i):
    usernameStr = sheet.cell(i, 0).value
    passwordStr = sheet.cell(i, 1).value

    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[0])
    # 打开登录
    img = driver.find_element(By.CLASS_NAME, "usercenter_avatar_img ")
    img.click()

    iframe = driver.find_element(By.ID, 'alibaba-login-box')
    driver.switch_to.frame(iframe)

    # amimadenglu = driver.find_element(By.CLASS_NAME, "yk-login-title")
    amimadenglu = driver.find_element(By.XPATH, "//a[@class='yk-login-title']")
    amimadenglu.click()

    driver.find_element(By.ID, "fm-login-id").send_keys(usernameStr)
    driver.find_element(By.ID, "fm-login-password").send_keys(passwordStr)
    # time.sleep(1)
    inputC = driver.find_element(By.ID, "fm-agreement-checkbox")
    driver.execute_script('arguments[0].click()', inputC)
    # inputCec = driver.find_element(By.XPATH, "//label[@class='fm-agreement-text']").value_of_css_property('::after')
    # driver.find_element(By.CLASS_NAME,"fm-agreement-text").click()
    driver.find_element(By.CLASS_NAME, "fm-btn").click()
    print(f"登陆成功---{usernameStr}")


def startTask():
    driver.delete_all_cookies()
    driver.refresh()

    for i in range(0, sheet.nrows - 1):

        loginUsernameAndPassword(i)

        # driver.switch_to.default_content()

        time.sleep(0.5)

        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])

        print("打开个人信息")
        img = driver.find_element(By.CLASS_NAME, "usercenter_avatar_img ")
        img.click()

        driver.close()

        # time.sleep(2)
        time.sleep(0.5)
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
        time.sleep(0.5)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])
        ass = driver.find_elements(By.CLASS_NAME, "btn-link")
        ass[2].click()
        try:
            iframe = driver.find_element(By.ID, 'iframe1')

            driver.switch_to.frame(iframe)

            try:
                print('等待刷新验证码')
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'J_GetCode')))
            except:
                print('没有找到元素')
            finally:
                # time.sleep(5)
                driver.find_element(By.ID, "J_GetCode").click()
            yanzhengma111 = input('请输入验证码按回车结束：')

            driver.find_element(By.ID, "J_Phone_Checkcode").send_keys(yanzhengma111)
            time.sleep(0.5)
            driver.find_element(By.ID, "submitBtn").click()
        except:
            print('已经验证身份')
        phoneStr = input('请输入手机号按回车结束：')
        driver.find_element(By.ID, "J_Mobile").send_keys(phoneStr)
        time.sleep(0.3)
        driver.find_element(By.ID, "J_GetCode").click()
        yanzhengma222 = input('请输入验证码按回车结束：')
        driver.find_element(By.ID, "J_Phone_Checkcode").send_keys(yanzhengma222)
        time.sleep(0.3)
        inputqueding = driver.find_element(By.XPATH, "//input[@class='ui-button ui-button-lorange']")
        inputqueding.click()

        time.sleep(8)
        driver.delete_all_cookies()
        driver.refresh()


if __name__ == '__main__':
    startTask()
