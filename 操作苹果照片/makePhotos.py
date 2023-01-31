import os


applePhotosPath = r'C:\Users\Danny\Pictures\iCloud Photos\Photos'


if __name__ == '__main__':
    ssss = []
    for fileName in os.listdir(applePhotosPath):
        n,t = os.path.splitext(fileName)
        if '.MOV' == t or '.mov' == t:
            continue
        print(fileName)
        ssss.append(fileName)


    print(len(ssss))
    print(10352+3526)