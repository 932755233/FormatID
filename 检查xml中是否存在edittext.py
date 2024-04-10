import os
import fileinput
import xml.etree.ElementTree as ET

class CheckXml:
    path = 'G:\\work\\petshop\\centrehx\\src\\main\\res\\layout\\'

    def doTask(self):
        filesSet = set()

        files = os.listdir(self.path)
        print('一共%s个xml文件' % str(len(files)))
        for file in files:
            for line in fileinput.input(self.path + file, openhook=fileinput.hook_encoded('utf-8')):
                if line.find('EditText') >= 0:
                    filesSet.add(file)

        print('带EditText的xml有%s个' % str(len(filesSet)))
        noInputTypeFilesSet = set()
        for file in filesSet:
            # print(file)
            tree = ET.parse(self.path+file)
            root = tree.getroot()
            for elem in root.iter():
                if 'EditText' == elem.tag:
                    inputType = elem.get('{http://schemas.android.com/apk/res/android}inputType','0')
                    # print(inputType)
                    if 'number' not in inputType:
                        noInputTypeFilesSet.add(file)
        print('EditText中没有InputType的xml有%s个' % str(len(noInputTypeFilesSet)))
        noInputTypeFilesList = list(noInputTypeFilesSet)
        noInputTypeFilesList.sort()
        for index,file in enumerate(noInputTypeFilesList,1):
            print('%d----%s'%(index,file))



if __name__ == '__main__':
    cc = CheckXml()
    cc.doTask()

    # inputType = '0'
    # if 'number' not in inputType:
    #     print('1')
    # else:
    #     print('2')