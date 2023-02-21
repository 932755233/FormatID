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

xmlname = '单据编码,number,业务日期,date,考核对象,assessor,行为项目,project,加减分类型,type,一级审核人,one_auditor,二级审核人,two_auditor,行为项目备注,project_remark,考核分数,assess_num,备注,remark'

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
    print(f'''
     <RelativeLayout
                    android:id="@+id/ll_{temp[1]}"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:background="@color/colorWhite"
                    android:paddingTop="@dimen/basicPadding_"
                    android:paddingBottom="@dimen/basicPadding_">

                    <TextView
                        android:id="@+id/tv_red_{temp[1]}"
                        style="@style/text_sign_Style"
                        android:visibility="invisible" />

                    <TextView
                        android:id="@+id/tv_txt_{temp[1]}"
                        style="@style/text_Style"
                        android:layout_toRightOf="@+id/tv_red_{temp[1]}"
                        android:text="{temp[0]}:" />

                    <TextView
                        android:id="@+id/tv_{temp[1]}"
                        style="@style/edit_style"
                        android:layout_toRightOf="@+id/tv_txt_{temp[1]}"
                        android:background="@drawable/rounded_text" />
                </RelativeLayout>
    
    
    ''')




print(result)














