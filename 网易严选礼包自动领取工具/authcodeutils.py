import re
import time
import requests


class AuthCodeUtils:


    def __init__(self):
        self.sss = ''

    urls = ['http://sms.szfangmm.com:3000/api/smslist?token=cSuZgpUdwXxqWDCypT7kWB',
            'http://sms.szfangmm.com:3000/api/smslist?token=Go6ifqmfcbKqW39g77kkZQ',
            'http://sms.szfangmm.com:3000/api/smslist?token=Hzri6aRhxM5eMoyyuXW293'
            'http://sms.szfangmm.com:3000/api/smslist?token=EsnEbw4cj8SjNEnxiyZVzE',
            'http://sms.szfangmm.com:3000/api/smslist?token=ATCd4fakvTSzzovJfjcRGJ',
            'http://sms.szfangmm.com:3000/api/smslist?token=95LUogpdxV2k9FnYpdWBcG',
            'http://sms.szfangmm.com:3000/api/smslist?token=UaoKiHcARvzuEvmSYJSa6c']

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': ''
        # 'cookie':'rr=https%3A%2F%2Fcn1.at101.design%2F; iadult=1; hello=1; __cf_bm=p5gOpquFCoj5a8TQG4EXkJgz3Ex7FnsYEfEnocDLOvQ-1672239337-0-Aald4rPN3hah3kmMughmjJnSoAXumWxycfq63F5ZGSO30pHcwtAbqaAZLHGXuYc6q8I0nZgdiJR75WSZ20zsF7Fd02vMkSA7GKGU+aEdw5fSL4rGkP3QLsGEgxf04R5AkhrkKQTrbTGgNWCpGXKzTss=; XSRF-TOKEN=eyJpdiI6ImZObDlvclwvZjN4SnhtMHNyb2NkcTNBPT0iLCJ2YWx1ZSI6InlqNUp4V3dSN2ZucDZYN2h0OExBT2NBMlVFZVpVWXNSUTZuR1NvbVMwMlZhVVJJTDhLNTBnTHIrQUFrNTJJVDIiLCJtYWMiOiI2OGFmNDM5NzE5MDc5ZGFjMTJmODJmYjZkMTVkNWViOGI0YWUyN2JlZjUwZjg2YzEyOTVjZTVjNmZkNmE5NTYzIn0%3D; miao_ss=eyJpdiI6IlZUczhoMFJjN2VhUlRFYis1NXBYZ3c9PSIsInZhbHVlIjoiR2RWRDZncElnemNZa0poTnhGbHNcL1ZoTmlnVDhhNndYcVgxSHFTMCtcL3VnbUVZTXAyWGtCclloaURQR2dwMXVaIiwibWFjIjoiZjBlM2QzZDRjM2FmNzhmZjBmNjliMzgzNGI4NTZiZWEzZmY2MDg5YmJhZDBmNjI5NzJmYzcxMDc0OWNmN2U5YyJ9'
    }

    def requestNet(self, url, proxies=None):
        return requests.get(url, headers=self.headers, proxies=proxies, verify=False)

    # 登录使用
    def getAuthCode(self, phone):
        for i in range(10):
            time.sleep(1)
            for urlStr in self.urls:
                response = self.requestNet(urlStr)
                jsons = response.json()
                for json in jsons:
                    content = json['content']
                    if ('验证码' in content) & (phone[-4:] == json['simnum'][-4:]):
                        authcodecc = ('0000' + str(re.search(r'[1-9]\d*', content).group()))[-6:]
                        return authcodecc

