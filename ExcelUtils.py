# coding=utf-8
import xlrd

# workbook = xlrd.open_workbook('/Users/danny/Desktop/common-documents/工作文档/采购入库/入库的编辑界面.xls')  # 打开Excel
# workbook = xlrd.open_workbook(r'C:\Users\Danny\Desktop\common-documents\工作文档\采购入库\入库的编辑界面.xls')  # 打开Excel
workbook = xlrd.open_workbook(r'G:\CodeGitHub\common-documents\工作文档\库存调拨\表头.xls')  # 打开Excel
sheet = workbook.sheets()[0]
rows = sheet.nrows

# for i in range(rows):
#     print(sheet.row_values(i)[:13])
# 根据excel生成bean需要的成员变量
cols = sheet.ncols
for i in range(cols):
    str = sheet.col_values(i)[0]
    print('private String %s;' % str, end='')
    print('//%s' % sheet.col_values(i)[1])
    if str[-2:] == 'ID':
        print('private String %sNAME;' % str[:-2], end='')
        print('//%s名称' % sheet.col_values(i)[1])

print(cols)
#
sss = 0
sum = 0

for i in range(rows):
    # str = sheet.col_values(0)[i]
    strs = sheet.col_values(1)[i]
    strs = str(strs)
    if (strs == '0.0') | (strs == '42'):
        continue
    print('private String ' + sheet.col_values(0)[i] + ';// ' + strs)
    sum = sum+1


print(rows)
print(sum)
