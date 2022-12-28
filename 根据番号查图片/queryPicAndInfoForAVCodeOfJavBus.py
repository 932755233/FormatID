# 导入os模块
import os
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from PIL import Image

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

videoTypeYuanZu = ('.mp4', '.rm', '.rmvb', '.avi')

pattern = re.compile(r'[a-z]{2,7}-[0-9]{1,5}', re.I)

javBus = r'https://www.javbus.com'

# finderPath = r'Z:\LSP\AdultVideo'
finderPath = r'Z:\LSP\测试'

file_name_list = os.listdir(finderPath)

avCodeList = []


# 获取本地文件bean
def walkFilePath():
    for fileStr in file_name_list:
        # print(fileStr)
        tempPath = os.path.join(finderPath, fileStr);
        # print(os.path.isdir(tempPath))
        if os.path.isdir(tempPath):
            fileBean = {'path': tempPath, 'avcode': fenliavcode(fileStr)}
            if os.path.exists(os.path.join(tempPath, 'SampleImage')):
                continue
            for tempFileName in os.listdir(tempPath):
                file = os.path.splitext(tempFileName)
                if isvideo(file[1]):
                    fileBean['filename'] = file[0]
                # print(tempFileName)
            avCodeList.append(fileBean)


# 获取AVcode
def fenliavcode(fileName):
    return pattern.search(fileName)[0]


# 判断是否为视频文件
def isvideo(fileType):
    return fileType in videoTypeYuanZu


# 网络获取信息
def network(fileBean):
    print('  翻墙连接网络')
    url = javBus + '/' + fileBean['avcode']
    response = requests.get(url, headers=headers, proxies=proxies)
    urlText = response.text
    with open('./javbus_yellow.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    # soup = BeautifulSoup(urlText, 'html.parser')
    soup = BeautifulSoup(urlText, 'lxml')
    a = soup.find('a', attrs={'class': 'bigImage'})
    if a is None:
        return 'F'
    else:
        if 'http' == a.img['src'][0:4]:
            fileBean['picurl'] = a.img['src']
        else:
            fileBean['picurl'] = javBus + a.img['src']
        fileBean['plot'] = a.img['title']
        # fileBean['tag'] = soup.find_all('/html/body/div[5]/div[1]/div[2]/p[10]/span[1]/a')
        fileBean['genres'] = \
            re.findall(
                r'<span class="genre"><label><input type="checkbox" name="gr_sel" value="(.*?)"><a href="(.*?)">(.*?)</a></label></span>',
                urlText)
        date = re.search(r'<p><span class="header">發行日期:</span>(.*?)</p>', urlText).groups()[0]
        # 发行日期
        fileBean['faxingdate'] = re.search(r'\d{4}-\d{2}-\d{2}', date).group()
        fileBean['year'] = re.search(r'\d{4}', date).group()
        # 得到演员
        fileBean['star'] = []
        star = soup.find_all('div', attrs={'class': 'star-name'})
        for div in star:
            fileBean['star'].append(div.text)
        # 得到样品图像列表
        fileBean['imageurl'] = []
        simpleImageUrlList = soup.find_all('a', attrs={'class': 'sample-box'})
        for simpleImageUrl in simpleImageUrlList:
            fileBean['imageurl'].append(simpleImageUrl['href'])
        active = soup.find('li', attrs={'class': 'active'})
        if active is not None:
            if '有' in active.text:
                fileBean['active'] = '有码'
            else:
                fileBean['active'] = '无码'
        return 'T'


def savePicture(fileBean):
    imgData = requests.get(fileBean['picurl'], headers=headers, proxies=proxies).content
    # 以下两个路径正常图片
    picThumbPath = fileBean['path'] + os.path.sep + fileBean['filename'] + '-thumb.jpg'

    with open(picThumbPath, 'wb') as fp:
        fp.write(imgData)

    # 这个需要切一半
    picPosterPath = fileBean['path'] + os.path.sep + fileBean['filename'] + '-poster.jpg'
    img = Image.open(picThumbPath)
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    region = img.crop((w / 2, 0, w, h))
    region.save(picPosterPath)

    picFanartPath = fileBean['path'] + os.path.sep + fileBean['filename'] + '-fanart.jpg'
    with open(picFanartPath, 'wb') as fp:
        fp.write(imgData)


def saveSampleImage(fileBean):
    imgePath = os.path.join(fileBean['path'], 'SampleImage')
    Path(imgePath).mkdir(parents=True, exist_ok=True)
    # os.makedirs(os.path.dirname(imgePath), exist_ok=True)
    # if not os.path.exists(imgePath):
    #     os.makedirs(imgePath)
    index = 0
    for imageUrl in fileBean['imageurl']:
        index = index + 1

        if 'http' not in imageUrl:
            imageUrl = javBus + imageUrl

        imgData = requests.get(imageUrl, headers=headers, proxies=proxies).content
        path = imgePath + '\%s-%d.jpg' % (
            fileBean['avcode'], index)
        with open(path, 'wb') as fp:
            fp.write(imgData)
    # backdrop(fileBean)


def backdrop(fileBean):
    imgePath = fileBean['path'] + os.path.sep + 'SampleImage'
    # imgePath = 'Z:\LSP\测试\CAWD-386-C' + os.path.sep + 'SampleImage'

    imageList = []
    if len(fileBean['imageurl']) == 0:
        return
    for imageFileName in os.listdir(imgePath):
        type = os.path.splitext(imageFileName)[1]
        if type == '.db':
            continue
        imageList.append(Image.open(os.path.join(imgePath, imageFileName)))
    imageHeigh = 0
    imageWidth = 0;
    for imageBean in imageList:
        if imageBean.size[1] > imageHeigh:
            imageHeigh = imageBean.size[1]
        imageWidth = imageWidth + imageBean.size[0]

    imgTemp = Image.new('RGB', (imageWidth, imageHeigh), (0, 0, 0))
    widthTemp = 0
    for imageBean in imageList:
        imgTemp.paste(imageBean, (widthTemp, 0))
        widthTemp = imageBean.size[0] + widthTemp

    imgTemp.save(fileBean['path'] + os.path.sep + 'backdrop.jpg')
    imgTemp.save(fileBean['path'] + os.path.sep + 'banner.jpg')


def saveNfo(fileBean):
    picPath = fileBean['path'] + os.path.sep + fileBean['filename'] + '.nfo'
    nfoText = '''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<movie>
 <plot>%s</plot>
 <lockdata>false</lockdata>
 <dateadded>2022-12-24 00:00:00</dateadded>
 <year>%s</year>
 <premiered>%s</premiered>
 <releasedate>%s</releasedate>\n''' % (
        fileBean['plot'], fileBean['year'], fileBean['faxingdate'], fileBean['faxingdate'])
    if fileBean['active'] is not None and len(fileBean['active']) > 0:
        nfoText += ' <genre>%s</genre>\n' % fileBean['active']
    for genres in fileBean['genres']:
        nfoText += ' <genre>%s</genre>\n' % genres[2]
    for star in fileBean['star']:
        nfoText += ''' <tag></tag>
 <actor>
  <name>%s</name>
  <role>AV女优</role>
  <type>Actor</type>
 </actor>\n''' % star
    nfoText += '''</movie>'''
    with open(picPath, 'w', encoding='utf-8') as fp:
        fp.write(nfoText)


def doTask():
    walkFilePath()
    print('拿到番号列表：')
    print()
    for fileBean in avCodeList:
        print(fileBean['avcode'], end=',')
    print()
    print()
    sum = len(avCodeList)
    print('------开始查询，一共%d个------' % sum)
    index = 1
    for fileBean in avCodeList:
        print('---%d/%d---查询：%s------' % (index, sum, fileBean['avcode']))
        if 'F' == network(fileBean):
            fileBean['result'] = '未找到'
            print('  未找到！')
            print('--------------------')
        else:
            genres = ''
            for tag in fileBean['genres']:
                genres += '%s,' % tag[2]
            stars = ''
            for star in fileBean['star']:
                stars += '%s,' % star
            print('''  信息展示：
  内容概述：%s
  发行年份：%s
  发行日期：%s
  是否有码：%s
  风格：%s
  演员：%s
            ''' % (
                fileBean['plot'], fileBean['year'], fileBean['faxingdate'], fileBean['active'], genres[:-1], stars[:-1]))
            print('  保存NFO信息')
            saveNfo(fileBean)
            print('  保存封面')
            savePicture(fileBean)
            print('  保存样本图像')
            saveSampleImage(fileBean)
            print('--------------------')
            index = index + 1

    # fileBean = avCodeList[0]

    # print(fileBean)

    # for fileBean in avCodeList:
    # fileBean = avCodeList[0]
    # resultNet = network(fileBean)
    # if 'F' in resultNet:
    #     fileBean['result'] = '未找到'
    # else:
    #     fileBean['picPath'] = savePicture(fileBean)
    #     saveNfo(fileBean)
    # print(fileBean)


if __name__ == '__main__':
    doTask()
    # backdrop('')
    # translate_Japanese('123')
    # savePicture('')
    # walkFilePath()
    # print(avCodeList)
    # saveNfo('')
    # doTask()
    # walkFilePath()
    # network('STCV-202')
    # walkFile()
    # for fileStr in avCodeList:
    #     print(fileStr)
    # index = 0
    # for i in range(9):
    #     index = index + 25
    #     next_url = f'https://movie.douban.com/top250?start=%d&amp;filter='%index
    #     print(next_url)
