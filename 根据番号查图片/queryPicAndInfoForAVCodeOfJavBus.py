# 导入os模块
import zhconv
import os
import re
import sys
import shutil
import time
import urllib3
import lxml
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from PIL import Image
from requests.exceptions import SSLError

from 根据番号查图片 import deleteSampleImage

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

now_date = time.strftime("%Y-%m-%d", time.localtime())

proxy = '192.168.5.111:7890'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': ''
    # 'cookie':'rr=https%3A%2F%2Fcn1.at101.design%2F; iadult=1; hello=1; __cf_bm=p5gOpquFCoj5a8TQG4EXkJgz3Ex7FnsYEfEnocDLOvQ-1672239337-0-Aald4rPN3hah3kmMughmjJnSoAXumWxycfq63F5ZGSO30pHcwtAbqaAZLHGXuYc6q8I0nZgdiJR75WSZ20zsF7Fd02vMkSA7GKGU+aEdw5fSL4rGkP3QLsGEgxf04R5AkhrkKQTrbTGgNWCpGXKzTss=; XSRF-TOKEN=eyJpdiI6ImZObDlvclwvZjN4SnhtMHNyb2NkcTNBPT0iLCJ2YWx1ZSI6InlqNUp4V3dSN2ZucDZYN2h0OExBT2NBMlVFZVpVWXNSUTZuR1NvbVMwMlZhVVJJTDhLNTBnTHIrQUFrNTJJVDIiLCJtYWMiOiI2OGFmNDM5NzE5MDc5ZGFjMTJmODJmYjZkMTVkNWViOGI0YWUyN2JlZjUwZjg2YzEyOTVjZTVjNmZkNmE5NTYzIn0%3D; miao_ss=eyJpdiI6IlZUczhoMFJjN2VhUlRFYis1NXBYZ3c9PSIsInZhbHVlIjoiR2RWRDZncElnemNZa0poTnhGbHNcL1ZoTmlnVDhhNndYcVgxSHFTMCtcL3VnbUVZTXAyWGtCclloaURQR2dwMXVaIiwibWFjIjoiZjBlM2QzZDRjM2FmNzhmZjBmNjliMzgzNGI4NTZiZWEzZmY2MDg5YmJhZDBmNjI5NzJmYzcxMDc0OWNmN2U5YyJ9'
}

videoTypeYuanZu = ('.mp4')

pattern = re.compile(r'([0-9]{1,4})?[a-z]{2,8}-[a-z0-9]{1,7}', re.I)
haveSubtitlePattern = re.compile(r'.*?-.*?-C', re.I)
notfound = re.compile(r'404 Page Not Found!', re.I)

javBus = r'https://www.javbus.com'

# javhd101 = r'https://avhd101.com/search?q='
javhd101 = r'https://avhd101.com/'
javLibrary = r'https://www.i71t.com/tw/'
javDB = r'https://javdb.com/'

subtitlePath = r'H:\AV的文件\字幕\7000字幕'
subtitleType = ['chi', 'jpn', 'eng', 'arm', 'kor', 'ita', 'fre', 'fus']

avCodeList = []


def requestNet(url, proxies=None):
    return requests.get(url, headers=headers, proxies=proxies, verify=False)


# 获取本地文件bean
def walkFilePath(finderPath):
    for fileStr in os.listdir(finderPath):
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
                    fileBean['havesubtitle'] = haveSubtitlePattern.match(file[0]) != None
            avCodeList.append(fileBean)


# 获取AVcode
def fenliavcode(fileName):
    rere = pattern.search(fileName)
    if rere == None:
        return fileName
    else:
        return rere[0]


# 判断是否为视频文件
def isvideo(fileType):
    return fileType in videoTypeYuanZu


# 网络获取信息
def networkJavBus(fileBean):
    print('  连接JavBus')
    url = javBus + '/' + fileBean['avcode']
    response = requestNet(url, proxies=proxies)
    urlText = response.text
    with open('./javbus_yellow.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    # soup = BeautifulSoup(urlText, 'html.parser')
    soup = BeautifulSoup(urlText, 'lxml')
    a = soup.find('a', attrs={'class': 'bigImage'})
    if a is None:
        notf = re.search(notfound, urlText)
        if notf is None:
            print('    连接JavBus失败')
            sys.exit()
        return 'F'
    else:
        # sys.exit()
        print('    封面图url')
        if 'http' == a.img['src'][0:4]:
            fileBean['picurl'] = a.img['src']
        else:
            fileBean['picurl'] = javBus + a.img['src']
        print('    内容概述')
        fileBean['plot'] = a.img['title']
        fileBean['title'] = fileBean['filename'] + a.img['title']
        # fileBean['tag'] = soup.find_all('/html/body/div[5]/div[1]/div[2]/p[10]/span[1]/a')
        fileBean['genres'] = []
        genres = re.findall(
            r'<span class="genre"><label><input type="checkbox" name="gr_sel" value="(.*?)"><a href="(.*?)">(.*?)</a></label></span>',
            urlText)
        print('    风格')
        for genre in genres:
            fileBean['genres'].append(genre[2])
        date = re.search(r'<p><span class="header">發行日期:</span>(.*?)</p>', urlText).groups()[0]
        # 发行日期
        print('    发行日期')
        fileBean['faxingdate'] = re.search(r'\d{4}-\d{2}-\d{2}', date).group()
        fileBean['year'] = re.search(r'\d{4}', date).group()
        # 得到演员
        print('    演员')
        fileBean['star'] = []
        star = soup.find_all('div', attrs={'class': 'star-name'})
        for div in star:
            fileBean['star'].append(div.text)
        # 得到样品图像列表
        print('    样品图像列表')
        fileBean['imageurl'] = []
        simpleImageUrlList = soup.find_all('a', attrs={'class': 'sample-box'})
        for simpleImageUrl in simpleImageUrlList:
            fileBean['imageurl'].append(simpleImageUrl['href'])
        print('    有码/无码')
        active = soup.find('li', attrs={'class': 'active'})
        if active is not None:
            if '有' in active.text:
                fileBean['active'] = '有码'
            else:
                fileBean['active'] = '无码'
        return 'T'


# 从Avhd101拿中文一句话标题
def networkAVHD(fileBean):
    print('  连接Avhd101')
    headers['cookie'] = 'iadult=1'
    url = javhd101 + 'search?q=' + fileBean['avcode']
    response = requestNet(url, proxies=proxies)
    urlText = response.text
    with open('./avhd_yellow2.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    if 'This page has been removed' in urlText:
        print('    This page has been removed')
        sys.exit()
        print('    %s出现问题' % fileBean['avcode'])

    soup = BeautifulSoup(urlText, 'lxml')
    section = soup.find('section')
    if section is None:
        print('    未找到信息')
        return

    # title = re.search('title="(.*?)"', section.prettify()).groups()[0]
    h3 = section.find('h3')
    # print('------%s'%h3.text)
    # title = re.search('">(.*?)<mark>', h3.text).groups()[0]
    a = h3.find('a')
    # 去掉a标签里面的mark标签
    [s.extract() for s in a(['mark'])]
    fileBean['title'] = fileBean['filename'] + a.text.strip()
    fileBean['plot'] = '%s------%s' % (fileBean['plot'], a.text.strip())
    headers['cookie'] = ''
    print('    一句中文概述')


# 从JavLibrary获取中文评论
def networkJavLibrary(fileBean):
    print('  连接JavLibrary')
    url = javLibrary + 'vl_searchbyid.php?keyword=' + fileBean['avcode']
    response = requestNet(url)
    urlText = response.text
    with open('./javlibrary_yellow.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    soup = BeautifulSoup(urlText, 'html.parser')
    # 类别 fileBean['genres']
    genres = soup.find_all('a', attrs={'rel': 'category tag'})
    if len(genres) > 0:
        print('    类别替换')
        fileBean['genres'] = []
        for genre in genres:
            fileBean['genres'].append(genre.text)
    else:
        print('    无类别替换，翻译类别')
        genres = []
        for genre in fileBean['genres']:
            temp = zhconv.convert(genre, 'zh-cn')
            genres.append(temp)
        fileBean['genres'] = genres
    # 得到演员
    stars = soup.find_all('span', attrs={'class': 'star'})
    if len(stars) > 0:
        print('    演员替换')
        fileBean['star'] = []
        for star in stars:
            fileBean['star'].append(star.text)
    else:
        print('    无演员替换')
    # 使用者评价
    score = soup.find('span', attrs={'class': 'score'})
    if score is None:
        print('    无评分')
        fileBean['rating'] = ''
    else:
        print('    有评分')
        fileBean['rating'] = score.text[1:-1]
    # 评论
    textareas = soup.find_all('textarea', attrs={'class': 'hidden'})
    if textareas is None:
        return
        print('    无评论')
    textareasStr = ''
    for textarea in textareas:
        if is_chinese(textarea.text):
            textareaStr = re.compile('\[.*?\]').sub('', textarea.text)
            textareaStr = re.compile('\n').sub('。', textareaStr)
            textareasStr = '%s------%s' % (textareasStr, textareaStr)
    if len(textareasStr) > 0:
        print('    评论')
        fileBean['plot'] = '%s------[[[javlibrary评论]]]%s' % (fileBean['plot'], textareasStr)
    else:
        print('    无评论')


def networkJavDB(fileBean):
    print('   连接JavDB')
    # 提前初始化防止报错
    fileBean['video'] = '无'
    # fileBean['avcode']='DLDSS-156'
    url = '%ssearch?q=%s&f=all' % (javDB, fileBean['avcode'])
    urlText = requestNet(url, proxies=proxies).text
    with open('./javdb_yellow.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    soup = BeautifulSoup(urlText, 'html.parser')
    div = soup.find_all('div', attrs={'class': 'item'})
    if div is None:
        print('    未找到作品介绍视频')
        return
    strong = div[0].find('strong')
    if strong.text == fileBean['avcode']:
        nextpageUrl = div[0].find('a')['href']
        javDBDetail(fileBean, nextpageUrl)
    else:
        print('    未找到作品介绍视频')


def javDBDetail(fileBean, nextpageUrl):
    url = javDB + nextpageUrl
    urlText = requestNet(url, proxies=proxies).text
    with open('./javdb_detail_yellow.html', 'w', encoding='utf-8') as fp:
        fp.write(urlText)
    soup = BeautifulSoup(urlText, 'html.parser')
    source = soup.find('source', attrs={'type': 'video/mp4'})
    if source is None:
        print('    无作品介绍')
        return
    if source['src'] == '':
        print('    无作品介绍')
        return
    print('    作品介绍')
    if source['src'][:4] == 'http':
        fileBean['video'] = source['src']
    else:
        fileBean['video'] = 'http://%s' % source['src'][2:]


def is_chinese(string):
    tempTrue = []
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            tempTrue.append(True)
    if len(tempTrue) > len(string) / 3:
        return True
    else:
        return False


def savePicture(fileBean):
    imgData = requestNet(fileBean['picurl'], proxies=proxies).content
    # 以下两个路径正常图片
    picThumbPath = fileBean['path'] + os.path.sep + fileBean['filename'] + '-thumb.jpg'

    with open(picThumbPath, 'wb') as fp:
        fp.write(imgData)
        print('    thumb.jpg')

    # 这个需要切一半
    picPosterPath = fileBean['path'] + os.path.sep + fileBean['filename'] + '-poster.jpg'
    img = Image.open(picThumbPath)
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    region = img.crop((w / 2, 0, w, h))
    region.save(picPosterPath)
    print('    poster.jpg')

    picFanartPath = fileBean['path'] + os.path.sep + fileBean['filename'] + '-fanart.jpg'
    with open(picFanartPath, 'wb') as fp:
        fp.write(imgData)
        print('    fanart.jpg')

    folderPath = fileBean['path'] + os.path.sep + 'folder.jpg'
    if os.path.exists(folderPath):
        os.remove(folderPath)
        print('    删除folder.jpg文件')


def saveSampleImage(fileBean):
    imgePath = os.path.join(fileBean['path'], 'SampleImage')
    Path(imgePath).mkdir(parents=True, exist_ok=True)
    # os.makedirs(os.path.dirname(imgePath), exist_ok=True)
    # if not os.path.exists(imgePath):
    #     os.makedirs(imgePath)
    index = 0
    if len(fileBean['imageurl']) > 0:
        print('    %d张' % len(fileBean['imageurl']))
        print('    ', end='')
        for imageUrl in fileBean['imageurl']:
            index = index + 1
            if 'http' not in imageUrl:
                imageUrl = javBus + imageUrl
                tempProxies = proxies
                print('添加javbus头的', end='')
            else:
                tempProxies = None
            try:
                imgData = requestNet(imageUrl, proxies=tempProxies).content
            except:
                print()
                print('    %s样本图像下载问题，url：%s' % (fileBean['avcode'], imageUrl))
                deleteSampleImage.deleteOne(fileBean['path'])
                print('    %s删除SampleImage文件夹' % fileBean['avcode'])
                sys.exit()
            path = imgePath + '\%s-%d.jpg' % (
                fileBean['avcode'], index)
            with open(path, 'wb') as fp:
                fp.write(imgData)
                print('第%d张' % index, end=' ')
    else:
        print('    无样本图像', end='')
    print()
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


def formatNfo(fileBean):
    nfoText = '''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<movie>
 <plot>%s</plot>
 <lockdata>false</lockdata>
 <dateadded>%s</dateadded>
 <title>%s</title>
 <year>%s</year>
 <premiered>%s</premiered>
 <releasedate>%s</releasedate>
 <rating>%s</rating>\n''' % (
        fileBean['plot'], now_date, fileBean['title'], fileBean['year'], fileBean['faxingdate'], fileBean['faxingdate'],
        fileBean['rating'])
    if fileBean['active'] is not None and len(fileBean['active']) > 0:
        nfoText += ' <genre>%s</genre>\n' % fileBean['active']
    for genre in fileBean['genres']:
        nfoText += ' <genre>%s</genre>\n' % genre
    for star in fileBean['star']:
        nfoText += ''' <actor>
  <name>%s</name>
  <role>AV女优</role>
  <type>Actor</type>
 </actor>\n''' % star
    nfoText += '''</movie>'''
    fileBean['nfotext'] = nfoText


def saveNfo(fileBean):
    picPath = fileBean['path'] + os.path.sep + fileBean['filename'] + '.nfo'
    with open(picPath, 'w', encoding='utf-8') as fp:
        fp.write(fileBean['nfotext'])


def saveVideo(fileBean):
    videoPath = fileBean['path'] + os.path.sep + fileBean['videoname']

    if '无' == fileBean['video']:
        print('    无网络视频')
        if searchType == 1:
            print('      复制替代视频')
            shutil.copyfile('./wuyugao.mp4', videoPath)

        return
    videoData = requestNet(fileBean['video']).content
    videoPath = fileBean['path'] + os.path.sep + fileBean['videoname']
    with open(videoPath, 'ab') as f:
        f.write(videoData)
        print('    视频保存')


def walksubtitleFilePath(subtitlePath):
    avcodeSet = []
    for filename in os.listdir(subtitlePath):
        # print(filename)
        avcodeRe = re.search('([a-zA-Z]{2,5}-[a-zA-Z0-9]{2,5})', filename)
        # avcode = re.search('PPPD-688(.*?)',filename) 反查文件，有同番号多文件情况
        if avcodeRe is not None:
            avcode = avcodeRe.group()
            if os.path.isdir(os.path.join(subtitlePath + os.path.sep + 'result', '%s-C' % avcode)):
                continue
            avcodeSet.append(avcode)
    avcodeSet = sorted(list(set(avcodeSet)), key=avcodeSet.index)
    for avcode in avcodeSet:
        fileBean = {}
        fileBean['avcode'] = avcode
        fileBean['filename'] = '%s-C' % avcode
        fileBean['basalpath'] = subtitlePath
        fileBean['path'] = os.path.join(subtitlePath + os.path.sep + 'result', fileBean['filename']);
        fileBean['havesubtitle'] = False
        avCodeList.append(fileBean)
    return 1


def findSubtitleFile(fileBean):
    fileList = []
    for filename in os.listdir(subtitlePath):
        filenametemp = re.search('%s(.+)' % fileBean['avcode'], filename)
        if filenametemp is not None:
            file = filenametemp.group()
            if os.path.isfile(os.path.join(subtitlePath, file)):
                fileList.append(file)
    return fileList


def copySubtitleFile(type, fileBean):
    fileList = findSubtitleFile(fileBean)
    if len(fileList) > 0:
        print('    %s个字幕文件' % len(fileList))
    else:
        print('    无字幕文件')
        if fileBean['havesubtitle']:
            oldPath = r'./subtitle_simple.srt'
            newfilename = r'%s.zul.srt' % fileBean['filename']
            newPath = os.path.join(fileBean['path'], newfilename)
            shutil.copyfile(oldPath, newPath)
            print('      字幕标志文件')
    index = 0
    for filename in fileList:
        oldPath = os.path.join(subtitlePath, filename)
        if type == 1:
            newfilename = '%s.%s%s' % (fileBean['filename'], subtitleType[index], os.path.splitext(filename)[1])
            newPath = os.path.join(fileBean['path'], newfilename)
        else:
            newTempPath = os.path.join(fileBean['basalpath'], '未找到')
            Path(newTempPath).mkdir(parents=True, exist_ok=True)
            newPath = os.path.join(newTempPath, filename)
        shutil.copyfile(oldPath, newPath)
        index = index + 1

# 0为黑群晖av文件夹
# 1为字幕文件夹
searchType = 0


def doTask():
    finderPath = r'X:\LSP\AdultVideo'
    # finderPath = r'Z:\LSP\测试'
    subtitlePath = r'H:\AV的文件\字幕\7000字幕'
    # subtitlePath = r'H:\新建文件夹 (2)\湿巾\字幕\测试'

    if searchType == 0:
        # 获取群辉AV文件夹中的番号与文件路径
        walkFilePath(finderPath)
    else:
        # 获取字幕文件列表
        walksubtitleFilePath(subtitlePath)

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
        if 'F' == networkJavBus(fileBean):
            fileBean['result'] = '未找到'
            print('  未找到！')
            if searchType == 1:
                print('  复制字幕文件到未找到')
                copySubtitleFile(0, fileBean)
            elif searchType == 0:
                imgePath = os.path.join(fileBean['path'], 'SampleImage')
                Path(imgePath).mkdir(parents=True, exist_ok=True)
            print('--------------------')
        else:
            networkAVHD(fileBean)
            networkJavLibrary(fileBean)
            networkJavDB(fileBean)
            genres = ''
            for tag in fileBean['genres']:
                genres += '%s,' % tag
            stars = ''
            for star in fileBean['star']:
                stars += '%s,' % star
            print('''  信息展示：
  标题：%s
  内容概述：%s
  发行年份：%s
  发行日期：%s
  是否有码：%s
  评分：%s
  风格：%s
  演员：%s
  作品介绍视频链接：%s
            ''' % (
                fileBean['title'], fileBean['plot'], fileBean['year'], fileBean['faxingdate'], fileBean['active'],
                fileBean['rating'],
                genres[:-1],
                stars[:-1],
                fileBean['video']))
            # 开始保存
            Path(fileBean['path']).mkdir(parents=True, exist_ok=True)
            print('  保存NFO信息')
            formatNfo(fileBean)
            saveNfo(fileBean)
            print('  保存封面')
            savePicture(fileBean)
            print('  保存样本图像')
            saveSampleImage(fileBean)
            print('  保存作品介绍视频')
            if searchType == 1:
                fileBean['videoname'] = fileBean['filename'] + '.mp4'
            else:
                fileBean['videoname'] = fileBean['filename'] + '-trailer.mp4'
            saveVideo(fileBean)
            print('  复制字幕文件')
            copySubtitleFile(1, fileBean)
            print('------番号%s完成--------------' % fileBean['avcode'])
        # print(fileBean)
        index = index + 1
    print('%d个番号，全部完毕' % len(avCodeList))


def mainFunction():
    doTask()
    # fileBean = {'avcode': 'MIDV-229', 'plot': '开始', 'basalpath': 'H:\新建文件夹 (2)\湿巾\字幕\测试',
    #             'path': 'H:\新建文件夹 (2)\湿巾\字幕\测试\MIDV-229-C'}
    # copySubtitleFile(1, fileBean)
    # networkJavDB(fileBean)
    # saveVideo(fileBean)
    # print(fileBean)
    # networkJavLibrary(fileBean)
    # print(fileBean)
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


if __name__ == '__main__':
    mainFunction()
