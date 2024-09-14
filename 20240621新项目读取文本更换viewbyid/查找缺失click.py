import fileinput
import os
import re


class IDReplace:

    def __init__(self):
        self.findId = re.compile(r'case R\.id\.(\w*)')
        self.findBian = re.compile(r' (\w*);')
        self.leiBeans = []

    def replaceText(self, path):

        textLines = []
        idBeans = []

        for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
            # print(line.strip())
            textLines.append(line)

        for (index, line) in enumerate(textLines, 0):
            search = self.findId.search(line)
            if search:
                xmlId = search.group(1)
                # bianliangName = self.findBian.search(textLines[index + 1]).group(1)

                idBean = {"id": xmlId, "i": index}

                idBeans.append(idBean)

        print('  找到id的数量为：%d' % len(idBeans))
        # print(idBeans)

        # 从头开始查找相同ID的变量名
        for idBean in idBeans:
            leiBean = {'fileName': '', 'hang': []}
            for i, line in enumerate(textLines):
                pattern = re.compile(r' *\w* ' + idBean["id"] + ';')
                if re.match(pattern, line):
                    # print(line)
                    # print(textLines[i-1])
                    if 'onClick' not in textLines[i - 1]:
                        # print(path)
                        # print(i)
                        leiBean['fileName'] = path
                        leiBean['hang'].append(i)
                    break
            if len(leiBean['hang']) > 0:
                self.leiBeans.append(leiBean)

        # line = textLines[idBean["i"]]
        # if 'onClick' in line:
        #     textLines[idBean["i"]] = '\t@ViewById(onClick = 0)\n'
        # else:
        #     textLines[idBean["i"]] = '\t@ViewById\n'
        #
        # for (index, line) in enumerate(textLines):
        #     for idBean in idBeans:
        #         # 根据正则查找单词，前后都需要满足不是字母或者数字，这才是一个正常变量名称
        #         pattern = r'\W(' + idBean["bianliang"] + ')\W'
        #         # 单纯替换会把正则搜到的前后字符都替换掉，用lambda拿到正则查找到的分组内容，取前一个字符，和后一个字符，拼接成完整的部位代码
        #         # 例：(word) 的部位会被替换为 hello，用lambda后，拿前后拼接成(hello)
        #         line = re.sub(pattern, lambda x: x.group()[0: 1] + idBean['id'] + x.group()[-1:], line)
        #     textLines[index] = line

        # for line in textLines:
        #     print(line, end='')

        # file = open(path, 'w', encoding='utf-8')
        # file.truncate(0)
        # for line in textLines:
        #     file.write(line)
        # file.close()

    def dotask(self):
        fuPath = r'G:\work\petshop202406\wukong\src\main\java\com\centre\wkoffice\centre'

        zipaths = []

        for file in os.listdir(fuPath):
            for ziFile in os.listdir(os.path.join(fuPath, file)):
                if ziFile == 'activity':
                    activityPath = os.path.join(fuPath, file, 'activity')
                    zipaths.append(activityPath)
                elif ziFile == 'fragment':
                    fragmentPath = os.path.join(fuPath, file, 'fragment')
                    zipaths.append(fragmentPath)

        print('一共%d个文件夹' % len(zipaths))
        print()

        filePaths = []
        for zipath in zipaths:
            for path in os.listdir(zipath):
                filePath = {"path": os.path.join(zipath, path), "name": path}
                filePaths.append(filePath)

        print('一共%d个Java文件' % len(filePaths))
        print()

        for (index, filePathBean) in enumerate(filePaths, 1):
            print(str(index) + "---" + filePathBean['name'] + "---开始")
            self.replaceText(filePathBean['path'])
            print("  " + filePathBean['name'] + "---完成")

        print(self.leiBeans)
        print(len(self.leiBeans))

        for bean in self.leiBeans:
            print(bean)


if __name__ == '__main__':
    path = r'G:\work\petshop202406\cmes\src\main\java\com\centre\cmes\base\handwritten\LinePathActivity.java'
    task = IDReplace()
    # task.dotask()
    task.replaceText(path)

    # dotask();manufacturer_scanning_content_tv

    # fuPath = r'G:\work\petshop202406\wukong\src\main\java\com\centre\wkoffice\centre'
    #
    # zipaths = []
    #
    # for file in os.listdir(fuPath):
    #     for ziFile in os.listdir(os.path.join(fuPath, file)):
    #         if ziFile == 'activity':
    #             activityPath = os.path.join(fuPath, file, 'activity')
    #             zipaths.append(activityPath)
    #         elif ziFile == 'fragment':
    #             fragmentPath = os.path.join(fuPath, file, 'fragment')
    #             zipaths.append(fragmentPath)
    #
    # print('一共%d个文件夹' % len(zipaths))
    # print()
    #
    # filePaths = []
    # for zipath in zipaths:
    #     for path in os.listdir(zipath):
    #         filePath = {"path": os.path.join(zipath, path), "name": path}
    #         filePaths.append(filePath)
    #
    # print('一共%d个Java文件' % len(filePaths))
    # print()
    #
    # for (index, filePathBean) in enumerate(filePaths, 1):
    #     print(str(index) + "---" + filePathBean['name'] + "---开始")
    #     replaceText(filePathBean['path'])
    #     print("  " + filePathBean['name'] + "---完成")

    # replaceText(r'G:\work\petshop202406\wukong\src\main\java\com\centre\wkoffice\centre\c_centreinfo\activity\AndroidPingActivity.java')
    # line = '''
    #     btnMenu.setVisibility(View.VISIBLE);
    #     btnMenu1.setVisibility(View.VISIBLE);
    #     btnMenua.setVisibility(View.VISIBLE);
    #     btnMenuv.setVisibility(View.VISIBLE);'''
    # pattern = r'\W(btnMenu)\W'
    # line = re.sub(pattern, lambda x: x.group()[0: 1] + '123' + x.group()[-1:], line)
    # print(line)
