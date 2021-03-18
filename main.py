# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import fileinput


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
# try:
#     with open('/Users/danny/Desktop/petshop/centre/src/main/res/layout/layout_purchase_request_detail.xml', 'r') as xml:
#     print(xml)
#     # for str in xml.readline()
#     #     print str
# finally:
#     if xml:
#         xml.close()
temp = ''
for line in fileinput.input(
        '/Users/danny/Desktop/petshop/centre/src/main/res/layout/layout_purchase_request_detail.xml'):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        print('@ViewById(R.id.'+temp+ ')')
        print(tempStr[tempStr.index('<') + 1:-1]+' '+temp+';')
    tempStr = line

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
