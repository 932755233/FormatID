import os
import re

pattern = re.compile(r'"\w*?"', re.I)

index = 0;

texts = []

#  SelectSearchInfoActivity

def find(path):
    global index
    for fileName in os.listdir(path):
        itemPath = os.path.join(path, fileName)
        if os.path.isdir(itemPath):
            find(itemPath)
        else:
            if 'AppConstants' in fileName:
                print('zzy')
            else:
                javafile = open(itemPath, mode='r', encoding='UTF-8')
                ssss = re.findall(pattern, javafile.read())
                if len(ssss) == 0:
                    continue
                else:
                    showStr = '角标：%d---\t%s---\t%s' % (
                    index, fileName.ljust(len('CustomerContractOverDueProcessedFragment.java-----'), '-'), ssss)
                    # print(showStr)
                    for text in ssss:
                        if text not in texts:
                            texts.append(text)
                    with open('./wenben.txt', mode='a', encoding='utf-8') as fp:
                        fp.write(showStr)
                        fp.write('\n')
                    index = index + 1


if __name__ == '__main__':

    with open('./wenben.txt', mode='w', encoding='utf-8') as fp:
        fp.write('')

    path = r'G:\work\petshop\centrehx\src\main\java'
    find(path)

    print(texts)
    print(len(texts))
    with open('./wenben.txt', mode='a', encoding='utf-8') as fp:
        fp.write(str(texts))
        fp.write('\n')
        fp.write('一共%d个文本'%len(texts))

    # javafile = open(r'G:\work\petshop\centrehx\src\main\java\com\hxxy\workoffice\base\AppConstants.java', mode='r', encoding='UTF-8')
    # ssss = re.findall(pattern,javafile.read())
    # print(ssss)
