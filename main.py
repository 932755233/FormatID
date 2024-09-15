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
# path = '/Users/danny/Desktop/petshop/centre/src/main/res/layout/layout_custinfosupple_company_info.xml'
# path = 'G:\\work\\petshop\\centre\\src\\main\\res\\layout\\item_gift_pur_req_bill_list.xml'
# path = '/Users/danny/Desktop/petshop/centre/src/main/res/layout/item_purchase_order_list.xml'
# path = 'G:\\work\\petshop\\centre\\src\\main\\res\\layout\\layout_f_claim_expense_entry_item.xml'
# path = r'G:\work\petshop202406\agentgj\src\main\res\layout\activity_main.xml'
# path = r'G:\work\petshop202406\centre\src\main\res\layout\activity_meetingexpense_info.xml'
# path = 'G:\\work\\petshop\\agent\\src\\main\\res\\layout\\layout_product_coding_dispose.xml'
path = r'G:\work\petshop202406\centre\src\main\res\layout\layout_technical_support_application.xml'
tempStr = ''
# with open(path, 'rb') as lines:
#     for line in lines.readline():
#         print(line)

for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        if temp[-3:] == 'red':
            continue
        if temp[-3:] == 'txt':
            continue
        print('holder.%s.setText(bean.get());' % temp)
    tempStr = line
print()
for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        if temp[-3:] == 'red':
            continue
        if temp[-3:] == 'txt':
            continue
        print('%s.setText();' % temp)
    tempStr = line
print()
for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        # if temp[-3:] == 'red':
        # continue
        if temp[-3:] == 'txt':
            continue
        print('TextView %s;' % temp)
    tempStr = line
print()
for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        # if temp[-3:] == 'red':
        # continue
        if temp[-3:] == 'txt':
            continue
        print('holder.%s = itemView.findViewById(R.id.%s);' % (temp, temp))
    tempStr = line

print()
tempStrSS = ''
for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):

    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        # if temp[-3:] == 'red':
        # tempStrSS = tempStrSS + '_red'
        # tempStrSS = ''
        # continue
        if temp[-3:] == 'txt':
            tempStrSS = ''
            continue
        print('@ViewById')
        print('TextView %s;//%s' % (temp, tempStrSS))
    if line.find('android:text=') >= 0:
        if tempStrSS == '':
            tempStrSS = line.split('=')[1][1:-6]
    tempStr = line
print()

for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        if temp[-3:] == 'red':
            continue
        if temp[-3:] == 'txt':
            continue
        print('holder.%s_red.setVisibility(View.INVISIBLE);' % temp)
        print('holder.%s.setBackgroundResource(R.drawable.rounded_text);' % temp)
        print('holder.%s.setFocusable(false);' % temp)
        print('holder.%s.setClickable(false);' % temp)
        print('holder.%s.setFocusableInTouchMode(false);' % temp)
        print('holder.%s.setHint("");' % temp)
        print()
    tempStr = line

print()

tempStrSSs = ''
for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):

    if line.find('android:id="@+id/') >= 0:
        temp = line.split('/')[1][:-2]
        if temp[-3:] == 'red':
            tempStrSSs = tempStrSSs + '_red'
            tempStrSSs = ''
            continue
        if temp[-3:] == 'txt':
            tempStrSSs = ''
            continue
        print('case R.id.%s: //%s' % (temp, tempStrSSs))
        print('  break;')
    if line.find('android:text=') >= 0:
        if tempStrSSs == '':
            tempStrSSs = line.split('=')[1][1:-6]
    tempStr = line
print()

# 自动生成注释和控件
# 生成settext
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
