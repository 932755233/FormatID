import os.path
import pymediainfo

oldPath = r'/Users/danny/Pictures/test1'
newPath = r'/Users/danny/Pictures/test2'

fileList = []


def queryFileList():
    for filename in os.listdir(oldPath):
        fileList.append(filename)

        mi = pymediainfo.MediaInfo.parse(os.path.join(oldPath, filename))
        print(mi.to_data()
              )


if __name__ == '__main__':
    queryFileList()
    print(fileList)
