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

javBus = r'https://www.javbus.com'

finderPath = r'Z:\LSP\Adult Video'

file_name_list = os.listdir(finderPath)

avCodeList = []


def walkFilePath():
    for fileStr in file_name_list:
        # print(fileStr)
        tempPath = os.path.join(finderPath, fileStr);
        # print(os.path.isdir(tempPath))
        if os.path.isdir(tempPath):
            for tempFileName in os.listdir(tempPath):
                file = os.path.splitext(tempFileName)
                print(file[1])
                print(tempFileName)
            fileBean = {'path': tempPath, 'avcode': fileStr}
            avCodeList.append(fileBean)


def network(fileBean):
    url = javBus + '/' + fileBean['avcode']
    print(url)
    response = requests.get(url, headers=headers, proxies=proxies)
    urlText = response.text
    with open('./javbus_yellow.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    soup = BeautifulSoup(urlText, 'html.parser')
    a = soup.find('a', attrs={'class': 'bigImage'})
    print(javBus + a.img['src'])
    print(a.img['title'])  # 标题
    if a is None:
        return 'F'
    else:
        fileBean['piUrl'] = javBus + a.img['src']
        return javBus + a.img['src']


def savePicture(fileBean):
    imgData = requests.get(fileBean['piUrl'], headers=headers, proxies=proxies).content
    # picPath = path + os.path.sep + 'folder.jpg'
    picPath = './pic/' + fileBean['avcode'] + '.jpg'
    with open(picPath, 'wb') as fp:
        fp.write(imgData)
    return picPath


def saveNfo(fileBean):
    picPath = './pic/'+ '111.nfo'
    nfoText = '你好'
    with open(picPath, 'w',encoding='utf-8') as fp:
        fp.write(nfoText)


def doTask():
    walkFilePath()
    # for fileBean in avCodeList:
    fileBean = avCodeList[0]
    resultNet = network(fileBean)
    if 'F' in resultNet:
        fileBean['result'] = '未找到'
    else:
        fileBean['picPath'] = savePicture(fileBean)
        saveNfo(fileBean)
    print(fileBean)


if __name__ == '__main__':
    saveNfo('')
    # doTask()
    # walkFilePath()
    # network('STCV-202')
    # walkFile()
    # for fileStr in avCodeList:
    #     print(fileStr)
