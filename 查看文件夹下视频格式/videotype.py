import os
import sys
from pathlib import Path

import pymediainfo
import shutil

newFilePath = r'H:\新建文件夹'
videoTypeYuanZu = ('.mp4', '.MP4', '.avi', '.AVI', '.wmv', '.WMV', '.rm', '.RM', '.rmvb', '.RMVB','.mkv','.MKV')

sssss = 'niaho'


def copyFile(oldPath, fileName):
    newPath = r'%s\%s' % (newFilePath, fileName)
    print('  新文件路径：%s' % newPath)
    shutil.copyfile(oldPath, newPath)
    print('    复制完成')
    with open(r'%s\位置.txt' % newFilePath, mode='a') as f:
        f.write(oldPath)
        f.write('\n')
        print('  保存位置信息')


def find(path):
    for fileName in os.listdir(path):
        itemPath = os.path.join(path, fileName)
        if os.path.isdir(itemPath):
            find(itemPath)
        else:
            n, t = os.path.splitext(fileName)
            if t in videoTypeYuanZu:
                mi = pymediainfo.MediaInfo.parse(itemPath)
                try:
                    myFormat = mi.to_data()['tracks'][1]['internet_media_type']
                except IndexError as e:
                    print(e)
                    print(fileName)
                    print(mi.to_data())
                    sys.exit()
                if 'video/MP4V-ES' == myFormat:
                    print()
                    print('类型：%s------文件名：%s' % (myFormat, fileName))
                    print('  文件路径：%s' % itemPath)
                    print('复制文件')
                    # copyFile(itemPath, fileName)
                else:
                    # print('类型：%s------文件名：%s' % (myFormat, fileName))
                    # print('  文件路径：%s' % itemPath)
                    print('-',end=' ')


def findOne():
    fileName = 'Z:\LSP/Video/【极品空姐 真母狗空姐】近期热门空姐系列第4部 揭开高冷空姐私下糜烂淫秽的面纱/v/guochan2048.com-1 (36).avi'
    mi = pymediainfo.MediaInfo.parse(fileName)
    myFormat = mi.to_data()['tracks'][1]['internet_media_type']
    # myFormat = mi.to_data()
    # print(myFormat)
    print('类型：%s------文件名：%s' % (myFormat, fileName))


if __name__ == '__main__':
    # filePath = r'Z:\LSP\AdultVideo'
    # filePath = r'Z:\LSP\国产AV'
    # filePath = r''
    filePath = r'Z:\LSP\Video'
    # filePath = r'Z:\LSP\里番'

    find(filePath)
    # findOne()
