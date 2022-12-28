import os


def delete(path):
    os.chdir(path)
    for fileName in os.listdir():
        # print(fileName)
        if os.path.isdir(fileName):
            print('------删除%s下面的相应文件和文件夹------' % fileName)
            # 找到SampleImage，实力图像
            samplePath = os.path.join(fileName, 'SampleImage')
            if os.path.exists(samplePath):
                for tempFileName in os.listdir(samplePath):
                    os.remove(os.path.join(samplePath, tempFileName))
                os.rmdir(samplePath)
                print('   删除SampleImage文件夹')
            # 删除当前文件夹下的jpg图片和nfo文件
            for jpgnfoFileName in os.listdir(fileName):
                fileNames = os.path.splitext(jpgnfoFileName)
                if '.jpg' == fileNames[1]:
                    os.remove(os.path.join(fileName, jpgnfoFileName))
                    print('   删除jpg文件')
                # if '.db' == fileNames[1]:
                #     os.remove(os.path.join(fileName, jpgnfoFileName))
                #     print('   删除db文件')
                if '.nfo' == fileNames[1]:
                    os.remove(os.path.join(fileName, jpgnfoFileName))
                    print('   删除nfo文件')


if __name__ == '__main__':
    # 删除文件夹里的jpg，nfo，db文件，SampleImage文件夹
    # delete(r'Z:\LSP\AdultVideo')
    delete(r'Z:\LSP\测试')
