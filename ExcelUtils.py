# coding=utf-8
import xlrd

workbook = xlrd.open_workbook('/Users/danny/Desktop/common-documents/工作文档/采购入库/入库的编辑界面.xls')  # 打开Excel
sheet = workbook.sheets()[0]
rows = sheet.nrows

# for i in range(rows):
#     print(sheet.row_values(i)[:13])
# 根据excel生成bean需要的成员变量
cols = sheet.ncols
for i in range(cols):
    str = sheet.col_values(i)[0]
    print('String %s;' % str, end='')
    print('//%s' % sheet.col_values(i)[1])
    if str[-2:] == 'ID':
        print('String %sNAME;' % str[:-2], end='')
        print('//%s名称' % sheet.col_values(i)[1])

print(cols)
