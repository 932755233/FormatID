# 导入os模块
import os
import requests
from bs4 import BeautifulSoup

proxy = '192.168.3.220:7890'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9'
}

javBus = r'https://www.javbus.com/'

finderPath = r'Z:\LSP\Adult Video'

file_name_list = os.listdir(finderPath)

avCodeList = []


def walkFile():
    for fileStr in file_name_list:
        if (fileStr[-3:] == 'jpg') | (fileStr[-3:] == 'JPG'):
            continue
        if fileStr[-2:] == 'db':
            continue
        if (fileStr[-3:] == 'mp4') | (fileStr[-3:] == 'MP4'):
            fileStr = fileStr[:-4]
        if (fileStr[-3:] == 'avi') | (fileStr[-3:] == 'AVI'):
            fileStr = fileStr[:-4]
        avcode = fileStr
        if avcode[-1] == 'C':
            avcode = avcode[:-1]
        if avcode[-1] == '-':
            avcode = avcode[:-1]
        if avcode.find(' ') != -1:
            avcode = avcode[:avcode.find(' ')]

        fileD = {'filename': fileStr, 'avcode': avcode}

        avCodeList.append(fileD)


def network(avCode):
    url = javBus + avCode
    print(url)
    response = requests.get(url, headers=headers, proxies=proxies)
    urlText = response.text
    with open('./yellow.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    soup = BeautifulSoup(urlText, 'html.parser')
    a = soup.find('a', attrs={'class': 'bigImage'})
    print(javBus + a.img['src'])
    print(a.img['title'])
    if a is None:
        return 'F'
    else:
        return javBus + a.img['src']


def savePicture(picUrl, picName):
    imgData = requests.get(picUrl, headers=headers).content
    picPath = finderPath + '\\' + picName + '-poster.jpg'
    with open(picPath, 'wb') as fp:
        fp.write(imgData)
    return picPath


def doTask():
    walkFile()
    print('文件有：', len(avCodeList))
    for fileStr in avCodeList:
        print('------------------开始：' + fileStr['filename'])
        picUrl = network(fileStr['avcode'])
        if 'F' in picUrl:
            fileStr['result'] = '未找到'
            print('------------------------未找到')
        else:
            fileStr['result'] = savePicture(picUrl, fileStr['filename'])
        print('------------------结束：' + fileStr['filename'])
    print('------------------完成------------------')


if __name__ == '__main__':
    # doTask()
    # walkFile()
    network('STCV-202')
    for fileStr in avCodeList:
        print(fileStr)
