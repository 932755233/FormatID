import datetime
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
from xlutils.copy import copy

excelPath = r'C:\Users\Danny\Desktop\会员时间查询.xls'

# 解析excel表格
workbook = xlrd.open_workbook(excelPath)  # 打开Excel
sheet = workbook.sheets()[0]
rows = sheet.nrows
print(f"一共{rows}个手机号")

username = ord('A')

password = ord('B') - username

tokens = ['cSuZgpUdwXxqWDCypT7kWB',
          'AeDuGbHvvMfBJ6WmebJptf',
          'Go6ifqmfcbKqW39g77kkZQ',
          'Hzri6aRhxM5eMoyyuXW293',
          'EsnEbw4cj8SjNEnxiyZVzE',
          'cjPUXdTtiYGCJj8qHLqVzi',
          'NaxhLGzQa6v5aV3n9w4FXN',
          'ATCd4fakvTSzzovJfjcRGJ',
          '95LUogpdxV2k9FnYpdWBcG',
          'UaoKiHcARvzuEvmSYJSa6c']

# tokens = ['Go6ifqmfcbKqW39g77kkZQ']

chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# driver = webdriver.Chrome(options=chrome_options)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': ''
    # 'cookie':'rr=https%3A%2F%2Fcn1.at101.design%2F; iadult=1; hello=1; __cf_bm=p5gOpquFCoj5a8TQG4EXkJgz3Ex7FnsYEfEnocDLOvQ-1672239337-0-Aald4rPN3hah3kmMughmjJnSoAXumWxycfq63F5ZGSO30pHcwtAbqaAZLHGXuYc6q8I0nZgdiJR75WSZ20zsF7Fd02vMkSA7GKGU+aEdw5fSL4rGkP3QLsGEgxf04R5AkhrkKQTrbTGgNWCpGXKzTss=; XSRF-TOKEN=eyJpdiI6ImZObDlvclwvZjN4SnhtMHNyb2NkcTNBPT0iLCJ2YWx1ZSI6InlqNUp4V3dSN2ZucDZYN2h0OExBT2NBMlVFZVpVWXNSUTZuR1NvbVMwMlZhVVJJTDhLNTBnTHIrQUFrNTJJVDIiLCJtYWMiOiI2OGFmNDM5NzE5MDc5ZGFjMTJmODJmYjZkMTVkNWViOGI0YWUyN2JlZjUwZjg2YzEyOTVjZTVjNmZkNmE5NTYzIn0%3D; miao_ss=eyJpdiI6IlZUczhoMFJjN2VhUlRFYis1NXBYZ3c9PSIsInZhbHVlIjoiR2RWRDZncElnemNZa0poTnhGbHNcL1ZoTmlnVDhhNndYcVgxSHFTMCtcL3VnbUVZTXAyWGtCclloaURQR2dwMXVaIiwibWFjIjoiZjBlM2QzZDRjM2FmNzhmZjBmNjliMzgzNGI4NTZiZWEzZmY2MDg5YmJhZDBmNjI5NzJmYzcxMDc0OWNmN2U5YyJ9'
}


def getExcelStr(row, col):
    cell = sheet.cell(row, col)
    if cell.ctype == 2:
        return str(int(cell.value))
    else:
        return cell.value


def requestNet(url, proxies=None):
    return requests.get(url, headers=headers, proxies=proxies, verify=False)


def getAuthCode(phone):
    headers = {}
    # print(f'等待查询{phone}的验证码')
    sendCodeTimeLong = time.time()
    # timettt = input('请输入:')
    # sendCodeTimeLong = time.mktime(time.strptime(timettt, "%Y-%m-%d %H:%M:%S"))
    time.sleep(5)
    bean = {'token': '', 'code': ''}
    for i in range(10):
        time.sleep(1)
        for token in tokens:
            response = requestNet(f'http://sms.szfangmm.com:3000/api/smslist?token={token}')
            # print(response)
            if response.status_code == 200:
                # try:
                jsons = response.json()
                for json in jsons:
                    # print(json)
                    content = json['content']
                    # 获得列表中的发送时间
                    oldSendTime = json['time']
                    oldSendTimeLong = time.mktime(time.strptime(oldSendTime, "%Y-%m-%d %H:%M:%S"))
                    if oldSendTimeLong < sendCodeTimeLong:
                        # print(f'{oldSendTime}----{oldSendTimeLong}')
                        break
                    if ('网易' in content) & ('验证码' in content) & (phone[-4:] == json['simnum'][-4:]):
                        authcodecc = '0000' + str(re.search(r'[1-9]\d*', content).group())
                        # print('查找到最近验证码:' + authcodecc[-6:])
                        bean['code'] = authcodecc[-6:]
                        bean['token'] = token
                        return bean
            # except:
            #     print(response.text)
            #     print(token)
            else:
                print(f'链接失败token：{token}')
    return bean


def loginUsernameOfAuthCode(usernameStr):
    print(f'----开始登录')

    # window_handles = driver.window_handles
    # driver.switch_to.window(window_handles[0])
    # 打开登录
    print('------打开登录页')
    openDenglu = driver.find_element(By.LINK_TEXT, "登录")
    openDenglu.click()
    time.sleep(1)
    print('------选择其他登录模式')
    qitadenglu = driver.find_element(By.LINK_TEXT, "选择其他登录模式")
    qitadenglu.click()
    time.sleep(1)
    print('------选择手机号验证码登录')
    inputC = driver.find_element(By.ID, "j-official-terms")
    driver.execute_script('arguments[0].click()', inputC)

    shoujihao = driver.find_element(By.LINK_TEXT, "手机号登录/注册")
    shoujihao.click()

    # iframe = driver.find_element(By.ID, 'alibaba-login-box')
    # driver.switch_to.frame(iframe)

    # amimadenglu = driver.find_element(By.CLASS_NAME, "yk-login-title")
    # amimadenglu = driver.find_element(By.XPATH, "//a[@class='yk-login-title']")
    # amimadenglu.click()
    iframe = driver.find_element(By.ID, 'captcha-login-box').find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    # iframes =driver.find_elements(By.TAG_NAME,'iframe')
    # for iframe in iframes:
    #     if 'x-URS-iframe' in iframe[id]:

    print('------输入手机号')
    driver.find_element(By.ID, "phoneipt").clear()
    driver.find_element(By.ID, "phoneipt").send_keys(usernameStr)

    print('------等待验证码')
    # 点击发送验证码
    driver.find_element(By.LINK_TEXT, '获取验证码').click()
    # 获取验证码输入
    authCodeStr = getAuthCode(usernameStr)
    # authCodeStr = {'code': ''}
    if authCodeStr['code'] == '':
        # 没找到验证码 直接进入下一个查询
        # tempCode = input('请输入验证码\n输入1直接开始查询会员时间\n输入0开始下一个：')
        # if len(tempCode) == 1:
        return {'code': '0', 'message': '收不到验证码'}
        # else:
        #     authCodeStr['code'] = tempCode

    driver.find_element(By.XPATH, "//input[@placeholder='请输入短信验证码']").send_keys(authCodeStr['code'])

    driver.find_element(By.LINK_TEXT, "登录").click()

    time.sleep(2)
    print('------判断登录状态')
    # 判断是否新号注册
    xinhaos = driver.find_elements(By.XPATH, "//div[text()='完成注册，开启云音乐']")
    if len(xinhaos) > 0:
        # 当前为新号
        return {'code': '0', 'message': '未注册的新号'}

    tophead = driver.find_element(By.CLASS_NAME, 'm-tophead')
    masks = tophead.find_elements(By.CLASS_NAME, 'mask')
    print('----登录逻辑完成')
    if len(masks) > 0:
        # 登录成功
        print(masks[0].text)
        return {'code': '1', 'message': '登录成功'}
    else:
        # 登录失败
        return {'code': '0', 'message': '可以接收验证码但登录失败'}
    # n_user_profile = driver.find_element(By.CLASS_NAME,'n-user-profile')
    # infos = n_user_profile.find_elements(By.CLASS_NAME,'info')

    # yonghumings = driver.find_elements(By.ID, 'j-vip-code-to-home')
    # if len(yonghumings) > 0:
    #     # 登录成功
    #     print(yonghumings[0].text)
    #     return {'code': '1', 'message': '登录成功'}
    # else:
    #     # 登录失败
    #     return {'code': '0', 'message': '可以接收验证码但登录失败'}
    # try:
    #     print('等待判断是否新号注册')
    #     WebDriverWait(driver, 3).until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[text()='完成注册，开启云音乐']")))
    #     # 是新号注册
    # except:
    #     print('没有找到元素')
    # finally:
    #     driver.find_element()

    # print(f"验证码登陆成功---{usernameStr}")


def searchVip():
    driver.get('https://music.163.com/#/member?refer=myvipweb')
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'g_iframe')))
    except:
        return {'message': '未找到会员iframe', 'code': '0'}
    iframe = driver.find_element(By.ID, 'g_iframe')
    driver.switch_to.frame(iframe)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'index_expire__fgB3_')))
    except:
        return {'message': '未找到会员时间', 'code': '0'}

    div = driver.find_element(By.CLASS_NAME, 'index_expire__fgB3_')
    return {'message': div.text}


def startTask(startIndex):
    new_workbook = copy(workbook)
    new_sheet = new_workbook.get_sheet(0)

    for i in range(startIndex - 1, sheet.nrows):
        global driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://music.163.com/#")
        # usernameStr = str(int(sheet.cell(i, 0).value))
        usernameStr = getExcelStr(i, 0)
        print(f'第{i + 1}行----手机号：{usernameStr}----查询会员开始！')

        tempBean = loginUsernameOfAuthCode(usernameStr)
        # tempBean = {'code': '1'}
        if tempBean['code'] != '0':
            time.sleep(2)
            tempBean = searchVip()

        print(f'----信息：{tempBean["message"]}')

        # 保存查询后数据
        print(f'----保存文件')
        # 复制单元格
        new_sheet.write(i, 1, tempBean['message'])
        if tempBean['code'] == '1':
            cookies = driver.get_cookies()
            cookie = [item["name"] + "=" + item["value"] for item in cookies]
            cookiestr = ';'.join(item for item in cookie)
            print(f'----获取到的Cookie：{cookiestr}')
            new_sheet.write(i, 2, cookiestr)
        # 保存文件
        new_workbook.save(r'C:\Users\Danny\Desktop\会员时间查询1.xls')

        # driver.delete_all_cookies()
        # driver.get('chrome://settings/clearBrowserData')
        time.sleep(2)
        # clearButton = driver.execute_script(
        #     "return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
        # clearButton.click()
        driver.quit()
        print(f'第{i + 1}行----手机号：{usernameStr}----完成')
        print()


if __name__ == '__main__':
    startIndex = int(input('请输入开始行数：'))
    startTask(startIndex)
