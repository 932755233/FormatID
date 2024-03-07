import xlrd
import xlutils
import xlwt
import random
from xlutils.copy import copy

from zhu.FormatTizhi import FormatTizhi


def getNumber(str, num):
    return str[:len(str) - num] + '.' + str[len(str) - num:]


ascii_a = ord('A')

colx = ord('G') - ascii_a

fileName = r'郓城县郓州街道办事处陈路口小学体测数据模板'
path = r'C:\Users\Danny\Desktop\朱仰腾\%s.xls' % fileName
outpath = r'C:\Users\Danny\Desktop\朱仰腾\1111.xls'

indexEnd = 10000000

feihuoliangStart = 2300
feihuoliangEnd = 2750
feihuoliangStartNv = 1920
feihuoliangEndNv = 2200

# 这里需要标准乘以十
mi50Start = 86
mi50End = 90
mi50StartNv = 90
mi50EndNv = 96

# 这里需要标准乘以十
zuoweitiStart = 51
zuoweitiEnd = 90
zuoweitiStartNv = 96
zuoweitiEndNv = 129

yifenzhongStart = 128
yifenzhongEnd = 147
yifenzhongStartNv = 129
yifenzhongEndNv = 159

yangwoStart = 35
yangwoEnd = 45
yangwoStartNv = 33
yangwoEndNv = 42

wangfanStart = 133
wangfanEnd = 145
wangfanStartNv = 149
wangfanEndNv = 155

# workboox = xlrd.open_workbook('/Users/danny/Desktop/朱仰腾/二郓城县郓州街道办事处陈路口小学体测数据模板 .xls')
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)

outworkbook = copy(workbook)
sheetss = outworkbook.get_sheet(0)
if __name__ == '__main__':
    formatTizhi = FormatTizhi()
    for i in range(0, sheet.nrows - 1):
        print(str(i + 1), sheet.cell(i + 1, ord('F') - ascii_a).value, end=' ')

        xinbie = sheet.cell(i + 1, colx).value
        nianji = sheet.cell(i + 1, ord('A') - ascii_a).value
        print(xinbie, end=' ')
        print(nianji, end=' ')
        # feihuoliang = ''
        # mi50 = '0.0'
        # zuoweiti = '0.0'
        # yifenzhong = '0.0'
        # yangwo = '0.0'
        # wangfan = '0.0'
        # if xinbie == '1':
        #     # 男的
        #     feihuoliang = str(random.randint(feihuoliangStart, feihuoliangEnd))
        #     mi50 = str(random.randint(mi50Start, mi50End))
        #     zuoweiti = str(random.randint(zuoweitiStart, zuoweitiEnd))
        #     yifenzhong = str(random.randint(yifenzhongStart, yifenzhongEnd))
        #     yangwo = str(random.randint(yangwoStart, yangwoEnd))
        #     wangfan = str(random.randint(wangfanStart, wangfanEnd))
        # else:
        #     # 女的
        #     feihuoliang = str(random.randint(feihuoliangStartNv, feihuoliangEndNv))
        #     mi50 = str(random.randint(mi50StartNv, mi50EndNv))
        #     zuoweiti = str(random.randint(zuoweitiStartNv, zuoweitiEndNv))
        #     yifenzhong = str(random.randint(yifenzhongStartNv, yifenzhongEndNv))
        #     yangwo = str(random.randint(yangwoStartNv, yangwoEndNv))
        #     wangfan = str(random.randint(wangfanStartNv, wangfanEndNv))
        # print(feihuoliang, end=' ')
        bean = formatTizhi.getBean(nianji, xinbie)
        mi50 = ''
        if bean["mi50"] != '':
            mi50 = getNumber(bean["mi50"], 1)
            print(mi50, end=' ')

        zuoweiti = ''
        if bean["zuoweiti"] != '':
            zuoweiti = getNumber(bean["zuoweiti"], 1)
            print(zuoweiti, end=' ')
        # print(yifenzhong, end=' ')
        # print(yangwo, end=' ')
        wangfan = ''
        if bean["wangfan"] != '':
            m, s = divmod(int(bean["wangfan"]), 60)
            bu0 = ''
            if s < 10:
                bu0 = '0'
            wangfan = "%s'%s%s" % (m, bu0, s)
            print(wangfan)
        sheetss.write(i + 1, ord('L') - ascii_a, bean["feihuoliang"])
        sheetss.write(i + 1, ord('M') - ascii_a, mi50)
        sheetss.write(i + 1, ord('N') - ascii_a, zuoweiti)
        sheetss.write(i + 1, ord('O') - ascii_a, bean["yifenzhong"])
        sheetss.write(i + 1, ord('P') - ascii_a, bean["yangwo"])
        sheetss.write(i + 1, ord('Q') - ascii_a, wangfan)
    outworkbook.save(outpath)
    print("生成文件成功")
    print('一共>', sheet.nrows, '<行')


def getRandom(start, end):
    if start not in '.' & end not in '.':
        return random.randint(int(start), int(end))
    elif start in '.' & end not in '.':
        start[start.find('.'):].length
        return
    return
