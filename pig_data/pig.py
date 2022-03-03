import time

from bs4 import BeautifulSoup  # 网页解析
import xlwt  # excel
import re  # 正则表达式
import urllib.request, urllib.error
import ssl
import datetime
import chardet
import requests

# 装数据的集合
datalist = []

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    # 获取路径
    dataList = getData()

    # 保存数据
    saveData(dataList)


def getData():
    thisDate = datetime.datetime.now()
    thisDay = "%s-%s-%s" % (thisDate.year, thisDate.month, thisDate.day)
    page = 1
    flagg = False

    for i in range(200):

        # 指定所需爬取网页路径
        basePath = "https://bj.zhue.com.cn/index.php?&page=" + str(page)
        # 解析数据
        html = uskURL(basePath)

        # 解析网页数据
        bs = BeautifulSoup(html, "html.parser")

        tables = bs.find_all("table", class_="t_f")

        index = 0
        # 用来显示的时间
        showDate = tables[1].find_all("tr")[2].td.text
        print("第%s页。此页时间：%s" % (page, showDate))
        # 遍历表格里面的tr
        for trs in tables[1].find_all("tr"):
            index = index + 1
            if index < 3:
                continue
            # item = str(item)  # 转化为字符串.a.string
            tds = trs.find_all("td")
            # 判断时间是否为今天
            d1_stf = time.strptime(tds[0].text.strip(), "%Y-%m-%d")
            d2_stf = time.strptime(thisDay, "%Y-%m-%d")
            if d1_stf != d2_stf:
                print("第%s条已到%s" % (index, tds[0].text.strip()))
                flagg = True
                break
            ppp = [tds[0].text.strip(),
                   tds[1].text.strip(),
                   tds[2].text.strip(),
                   tds[3].text.strip(),
                   tds[4].text.strip(),
                   tds[5].find("li", class_="jgtp").text.strip(),
                   tds[5].find("li", class_="jgdw").text.strip(),
                   tds[6].text.strip(),
                   tds[7].text.strip(),
                   tds[8].text.strip(),
                   tds[10].text.strip()]
            datalist.append(ppp)
        if flagg:
            break
        page = page + 1
        # break

    print(datalist)
    return datalist


def saveData(dataList):
    Book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # style_compression:表示是否压缩，不常用
    sheet = Book.add_sheet("猪", cell_overwrite_ok=True)  # cell_overwrite_ok，表示是否可以覆盖单元格
    line = ("日期", "省市", "报价地点", "产品名称", "分类", "价格", "单位", "买/卖", "发布人", "联系方式", "备注")
    for item in range(len(line)):  # 此处循环如果line里只有一个字符串，那么生成的xls里，只会出现一个‘详’字
        # print(len(line))
        sheet.write(0, item, line[item])  # wirte(row, col, *args)
    for i in range(len(dataList)):  # 第一次循环应是将行数，有多少数据有多少行
        data = dataList[i]  # 每一条数据应该放在一行里，所以将在一次进行for循环
        for j in range(len(line)):
            sheet.write(i + 1, j, data[j])

    Book.save(data[0] + ".xls")
    print("%s数据已保存！" % data[0])


def uskURL(basePath):
    heard = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "GB2312"
        # 伪装为浏览器
    }
    html = ""
    r = requests.get(basePath, headers=heard)
    html = r.text

    return html


if __name__ == '__main__':
    main()
