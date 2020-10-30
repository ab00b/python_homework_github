# 人民币和美元换算程序  
# ab00b
# 简介:
# 支持多种单位表示方式, 并且当输入中头、尾、数字与单位之间包含任意数量的空格时,均可以正常识别. 

# 使用死循环,便于一次执行中进行多次换算
while True:
    # 输入  
    note='请输入带单位的货币值(单位为元/美元/CNY/USD/yuan/dollars),输入exit退出: '
    input_str=input(note)
    # 如果不用终端输入,而是使用下面的测试输入,会无限输出,可以手动终止程序,或者放弃外部的死循环
    # input_str='     34元    '
    
    # 死循环的出口  
    if input_str=='exit':
        exit()

    # 去除输入头尾的空格
    input_str=input_str.strip()
    # 如果输入的数字和单位之间没有空格,那么在数字段段末尾加一个空格作为分隔的标记.  
    if str.find(' ',input_str)==-1:
        num_end_i=0
        while(input_str[num_end_i].isnumeric()==True):
            num_end_i+=1
        temp_str=''
        input_str=temp_str.join([input_str[:num_end_i],' ',input_str[num_end_i:]])
        # print(num_end_i)
        # print(input_str)

    #根据数字和单位之间的空格,将输入拆分成数字段和单位段.  
    number_str=input_str.partition(' ')[0]
    unit_str=input_str.rpartition(' ')[2]
    # print(number_str)
    # print(unit_str)

    #如果数字段的确都是数字,则合法,可以进行换算.  
    if number_str.isdecimal()==True:
        number=eval(number_str)
        if unit_str in ['元','CNY','yuan']:
            print('转化后的货币是{:.2f}美元\n'.format(number*6))
        elif unit_str in ['美元','USD','dollars']:
            print('转换后的货币是{:.2f}元\n'.format(number/6))
        else:
            print('输入格式错误\n')
    else:
        print('输入格式错误\n')