import xlrd
import xlwt
from xlutils.copy import copy

ascii_a = ord('A')

workboox = xlrd.open_workbook('/Users/danny/Desktop/朱仰腾/二郓城县郓州街道办事处陈路口小学体测数据模板 .xls')
sheet = workboox.sheet_by_index(0)


if __name__ == '__main__':
    print(sheet.cell(0,ord('C')-ascii_a))
    print(ord('C')-ord('A'))