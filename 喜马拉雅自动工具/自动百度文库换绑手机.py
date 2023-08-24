import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re

import xlrd
import requests

excelPath = r'C:\Users\Danny\Desktop\账号.xls'

# workbook = xlrd.open_workbook('/Users/danny/Desktop/common-documents/工作文档/采购入库/入库的编辑界面.xls')  # 打开Excel
# workbook = xlrd.open_workbook(r'C:\Users\Danny\Desktop\common-documents\工作文档\采购入库\入库的编辑界面.xls')  # 打开Excel

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\Danny\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()


# 切换页面
window_handles = driver.window_handles
driver.switch_to.window(window_handles[0])

print(driver.title)

# 配置
# startIndex = 1
authCodeCh = 10

# 解析excel表格

workbook = xlrd.open_workbook(excelPath)  # 打开Excel
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


# 验证新手机使用
def getNewPhoneAuthCode(phone):
    print(f'等待查询{phone}的验证码')
    time.sleep(10)
    authcodecc = ''
    for i in range(authCodeCh):
        time.sleep(1)
        response = requestNet('http://sms.szfangmm.com:3000/api/smslist?token=Go6ifqmfcbKqW39g77kkZQ')
        jsons = response.json()
        for json in jsons:
            content = json['content']
            if ('网易云音乐' in content) & (phone[-4:] == json['simnum'][-4:]):
                # pattern = re.compile(r'[1-9]\d*', )
                # authcodecc =  pattern.search(content)
                authcodecc = re.search(r'[1-9]\d*', content).group()
                print('查找到最近验证码:' + authcodecc)

                return authcodecc
    if authcodecc == '':
        return input('请手动输入验证码：')


# 验证身份使用
def getYanzhengAuthCode(phone):
    print(f'等待查询{phone}的验证码')
    time.sleep(8)
    authcodecc = ''
    for i in range(authCodeCh):
        time.sleep(1)
        response = requestNet('http://sms.szfangmm.com:3000/api/smslist?token=Go6ifqmfcbKqW39g77kkZQ')
        jsons = response.json()
        for json in jsons:
            content = json['content']
            if ('网易云音乐' in content) & (phone[-4:] == json['simnum'][-4:]):
                authcodecc = re.search(r'[1-9]\d*', content).group()
                print('查找到最近验证码:' + authcodecc)
                return authcodecc
    if authcodecc == '':
        return input('请手动输入验证码：')


# 登录使用
def getAuthCode(phone):
    print(f'等待查询{phone}的验证码')
    time.sleep(8)
    authcodecc = ''
    for i in range(authCodeCh):
        time.sleep(1)
        response = requestNet('http://sms.szfangmm.com:3000/api/smslist?token=Go6ifqmfcbKqW39g77kkZQ')
        jsons = response.json()
        for json in jsons:
            content = json['content']

            if ('网易' in content) & (phone[-4:] == json['simnum'][-4:]):
                authcodecc = re.search(r'[1-9]\d*', content).group()
                print('查找到最近验证码:' + authcodecc)
                return authcodecc
    if authcodecc == '':
        return input('请手动输入验证码：')


def loginUsernameOfAuthCode(usernameStr):
    print(f'开始登录----{usernameStr}')

    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[0])
    # 打开登录
    openDenglu = driver.find_element(By.LINK_TEXT, "登录")
    openDenglu.click()
    time.sleep(1)
    duanxindenlgu = driver.find_element(By.ID, "TANGRAM__PSP_11__changeSmsCodeItem")
    duanxindenlgu.click()
    time.sleep(0.5)

    driver.find_element(By.ID, 'TANGRAM__PSP_11__smsPhone').clear()
    driver.find_element(By.ID, 'TANGRAM__PSP_11__smsPhone').send_keys(usernameStr)

    driver.find_element(By.ID, 'TANGRAM__PSP_11__smsTimer').click()

    authCodeStr = getAuthCode(usernameStr)

    driver.find_element(By.ID, 'TANGRAM__PSP_11__smsVerifyCode').send_keys(authCodeStr)
    driver.find_element(By.ID, 'TANGRAM__PSP_11__smsSubmit').click()

    # inputC = driver.find_element(By.ID, "j-official-terms")
    # driver.execute_script('arguments[0].click()', inputC)
    #
    # shoujihao = driver.find_element(By.LINK_TEXT, "手机号登录/注册")
    # shoujihao.click()

    # iframe = driver.find_element(By.ID, 'alibaba-login-box')
    # driver.switch_to.frame(iframe)

    # amimadenglu = driver.find_element(By.CLASS_NAME, "yk-login-title")
    # amimadenglu = driver.find_element(By.XPATH, "//a[@class='yk-login-title']")
    # amimadenglu.click()
    # iframe = driver.find_element(By.ID, 'captcha-login-box').find_element(By.TAG_NAME, 'iframe')
    # driver.switch_to.frame(iframe)
    # iframes =driver.find_elements(By.TAG_NAME,'iframe')
    # for iframe in iframes:
    #     if 'x-URS-iframe' in iframe[id]:

    # driver.find_element(By.ID, "phoneipt").clear()
    # driver.find_element(By.ID, "phoneipt").send_keys(usernameStr)

    # 点击发送验证码
    # driver.find_element(By.LINK_TEXT, '获取验证码').click()
    # 获取验证码输入
    # authCodeStr = getAuthCode(usernameStr)
    # driver.find_element(By.XPATH, "//input[@placeholder='请输入短信验证码']").send_keys(authCodeStr)

    # driver.find_element(By.LINK_TEXT, "登录").click()

    print(f"验证码登陆成功---{usernameStr}")


def openHuanBang(usernameOld):
    print('打开百度账号设置 -> 换绑手机')
    driver.get('https://passport.baidu.com/v6/ucenter')
    driver.refresh()

    # try:
    #     print('等待绑定设置正常显示')
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, '修改')))
    # except:
    #     print('没有找到元素')
    # finally:

    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[0])

    pcmenus = driver.find_elements(By.CLASS_NAME, 'pc-menu')
    if len(pcmenus) == 0:
        print('登录失败！')
        exit()

    driver.find_elements(By.CLASS_NAME, 'pc-menu')[2].click()

    driver.find_elements(By.CLASS_NAME, 'pass-bind-button')[0].click()

    selects = driver.find_elements(By.ID, 'TANGRAM__2__content_type_select')

    if len(selects) != 0:
        # 可能需要旧手机号的验证码
        print('有元素')
        driver.find_element(By.ID, 'TANGRAM__2__button_send_mobile').click()
        authCodeOld = getYanzhengAuthCode(usernameOld)
        driver.find_element(By.ID, 'TANGRAM__2__input_vcode').send_keys(authCodeOld)
        driver.find_element(By.ID, 'TANGRAM__2__button_submit').click()


def bangDingNewPhone():
    # 输入新手机号
    newPhoneStr = input('请输入新手机号：')
    driver.find_element(By.ID, 'TANGRAM__1__input_mobile').send_keys(newPhoneStr)
    driver.find_element(By.ID, 'TANGRAM__1__button_send').click()
    print(f'开始等待{newPhoneStr}的验证码')
    authCodeNewStr = getNewPhoneAuthCode(newPhoneStr)
    print(f'验证码为{authCodeNewStr}')
    driver.find_element(By.ID, 'TANGRAM__1__input_vcode').send_keys(authCodeNewStr)
    driver.find_element(By.ID, 'TANGRAM__1__button_submit').click()

    return newPhoneStr


def startTask(startIndex):
    for i in range(startIndex - 1, sheet.nrows):
        driver.delete_all_cookies()
        driver.get("https://wenku.baidu.com/")
        driver.refresh()

        usernameStr = str(int(sheet.cell(i, 0).value))
        # passwordStr = sheet.cell(i, 1).value
        # loginUsernameAndPassword(i)
        print(f'第{i + 1}行----手机号：{usernameStr}----更换绑定开始！')

        loginUsernameOfAuthCode(usernameStr)

        time.sleep(1)

        openHuanBang(usernameStr)

        time.sleep(1)

        newPhoneStr = bangDingNewPhone()
        # newPhoneStr = '1231'

        print(f'{usernameStr}换绑为{newPhoneStr}成功!!!')

        tempText = driver.find_elements(By.CLASS_NAME, 'pass-bind-button')[1].text
        if '开启手机' in tempText:
            print(f'警告！！！手机号{newPhoneStr}需要手动打开手机号登录！！！')
            tempBool = input('是否继续运行脚本y/n：')
            if tempBool != 'y':
                return

        time.sleep(5)

        # WebDriverWait(driver, 20).until_not(EC.visibility_of_element_located((By.ID, 'nocaptcha')))

        # WebDriverWait(driver,10,0.1).until(EC.visibility_of_element_located((spans)))

        # iframe = driver.find_element(By.ID, 'iframe1')
        # driver.switch_to.frame(iframe)
        # try:
        #     print('等待刷新验证码')
        #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'J_GetCode')))
        # except:
        #     print('没有找到元素')
        # finally:
        #     # time.sleep(5)
        #     driver.find_element(By.ID, "J_GetCode").click()
        # # yanzhengma111 = input('请输入验证码按回车结束：')
        # authcodeOld = getYanzhengAuthCode(usernameStr)
        # driver.find_element(By.ID, "J_Phone_Checkcode").send_keys(authcodeOld)
        # time.sleep(0.5)
        # driver.find_element(By.ID, "submitBtn").click()


if __name__ == '__main__':
    index = input('从第几行开始：')
    startTask(int(index))
