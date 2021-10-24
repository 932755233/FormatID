# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import fileinput


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script. if __name__ == '__main__': print_hi('PyCharm') try: with
# open('/Users/danny/Desktop/petshop/centre/src/main/res/layout/layout_purchase_request_detail.xml', 'r') as xml:
# print(xml) # for str in xml.readline() #     print str finally: if xml: xml.close()
# path = '/Users/danny/Desktop/petshop/centre/src/main/res/layout/item_sell_out_warehouse.xml'
# path = 'G:\\work\\petshop\\centre\\src\\main\\res\\layout\\layout_customer_cancellation.xml'
path = 'G:\\work\\petshop\\agent\\src\\main\\res\\layout\\item_market_theout.xml'
tempStr = ''
# with open(path, 'rb') as lines:
#     for line in lines.readline():
#         print(line)

for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        print('%s.setText();' % temp)
    tempStr = line
print()
for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        print('TextView %s;' % temp)
    tempStr = line
print()
for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        print('%s = itemView.findViewById(R.id.%s);' % (temp, temp))
    tempStr = line

print()
tempStrSS = ''
for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):

    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        if temp[-3:] == 'red':
            continue
        if temp[-3:] == 'txt':
            tempStrSS = ''
            continue
        print('@ViewById(R.id.%s)' % temp)
        print('TextView %s;//%s' % (temp, tempStrSS))
    if line.find('android:text=') >= 0:
        if tempStrSS == '':
            tempStrSS = line.split('=')[1][1:-6]
    tempStr = line

# 自动生成注释和控件
# 生成settext
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
