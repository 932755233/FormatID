# coding:utf-8


# name = 1111
# print(name)
# name = input()
# name = int(name)
# print(id(name))
# print(type(name))
# print(name)
#
# str = '圣牧库'+'-%s库位'
# index = 1
# print(str%index)

# for index in range(15):
#     print('this.name'+str(index)+'=str['+str(index)+'];')
# print('"name'+str(index)+'",',end="")
# print('String', 'name' + str(index)+";")

xmlname = r'单据编号,number,' \
          r'业务日期,bizdate,' \
          r'交&#8194;出&#8194;人,send_person,' \
          r'交出人事&#8196;\n业部,send_person_business,' \
          r'接&#8194;收&#8194;人,get_person,' \
          r'接收人事&#8196;\n业部,get_person_business,' \
          r'备&#8195;&#8195;注,description'

xmls = xmlname.split(',')

index = 0
ss = []
result = []
for name in xmls:

    if index % 2 == 0:
        ss = []
        ss.append(name)
    else:
        ss.append(name)
        result.append(ss)

    # print(name)
    index = index + 1

for temp in result:
    print(f'''<RelativeLayout
    android:id="@+id/rl_{temp[1]}"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
                    android:background="@color/colorWhite"
                    android:paddingTop="@dimen/basicPadding_"
                    android:paddingBottom="@dimen/basicPadding_">

                    <TextView
                        android:id="@+id/tv_{temp[1]}_red"
                        style="@style/text_sign_Style"
                        android:visibility="invisible" />

                    <TextView
                        android:id="@+id/tv_{temp[1]}_txt"
                        style="@style/text_Style"
                        android:layout_toRightOf="@+id/tv_{temp[1]}_red"
                        android:text="{temp[0]}:" />

                    <TextView
                        android:id="@+id/tv_{temp[1]}"
                        style="@style/edit_style"
                        android:layout_toRightOf="@+id/tv_{temp[1]}_txt"
                        android:background="@drawable/rounded_text" />
                </RelativeLayout>''')

# print(result)
