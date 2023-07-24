import xlrd

workbook = xlrd.open_workbook(
    r'G:\CodeGitHub\common-documents\工作文档\20230716检测单\tmp3759955772644522906.xls')  # 打开Excel
sheet = workbook.sheets()[0]
# 一共有多少行
rows = sheet.nrows
cols = sheet.ncols

beans = []

'''
表格第三行写上type字段
    0   非必填输入框
    1   必填输入框
    2
    3   只为显示字段
    4   不显示字段
'''


def generateXML():
    for bean in beans:
        nameTemp = bean['name'].lower()
        if len(nameTemp) == 3:
            nameTemp = r'%s&#8194;%s&#8194;%s' % (nameTemp[0], nameTemp[1], nameTemp[2])
        if len(nameTemp) == 2:
            nameTemp = r'%s&#8195;&#8195;%s' % (nameTemp[0], nameTemp[1])

        zhushiTemp = bean['zhushi'].lower()
        # 低于四个字，等于三个字
        if len(zhushiTemp) == 3:
            zhushiTemp = r'%s&#8194;%s&#8194;%s' % (zhushiTemp[0], zhushiTemp[1], zhushiTemp[2])
        if len(zhushiTemp) == 2:
            zhushiTemp = r'%s&#8195;&#8195;%s' % (zhushiTemp[0], zhushiTemp[1])

        type = bean['type']
        backgroudTemp = 'rounded_edit'
        inputTypeStr = ''
        if type == 4:
            continue
        elif type == 3:
            backgroudTemp = 'rounded_text'

        visiTemp = 'invisible'
        if type == 1:
            visiTemp = 'visible'
        topTempStr = r''' <RelativeLayout
   android:layout_width="match_parent"
   android:layout_height="wrap_content"
   android:paddingTop="@dimen/basicPadding_"
   android:paddingBottom="@dimen/basicPadding_">'''
        redTempStr = r'''  <TextView
    android:id="@+id/tv_%s_red"
    style="@style/in_out_text_Style"
    android:layout_marginLeft="5dp"
    android:layout_marginTop="0dp"
    android:layout_marginRight="0dp"
    android:text="*"
    android:textColor="@color/red"
    android:visibility="%s" />''' % (nameTemp, visiTemp)

        txtTempStr = r'''  <TextView
    android:id="@+id/tv_%s_txt"
    style="@style/in_out_text_Style"
    android:layout_marginTop="0dp"
    android:layout_toRightOf="@+id/tv_%s_red"
    android:text="%s:" />''' % (nameTemp, nameTemp, zhushiTemp)

        inputTextTempStr = r''' <TextView
    android:id="@+id/tv_%s"
    style="@style/in_out_edit_style"
    android:layout_toRightOf="@+id/tv_%s_txt"
    android:background="@drawable/%s" />''' % (nameTemp, nameTemp, backgroudTemp)

        inputEdtiTempStr = r''' <EditText
    android:id="@+id/et_%s"
    style="@style/in_out_edit_style"
    android:layout_toRightOf="@+id/tv_%s_txt"
    android:background="@drawable/rounded_edit"
    android:gravity="top|left"
    android:lines="3"
    android:minLines="3"
    android:padding="5dp" />''' % (nameTemp, nameTemp)

        bottomTempStr = r'''</RelativeLayout>'''

        inputTemp = inputTextTempStr
        if type == 1 or type == 0:
            inputTemp = inputEdtiTempStr

        print(topTempStr + redTempStr + txtTempStr + inputTemp + bottomTempStr)


def generateBean():
    for bean in beans:
        print('private String %s; //%s' % (bean['name'], bean['zhushi']))


def generateSetText():
    for bean in beans:
        print('tv_%s.setText(mBean.get%s());' % (bean['name'].lower(), bean['name']))


def format():
    print(cols)
    for i in range(cols):
        # print(sheet.col_values(i))
        col_value = sheet.col_values(i)
        bean = {'name': col_value[0]}
        bean['zhushi'] = col_value[1]
        bean['type'] = col_value[2]
        beans.append(bean)
    generateBean()
    print()
    print()
    generateSetText()
    print()
    print()
    generateXML()


if __name__ == '__main__':
    format()
