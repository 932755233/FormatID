# coding=utf-8
import xlrd
import xlwt


def studentFomat():
    workbook = xlrd.open_workbook(filename=r'C:\Users\Danny\Desktop\王岚学校\一二年级学生.xlsx')
    sheet = workbook.sheets()[0]

    print('开始读取文件')

    cols = sheet.ncols
    print('有%s列' % cols)
    rows = sheet.nrows
    print('有%s行' % rows)
    list2 = []
    list3 = []
    list4 = []
    result = []
    for r in range(rows):
        list1 = []
        name = sheet.cell_value(r, 1)
        code = sheet.cell_value(r, 2)

        if name == '学生姓名':
            continue

        yinianji = sheet.cell_value(r, 3)
        ernianji = sheet.cell_value(r, 4)
        phone = sheet.cell_value(r, 5)
        name1 = sheet.cell_value(r, 6)
        code1 = sheet.cell_value(r, 7)
        name2 = sheet.cell_value(r, 8)
        code2 = sheet.cell_value(r, 9)
        name3 = sheet.cell_value(r, 10)
        code3 = sheet.cell_value(r, 11)
        name4 = sheet.cell_value(r, 12)
        code4 = sheet.cell_value(r, 13)
        name5 = sheet.cell_value(r, 14)
        code5 = sheet.cell_value(r, 15)
        name6 = sheet.cell_value(r, 16)
        code6 = sheet.cell_value(r, 17)

        # list1.append([name, code, yinianji, ernianji, phone])
        list1.append(['学生', name, code, name1, '居民身份证', code1, yinianji, ernianji, phone])
        if len(name2) > 0:
            list1.append(['学生', name, code, name2, '居民身份证', code2, yinianji, ernianji, phone])
        if len(name3) > 0:
            list1.append(['学生', name, code, name3, '居民身份证', code3, yinianji, ernianji, phone])
        if len(name4) > 0:
            list1.append(['学生', name, code, name4, '居民身份证', code4, yinianji, ernianji, phone])
        if len(name5) > 0:
            list1.append(['学生', name, code, name5, '居民身份证', code5, yinianji, ernianji, phone])
        if len(name6) > 0:
            list1.append(['学生', name, code, name6, '居民身份证', code6, yinianji, ernianji, phone])

        if len(yinianji) > 0 and (len(ernianji) == 0):
            list2.extend(list1)
        elif (len(yinianji) == 0) and (len(ernianji) > 0):
            list4.extend(list1)
        else:
            list3.extend(list1)

    # result.extend(list2)
    # result.extend(list3)

    print('开始写出文件')

    wirteWorkbook = xlwt.Workbook()
    wSheet = wirteWorkbook.add_sheet('Sheet1')
    for yinianjiList in range(len(list2)):
        for nn in range(len(list2[yinianjiList])):
            wSheet.write(yinianjiList, nn, list2[yinianjiList][nn])
    wirteWorkbook.save(r'C:\Users\Danny\Desktop\王岚学校\一年级.xls')

    wirteWorkbook = xlwt.Workbook()
    wSheet = wirteWorkbook.add_sheet('Sheet1')
    for yinianjiList in range(len(list4)):
        for nn in range(len(list4[yinianjiList])):
            wSheet.write(yinianjiList, nn, list4[yinianjiList][nn])
    wirteWorkbook.save(r'C:\Users\Danny\Desktop\王岚学校\二年级.xls')

    wirteWorkbook = xlwt.Workbook()
    wSheet = wirteWorkbook.add_sheet('Sheet1')
    for yinianjiList in range(len(list3)):
        for nn in range(len(list3[yinianjiList])):
            wSheet.write(yinianjiList, nn, list3[yinianjiList][nn])
    wirteWorkbook.save(r'C:\Users\Danny\Desktop\王岚学校\有问题.xls')

    print('结束写入文件')
    # for ss in range(len(list2)):
    #     print(list2[ss])
    # yinian = sheet.cell_value(1, 3)
    # print(len(yinian), "sss")


def teacherFomat():
    workbook = xlrd.open_workbook(filename=r'C:\Users\Danny\Desktop\学校\五六年级教共同居住和生活的全部人员信息统计表-6d8b999737dde2e1.xlsx')
    sheet = workbook.sheets()[0]

    print('开始读取文件')

    cols = sheet.ncols
    print('有%s列' % cols)
    rows = sheet.nrows
    print('有%s行' % rows)

    list1 = []
    for rr in range(rows):
        name = sheet.cell_value(rr, 1)
        code = sheet.cell_value(rr, 2)
        phone = sheet.cell_value(rr, 4)

        if name == '教师姓名':
            continue

        gong = [5, 7, 9, 11, 13, 15]
        for cc in gong:
            name1 = sheet.cell_value(rr, cc)
            if len(name1) == 0:
                continue
            code1 = sheet.cell_value(rr, cc + 1)
            list1.append(['教职工', name, code, name1, '居民身份证', code1, str(phone)])

    print('开始写出文件')
    wirteWorkbook = xlwt.Workbook()
    wSheet = wirteWorkbook.add_sheet('Sheet1')
    for yinianjiList in range(len(list1)):
        for nn in range(len(list1[yinianjiList])):
            wSheet.write(yinianjiList, nn, list1[yinianjiList][nn])
    wirteWorkbook.save(r'C:\Users\Danny\Desktop\学校\教师result.xls')
    print('结束写入文件')

def tebiede():
    workbook = xlrd.open_workbook(filename=r'C:\Users\Danny\Desktop\学校\11五年级共同居住人.xlsx')
    sheet = workbook.sheets()[0]

    print('开始读取文件')

    cols = sheet.ncols
    print('有%s列' % cols)
    rows = sheet.nrows
    print('有%s行' % rows)

    list1 = []
    for rr in range(rows):
        name = sheet.cell_value(rr, 2)
        code = sheet.cell_value(rr, 3)
        banji = sheet.cell_value(rr, 4)
        phone = sheet.cell_value(rr, 5)

        if name == '学生姓名':
            continue

        gong = [6, 8, 10, 12, 14, 16]
        for cc in gong:
            name1 = sheet.cell_value(rr, cc)
            if len(name1) == 0:
                continue
            code1 = sheet.cell_value(rr, cc + 1)
            list1.append(['学生', name, code, name1, '居民身份证', code1, phone,banji])

    print('开始写出文件')
    wirteWorkbook = xlwt.Workbook()
    wSheet = wirteWorkbook.add_sheet('Sheet1')
    for yinianjiList in range(len(list1)):
        for nn in range(len(list1[yinianjiList])):
            wSheet.write(yinianjiList, nn, list1[yinianjiList][nn])
    wirteWorkbook.save(r'C:\Users\Danny\Desktop\学校\特别的result.xls')
    print('结束写入文件')

if __name__ == '__main__':
    # studentFomat()
    teacherFomat()
    # tebiede()
    # gong = [4, 6, 7, 10, 12, 14]
    # for rr in gong:
    #     print(rr)
