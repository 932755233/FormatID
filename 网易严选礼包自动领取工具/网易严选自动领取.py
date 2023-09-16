import time
import random

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re

from xlutils.copy import copy
import xlrd
import requests
from AuthCodeUtils import AuthCodeUtils


class WangYiAuto:
    tokens = ['q9MzMbNpuQ8VLMRGasboT8']

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"]

    def requestNet(self, url, cookies, proxies=None):
        return requests.get(url, headers=self.headers, cookies=cookies, proxies=proxies, verify=False)

    def __init__(self):
        # 网络请求
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Length': '0',
            'Content-Type': 'application/json',
            'Origin': 'https://act.you.163.com',
            'Referer': 'https://act.you.163.com/act/pub/ssr/e1V6SZYyeqXU.html?from=plan11BBC1E590A50EDDplan&channel_type=1',
            'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Connection': 'keep-alive',
            'Cookie': ''
            # 'cookie':'rr=https%3A%2F%2Fcn1.at101.design%2F; iadult=1; hello=1; __cf_bm=p5gOpquFCoj5a8TQG4EXkJgz3Ex7FnsYEfEnocDLOvQ-1672239337-0-Aald4rPN3hah3kmMughmjJnSoAXumWxycfq63F5ZGSO30pHcwtAbqaAZLHGXuYc6q8I0nZgdiJR75WSZ20zsF7Fd02vMkSA7GKGU+aEdw5fSL4rGkP3QLsGEgxf04R5AkhrkKQTrbTGgNWCpGXKzTss=; XSRF-TOKEN=eyJpdiI6ImZObDlvclwvZjN4SnhtMHNyb2NkcTNBPT0iLCJ2YWx1ZSI6InlqNUp4V3dSN2ZucDZYN2h0OExBT2NBMlVFZVpVWXNSUTZuR1NvbVMwMlZhVVJJTDhLNTBnTHIrQUFrNTJJVDIiLCJtYWMiOiI2OGFmNDM5NzE5MDc5ZGFjMTJmODJmYjZkMTVkNWViOGI0YWUyN2JlZjUwZjg2YzEyOTVjZTVjNmZkNmE5NTYzIn0%3D; miao_ss=eyJpdiI6IlZUczhoMFJjN2VhUlRFYis1NXBYZ3c9PSIsInZhbHVlIjoiR2RWRDZncElnemNZa0poTnhGbHNcL1ZoTmlnVDhhNndYcVgxSHFTMCtcL3VnbUVZTXAyWGtCclloaURQR2dwMXVaIiwibWFjIjoiZjBlM2QzZDRjM2FmNzhmZjBmNjliMzgzNGI4NTZiZWEzZmY2MDg5YmJhZDBmNjI5NzJmYzcxMDc0OWNmN2U5YyJ9'
        }
        # 解析excel表格
        self.excelPath = r'C:\Users\Danny\Desktop\网易严选自动领取账号.xls'
        self.workbook = xlrd.open_workbook(self.excelPath)  # 打开Excel
        self.sheet = self.workbook.sheets()[0]
        self.rows = self.sheet.nrows

        self.authCodeUtils = AuthCodeUtils()
        self.authCodeUtils.tokens = self.tokens

        self.loginUrl = 'https://m.you.163.com/u/login'

        self.checkLoginUrl = 'https://act.you.163.com/act/napi/forwardMobile/xhr/common/checklogin.json'
        self.getGoodsUrl = 'https://act.you.163.com/napi/aielx/inner/activity/user/limit'
        self.getGoodsInfoUrl = 'https://act.you.163.com/napi/aielx/inner/v2/getComplexWelfareNoMobile'

        self.chrome_options = Options()
        self.chrome_options.add_argument('--incognito')

        # self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    def getExcelStr(self, row, col):
        cell = self.sheet.cell(row, col)
        if cell.ctype == 2:
            return str(int(cell.value))
        else:
            return cell.value

    def getGood(self):
        self.driver.get(self.getGoodUrl)
        self.driver.find_element(By.CLASS_NAME, 'u-ADAB8E-button-image').click()
        time.sleep(2)

    # 登录使用
    def getAuthCode(self, phone):
        print(f'|----等待查询{phone}的验证码')
        time.sleep(8)
        for i in range(10):
            time.sleep(1)
            bean = self.authCodeUtils.getAuthCodeForTag(phone, '网易')
            if bean['status'] == '1':
                return bean
        return bean

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
        if authcodeStr == '未找到':
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

    def checkLogin(self):
        pass

    def random_ip(self):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        d = random.randint(1, 255)
        return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))

    def startTask(self, startIndex):
        new_workbook = copy(self.workbook)
        new_sheet = new_workbook.get_sheet(0)

        # 开始运行
        print('开始运行自动脚本')
        print(f'扫描表格：一共{self.sheet.nrows}个手机号')
        for i in range(startIndex - 1, self.sheet.nrows):
            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.driver.delete_all_cookies()

            # phoneStr = self.sheet.cell(i, 0).value
            phoneStr = self.getExcelStr(i, 0)
            print(f'第{i + 1}行----{phoneStr}----操作开始')
            print('|----登录')
            state = self.loginWangYi(phoneStr)
            if state == 1:
                # 登录成功拿cookie
                cookies = self.driver.get_cookies();

                self.headers['User-Agent'] = random.choice(self.user_agent_list)
                self.headers['X-Forwarded-For'] = self.random_ip()

                message = ''
                csrfToken = self.driver.get_cookie('yx_csrf')['value']
                self.driver.quit()
                print('|----拿到Token：' + csrfToken)
                cookiesStrs = '; '.join(item for item in [item["name"] + "=" + item['value'] for item in cookies])
                self.headers['Cookie'] = cookiesStrs
                # cookiesStr = dict(cookies_are=cookiesStrs)
                # print(cookiesStr)
                times = int(time.time() * 1000)
                urlStr = self.checkLoginUrl + '?csrf_token=' + csrfToken + '&__timestamp=' + str(times)
                print('|----调用网易严选验证登录接口')
                s = requests.session()
                response = s.get(url=urlStr, headers=self.headers)
                print('|------网易严选验证登录接口:' + response.text)
                jsons = response.json()
                if jsons['code'] == '200':
                    print('|----获取礼品前的验证登录成功')
                else:
                    print('|----获取礼品前的验证登录失败')
                    input('暂停')
                # 抽取礼品POST
                self.headers['Content-Length'] = '110'
                jsonStr = '{"token":"54ddbb5cc36d45f4a06ec33eee748388","outParam":{"from":"plan11BBC1E590A50EDDplan","channel_type":"1"}}'
                print('|----调用网易严选抽取礼品接口')
                responseGoods = s.post(url=self.getGoodsUrl + '?csrf_token=' + csrfToken, headers=self.headers,
                                              data=jsonStr)
                print('|------网易严选抽取礼品接口:' + responseGoods.text)
                goodsJson = responseGoods.json()
                if goodsJson['data']['quota'] == 0:
                    print('|----当前账号没有兑换次数')
                    input('暂停')
                print('|----调用网易严选礼品信息接口')
                responseGoodsInfo = s.post(url=self.getGoodsInfoUrl + '?csrf_token=' + csrfToken,
                                                  headers=self.headers,
                                                  data=jsonStr)
                print('|------网易严选抽取礼品信息接口:' + responseGoodsInfo.text)
                goodsInfoJson = responseGoodsInfo.json()
                print(f'|----手机号：{phoneStr}----获得的礼品：{goodsInfoJson["data"]["material"]["popupTitle"]}')
                print('|----保存信息到Excel。。。')
                new_sheet.write(i, 1, goodsInfoJson["data"]["material"]["popupTitle"])
                new_sheet.write(i, 2, message)
                new_sheet.write(i, 3, cookiesStrs)
                new_workbook.save(r'C:\Users\Danny\Desktop\网易严选自动领取账号.xls')
                print('|----保存信息到Excel完毕')
                self.headers['Cookie'] = ''
                s.close()
                print('--------------------------------------')
                print('等待10秒')
                time.sleep(10)


if __name__ == '__main__':
    auto = WangYiAuto()
    auto.startTask(24)
    # ssss = auto.getAuthCode('15687863187')
    # print(ssss)

    # sss = AuthCodeUtils().getAuthCode('15687863187')
    # print(sss)
