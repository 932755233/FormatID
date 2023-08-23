import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import xlrd
import requests

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

# 配置
startIndex = 1
authCodeCh = 10

# 解析excel表格


workbook = xlrd.open_workbook(r'C:\Users\Danny\Desktop\账号.xls')  # 打开Excel
sheet = workbook.sheets()[0]
rows = sheet.nrows
print(f"一共{rows}个手机号")
username = ord('A')

password = ord('B') - username

# 网络请求
# proxy = '192.168.3.220:7890'
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'http://' + proxy
# }

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': ''
    # 'cookie':'rr=https%3A%2F%2Fcn1.at101.design%2F; iadult=1; hello=1; __cf_bm=p5gOpquFCoj5a8TQG4EXkJgz3Ex7FnsYEfEnocDLOvQ-1672239337-0-Aald4rPN3hah3kmMughmjJnSoAXumWxycfq63F5ZGSO30pHcwtAbqaAZLHGXuYc6q8I0nZgdiJR75WSZ20zsF7Fd02vMkSA7GKGU+aEdw5fSL4rGkP3QLsGEgxf04R5AkhrkKQTrbTGgNWCpGXKzTss=; XSRF-TOKEN=eyJpdiI6ImZObDlvclwvZjN4SnhtMHNyb2NkcTNBPT0iLCJ2YWx1ZSI6InlqNUp4V3dSN2ZucDZYN2h0OExBT2NBMlVFZVpVWXNSUTZuR1NvbVMwMlZhVVJJTDhLNTBnTHIrQUFrNTJJVDIiLCJtYWMiOiI2OGFmNDM5NzE5MDc5ZGFjMTJmODJmYjZkMTVkNWViOGI0YWUyN2JlZjUwZjg2YzEyOTVjZTVjNmZkNmE5NTYzIn0%3D; miao_ss=eyJpdiI6IlZUczhoMFJjN2VhUlRFYis1NXBYZ3c9PSIsInZhbHVlIjoiR2RWRDZncElnemNZa0poTnhGbHNcL1ZoTmlnVDhhNndYcVgxSHFTMCtcL3VnbUVZTXAyWGtCclloaURQR2dwMXVaIiwibWFjIjoiZjBlM2QzZDRjM2FmNzhmZjBmNjliMzgzNGI4NTZiZWEzZmY2MDg5YmJhZDBmNjI5NzJmYzcxMDc0OWNmN2U5YyJ9'
}


def requestNet(url, proxies=None):
    return requests.get(url, headers=headers, proxies=proxies, verify=False)


def getAuthCode(phone):
    print(f'等待查询{phone}的验证码')
    time.sleep(3)
    for i in range(authCodeCh):
        time.sleep(1)
        response = requestNet('http://sms.szfangmm.com:3000/api/smslist?token=AeDuGbHvvMfBJ6WmebJptf')
        jsons = response.json()
        for json in jsons:
            content = json['content']
            findex = content.find('【优酷土豆】您的短信验证码是')

            # print((phone[-4:] == json['simnum'][-4:]))
            # print(phone[-4:])
            # print(json['simnum'][-4:])

            if findex == 1 & (phone[-4:] == json['simnum'][-4:]):
                print('查找到最近验证码:' + content[15:21])
                return content[15:21]


def loginUsernameOfAuthCode(usernameStr):
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[0])
    # 打开登录
    img = driver.find_element(By.CLASS_NAME, "usercenter_avatar_img ")
    img.click()

    iframe = driver.find_element(By.ID, 'alibaba-login-box')
    driver.switch_to.frame(iframe)

    # amimadenglu = driver.find_element(By.CLASS_NAME, "yk-login-title")
    # amimadenglu = driver.find_element(By.XPATH, "//a[@class='yk-login-title']")
    # amimadenglu.click()

    driver.find_element(By.ID, "fm-sms-login-id").send_keys(usernameStr)

    # time.sleep(1)
    inputC = driver.find_element(By.ID, "fm-agreement-checkbox")
    driver.execute_script('arguments[0].click()', inputC)
    # inputCec = driver.find_element(By.XPATH, "//label[@class='fm-agreement-text']").value_of_css_property('::after')
    # driver.find_element(By.CLASS_NAME,"fm-agreement-text").click()

    # 点击发送验证码
    driver.find_element(By.CLASS_NAME, "send-btn").click()
    # 获取验证码输入
    authcodestr = getAuthCode(usernameStr)
    driver.find_element(By.ID, 'fm-smscode').send_keys(authcodestr)

    driver.find_element(By.CLASS_NAME, "fm-btn").click()
    print(f"验证码登陆成功---{usernameStr}")


def loginUsernameAndPassword(usernameStr, passwordStr):

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
    print(f"密码登陆成功---{usernameStr}")


def startTask():
    driver.delete_all_cookies()
    driver.refresh()

    for i in range(0, sheet.nrows - 1):

        usernameStr = sheet.cell(i, 0).value
        # passwordStr = sheet.cell(i, 1).value
        # loginUsernameAndPassword(i)

        loginUsernameOfAuthCode(usernameStr)

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
            # yanzhengma111 = input('请输入验证码按回车结束：')
            authcodeOld = getAuthCode(usernameStr)
            driver.find_element(By.ID, "J_Phone_Checkcode").send_keys(authcodeOld)
            time.sleep(0.5)
            driver.find_element(By.ID, "submitBtn").click()
        except:
            print('已经验证身份')

        phoneStr = input('请输入手机号按回车结束：')
        driver.find_element(By.ID, "J_Mobile").send_keys(phoneStr)
        time.sleep(0.3)
        driver.find_element(By.ID, "J_GetCode").click()

        authcodeNew = getAuthCode(usernameStr)
        driver.find_element(By.ID, "J_Phone_Checkcode").send_keys(authcodeNew)
        time.sleep(0.3)
        inputqueding = driver.find_element(By.XPATH, "//input[@class='ui-button ui-button-lorange']")
        inputqueding.click()

        time.sleep(8)
        driver.delete_all_cookies()
        driver.refresh()


if __name__ == '__main__':
    startTask()
    # authcode = getAuthCode('13249565382')
    # print(authcode)
    # driver.refresh()
    # driver.delete_all_cookies()
    # loginUsernameOfAuthCode(1)
