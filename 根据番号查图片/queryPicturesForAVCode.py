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

javLibrary = r'https://www.g64w.com/cn/'

finderPath = r'Z:\LSP\Adult Video'

file_name_list = os.listdir(finderPath)

avCodeList = []


def walkFile():
    for fileStr in file_name_list:
        temFileStr = fileStr
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

        fileD = {'realfilename': temFileStr, 'filename': fileStr, 'avcode': avcode}

        avCodeList.append(fileD)


def network(avCode):
    url = javLibrary + 'vl_searchbyid.php?keyword=' + avCode
    response = requests.get(url, headers=headers)
    urlText = response.text
    with open('./yellow.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    soup = BeautifulSoup(urlText, 'html.parser')
    img = soup.find('img', attrs={'id': 'video_jacket_img'})

    if img is None:
        return 'F'
    else:
        return 'https:' + img['src']


def savePicture(picUrl, picPath):
    imgData = requests.get(picUrl, headers=headers).content
    tempPicPath = picPath + '\\folder.jpg'
    with open(tempPicPath, 'wb') as fp:
        fp.write(imgData)
    return picPath


def moveFile(avCodeBean):
    tempPath = finderPath + os.path.sep + avCodeBean['avcode']
    if os.path.exists(tempPath) is False:
        os.mkdir(tempPath)
        avCodeBean['dir'] = '文件夹创建成功'
    # tempfinderPath = os.path.join(finderPath, avCodeBean['realfilename'])
    # resultfinderPath = os.path.join(tempPath, avCodeBean['realfilename'])
    # with open(tempfinderPath,'rb') as rstream:
    #     container = rstream.read()
    #     with open(resultfinderPath,'wb') as wstream:
    #         wstream.write(container)
    return tempPath


def doTask():
    walkFile()
    print('文件有：', len(avCodeList))
    for avCodeBean in avCodeList:
        print('------------------开始：' + avCodeBean['filename'])
        picUrl = network(avCodeBean['avcode'])
        if 'F' in picUrl:
            avCodeBean['result'] = '未找到'
            print('------------------------未找到')
        else:
            avCodeBean['result'] = savePicture(picUrl, moveFile(avCodeBean))
        print('------------------结束：' + avCodeBean['filename'])
    print('------------------完成------------------')


if __name__ == '__main__':
    doTask()
    # walkFile()
    for fileStr in avCodeList:
        print(fileStr)
    # os.system(r'copy Z:\LSP\Adult Video\CAWD-386C.mp4 Z:\LSP\Adult Video\CAWD-386\\')
