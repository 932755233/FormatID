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

xmlname = r'数据中心,datacenter,' \
          r'业&#8194;务&#8194;员,creator_name,' \
          r'客&#8195;&#8195;户,emp_name,' \
          r'计划开始&#8196;\n日期,plane_start_date,' \
          r'计划完成&#8196;\n日期,plane_end_date,' \
          r'事项描述,schedule,' \
          r'完成标准,standard,' \
          r'完成情况,progress,' \
          r'提前提醒\n(天),leadtime,' \
          r'任务状态,status,' \
          r'备&#8195;&#8195;注,description'

xmls = xmlname.split(',')

index= 0
ss = []
result = []
for name in xmls:


    if index%2 == 0:
        ss = []
        ss.append(name)
    else:
        ss.append(name)
        result.append(ss)

    # print(name)
    index = index +1



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














