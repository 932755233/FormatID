import os
import re
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
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'existmag=mag; PHPSESSID=cjcodav99v2791ht4t6f0kcnb0; 4fJN_2132_saltkey=IYX9jY2o; 4fJN_2132_lastvisit=1672038441; 4fJN_2132_visitedfid=2; 4fJN_2132_home_diymode=1; 4fJN_2132_st_t=0%7C1672052343%7C126d950e0cdd67d020cf8a6909cbaa38; 4fJN_2132_forum_lastvisit=D_2_1672052343; starinfo=glyphicon%20glyphicon-minus; 4fJN_2132_sid=XfTXfj; 4fJN_2132_st_p=0%7C1672061998%7C84ade52bfe2b25c56414fd8d8e6ddc87; 4fJN_2132_viewid=tid_110427; 4fJN_2132_lastact=1672061999%09home.php%09misc; 4fJN_2132_sendmail=1'
}

headers2 = {
    # ':authority': 'www.javbus.com',
    # ':method': 'GET',
    # ':path': '/forum/forum.php?mod=viewthread&tid=110393&extra=page%3D3',
    # ':scheme': 'https',
    'accept': 'text / html, application / xhtml + xml, application / xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept - encoding': 'gzip,deflate,br',
    'accept - language': 'zh-CN,zh;q=0.9',
    'cache - control': 'max-age=0',
    'cookie': 'existmag=mag;PHPSESSID=cjcodav99v2791ht4t6f0kcnb0;4fJN_2132_saltkey=IYX9jY2o;4fJN_2132_lastvisit=1672038441;4fJN_2132_home_diymode=1;4fJN_2132_st_t=0%7C1672052343%7C126d950e0cdd67d020cf8a6909cbaa38;4fJN_2132_forum_lastvisit=D_2_1672052343;starinfo=glyphicon%20glyphicon-minus;4fJN_2132_visitedfid=2D36;4fJN_2132_sid = IYQN9p;4fJN_2132_st_p = 0 % 7C1672063820 % 7C1dbc94699239bbe413fc41d5b8e82cce;4fJN_2132_viewid = tid_110393;4fJN_2132_lastact = 1672063822 % 09home.php % 09misc;4fJN_2132_sendmail = 1',
    'referer': 'https://www.javbus.com/forum/forum.php?mod=forumdisplay&fid=2&page=3',
    'sec-ch-ua': '"Not?A_Brand";v = "8", "Chromium";v = "108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same - origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user - agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 108.0.0.0Safari / 537.36'
}


def network(url):
    response = requests.get(url, headers=headers, proxies=proxies)
    with open('./dowmload_gif.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    list = re.findall('src="(http.*?gif)"', response.text)
    return list


def saveGIF(gifBeanStr, index):
    imgData = requests.get(gifBeanStr, headers=headers2, proxies=proxies).content
    with open('./gif/%d.gif' % index, 'wb') as fp:
        fp.write(imgData)


if __name__ == '__main__':
    gifBeanList = network('https://www.javbus.com/forum/forum.php?mod=viewthread&tid=110393&extra=page%3D3')
    print('------开始下载图片，一共%d个------' % len(gifBeanList))
    index = 0
    # saveGIF(gifBeanList[0], 0)
    for gifBeanStr in gifBeanList:
        print('  开始下载：%d/%d------%s' % (index + 1, len(gifBeanList), gifBeanStr))
        saveGIF(gifBeanStr, index)
        index = index + 1
    print('------全部下载完毕------')
