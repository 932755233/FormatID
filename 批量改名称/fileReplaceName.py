import os


def walkFile(path):
    filenames = []
    for fileName in os.listdir(path):
        # print(fileName)
        if 'mp4' in os.path.splitext(fileName)[1]:
            filenames.append(fileName)
    filenames.sort(key=lambda x: str(x[:-4]))
    print(filenames)
    return filenames


def formatFileName():
    fileNameList = ['1.mp4']
    for i in range(11):
        fileNameList.append('1 (%d).mp4' % (i + 1))
    for n in range(1, 62):
        fileNameList.append('%d.mp4' % (n + 1))
    print(fileNameList)
    return fileNameList


if __name__ == '__main__':
    # walkFile('Z:\LSP\Video\自慰爱好者')
    # fileNameList = formatFileName()
    # path = r'Z:\LSP\Video\自慰爱好者'
    path = r'D:\FFOutput'
    os.chdir(path)
    print(os.getcwd())
    fileNameList = walkFile(path)

    # stats = os.stat('1.mp4')
    # print(stats.st_size / 1024 / 1024)
    # os.rename('1.mp4','111.mp4')
    # print(os.getcwd())
    index = 1
    for fileName in fileNameList:
        # newFileName = '{:02d}'.format(index)
        newFileName = 'S01E%s' % fileName
        print('更改文件名%s---%s' % (fileName, newFileName))
        os.rename(fileName, newFileName)
        index = index + 1
