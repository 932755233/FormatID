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
from authcodeutils import AuthCodeUtils


class WangYiAuto:
    tokens = ['cSuZgpUdwXxqWDCypT7kWB',
              'Go6ifqmfcbKqW39g77kkZQ',
              'Hzri6aRhxM5eMoyyuXW293',
              'EsnEbw4cj8SjNEnxiyZVzE',
              'ATCd4fakvTSzzovJfjcRGJ',
              '95LUogpdxV2k9FnYpdWBcG',
              'UaoKiHcARvzuEvmSYJSa6c']

    def __init__(self):
        # 网络请求
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': ''
            # 'cookie':'rr=https%3A%2F%2Fcn1.at101.design%2F; iadult=1; hello=1; __cf_bm=p5gOpquFCoj5a8TQG4EXkJgz3Ex7FnsYEfEnocDLOvQ-1672239337-0-Aald4rPN3hah3kmMughmjJnSoAXumWxycfq63F5ZGSO30pHcwtAbqaAZLHGXuYc6q8I0nZgdiJR75WSZ20zsF7Fd02vMkSA7GKGU+aEdw5fSL4rGkP3QLsGEgxf04R5AkhrkKQTrbTGgNWCpGXKzTss=; XSRF-TOKEN=eyJpdiI6ImZObDlvclwvZjN4SnhtMHNyb2NkcTNBPT0iLCJ2YWx1ZSI6InlqNUp4V3dSN2ZucDZYN2h0OExBT2NBMlVFZVpVWXNSUTZuR1NvbVMwMlZhVVJJTDhLNTBnTHIrQUFrNTJJVDIiLCJtYWMiOiI2OGFmNDM5NzE5MDc5ZGFjMTJmODJmYjZkMTVkNWViOGI0YWUyN2JlZjUwZjg2YzEyOTVjZTVjNmZkNmE5NTYzIn0%3D; miao_ss=eyJpdiI6IlZUczhoMFJjN2VhUlRFYis1NXBYZ3c9PSIsInZhbHVlIjoiR2RWRDZncElnemNZa0poTnhGbHNcL1ZoTmlnVDhhNndYcVgxSHFTMCtcL3VnbUVZTXAyWGtCclloaURQR2dwMXVaIiwibWFjIjoiZjBlM2QzZDRjM2FmNzhmZjBmNjliMzgzNGI4NTZiZWEzZmY2MDg5YmJhZDBmNjI5NzJmYzcxMDc0OWNmN2U5YyJ9'
        }
        # 解析excel表格
        self.excelPath = r'C:\Users\Danny\Desktop\网易严选自动领取账号.xls'
        self.workbook = xlrd.open_workbook(self.excelPath)  # 打开Excel
        self.sheet = self.workbook.sheets()[0]
        self.rows = self.sheet.nrows

        self.loginUrl = 'https://m.you.163.com/u/login'
        self.getGoodUrl = 'https://act.you.163.com/act/static/WlBvtWUxKpLs.html?from=planC98C67F59D9696F5plan&channel_type=1'
        self.checkUrl = 'https://m.you.163.com/coupon'

        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def requestNet(self, url, proxies=None):
        return requests.get(url, headers=self.headers, proxies=proxies, verify=False)

    def getAuthCode(self, phone):
        # print(f'等待查询{phone}的验证码')
        time.sleep(5)
        bean = {'token': '', 'code': ''}
        for i in range(10):
            time.sleep(1)
            for token in self.tokens:
                response = self.requestNet(f'http://sms.szfangmm.com:3000/api/smslist?token={token}')
                # print(response)
                jsons = response.json()
                for json in jsons:
                    content = json['content']
                    if ('网易' in content) & ('验证码' in content) & (phone[-4:] == json['simnum'][-4:]):
                        authcodecc = '0000' + str(re.search(r'[1-9]\d*', content).group())
                        # print('查找到最近验证码:' + authcodecc[-6:])
                        bean['code'] = authcodecc[-6:]
                        bean['token'] = token
                        return bean
        return bean
        # if authcodecc == '':
        #     return input('请手动输入验证码：')

    def getExcelStr(self, row, col):
        cell = self.sheet.cell(row, col)
        if cell.ctype == 2:
            return str(int(cell.value))
        else:
            return cell.value

    def getGood(self):
        self.driver.get(self.getGoodUrl)
        self.driver.find_element(By.CLASS_NAME, 'u-ADAB8E-button-image').click()

    def loginWangYi(self, phone):
        self.driver.get(self.loginUrl)
        self.driver.refresh()
        div = self.driver.find_element(By.XPATH, '//span[text()="手机号快捷登录"]/..')
        div.click()

        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'phoneipt')))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="mobileView"]/iframe')))

        iframe = self.driver.find_element(By.ID, 'mobileView').find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)

        print('|----填入手机号')
        self.driver.find_element(By.ID, 'phoneipt').clear()
        self.driver.find_element(By.ID, 'phoneipt').send_keys(phone)

        self.driver.find_element(By.LINK_TEXT, '获取验证码').click()

        time.sleep(1)
        # 判断是否显示滑块拼图
        slideboxs = self.driver.find_elements(By.ID, 'ScapTcha')
        if len(slideboxs) > 0:
            print('|----滑块验证出现')
            input('|----是否拖动完滑块？y/n')
            self.driver.find_element(By.LINK_TEXT, '获取验证码').click()

        # 获取验证码
        print('|----开始检查验证码')
        bean = self.getAuthCode(phone)
        authcodeStr = bean['code']
        if authcodeStr == '':
            authcodeStr = input('|----请手动输入验证码：')
        print(f'|----得到验证码{authcodeStr}')

        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入短信验证码"]').send_keys(authcodeStr)
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        time.sleep(2)
        errors = self.driver.find_elements(By.ID, 'nerror')
        if len(errors) > 0:
            print(f'|----登录失败，请手动登录 token={bean["token"]}')
            input('|----是否已手动登录？y/n')
            return 1
        else:
            print('|----登录成功')
            return 1
        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.visibility_of_element_located((By.ID, 'nerror')))
        #     # 登录失败
        # except:
        #     print('|----登录成功')

    def startTask(self, startIndex):
        # 开始运行
        print('开始运行自动脚本')
        print(f'扫描表格：一共{self.sheet.nrows}个手机号')
        for i in range(startIndex - 1, self.sheet.nrows):
            self.driver.delete_all_cookies()

            # phoneStr = self.sheet.cell(i, 0).value
            phoneStr = self.getExcelStr(i, 0)
            print(f'第{i + 1}行----{phoneStr}----操作开始')
            print('|----登录')
            state = self.loginWangYi(phoneStr)
            if state == 1:
                self.getGood()
            print('------------------------------------')
            print()


if __name__ == '__main__':
    auto = WangYiAuto()
    auto.startTask(1)
    # ssss = auto.getAuthCode('15687863187')
    # print(ssss)

    # sss = AuthCodeUtils().getAuthCode('15687863187')
    # print(sss)
