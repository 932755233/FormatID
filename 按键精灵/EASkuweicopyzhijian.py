import pynput
import xlrd
import time
from pynput.mouse import Button


class Task:
    excelPath = r"C:\Users\Danny\Desktop\temp.xls"
    tempXuyao = []

    def __init__(self):

        # 获取对象
        self.mouse = pynput.mouse.Controller()
        self.keyboard = pynput.keyboard.Controller()
        # 获取excel
        self.workbook = xlrd.open_workbook(self.excelPath)  # 打开Excel
        self.sheet = self.workbook.sheets()[0]
        for i in range(0, self.sheet.nrows):
            tempyuanshi = self.sheet.row_values(rowx=i, start_colx=0, end_colx=None)
            if tempyuanshi[6] == '启用':
                self.tempXuyao.append(tempyuanshi)

    def moveToXinJian(self):
        # 移动到新建位置点击
        print("  移动鼠标到新建位置并点击")
        self.mouse.position = (12, 64)
        self.mouse.click(Button.left, 1)  # 点击鼠标事件

    def moveToKuweibianma(self,str):
        # 移动到库位编码位置点击并输入
        print("  移动到库位编码位置点击并输入")
        self.mouse.position = (1314,692)
        self.mouse.click(Button.left, 1)  # 点击鼠标事件
        self.keyboard.type(str)

    def moveToKuweimiangcheng(self,str):
        # 移动到库位名称位置点击并输入
        print("  移动到库位名称位置点击并输入")
        self.mouse.position = (1299,711)
        self.mouse.click(Button.left, 1)  # 点击鼠标事件
        self.keyboard.type(str)
    def moveToSaveButton(self):
        # 移动到保存按钮位置点击
        print("  移动到保存按钮位置点击")
        self.mouse.position = (1191,610)
        self.mouse.click(Button.left, 1)  # 点击鼠标事件

    def moveToCloseButton(self):
        # 移动到关闭按钮位置
        print("  移动到关闭按钮位置")
        self.mouse.position = (1425,564)
        self.mouse.click(Button.left, 1)  # 点击鼠标事件

    def doTask(self):
        for i in self.tempXuyao:
            print(i)
        print("获取到库位中已启用的库位，一共：%d" % len(self.tempXuyao))
        # print("是否开始：y/n")
        # tempOff = input()
        tempOff = 'y'
        if tempOff == 'y':
            print("---开始---")
            for i in range(0, len(self.tempXuyao)):
            # temp = self.tempXuyao[4]
                print(self.tempXuyao[i])
                self.moveToXinJian()
                time.sleep(1)
                self.moveToKuweibianma(self.tempXuyao[i][0])
                time.sleep(1)
                self.moveToKuweimiangcheng(self.tempXuyao[i][1])
                time.sleep(1)
                self.moveToSaveButton()
                time.sleep(2)
                self.moveToCloseButton()
                print("---结束---")
                time.sleep(1)
        print("所有任务结束")


if __name__ == '__main__':
    t = Task()
    t.doTask()

# 新建按钮位置：12，64
# 新建窗口
#     库位编码位置：1314,692
#     库位名称位置：1299,711
#     保存按钮位置：1191,610
#     关闭按钮位置：1425,564
