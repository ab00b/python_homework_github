# input_str=input("请输入带单位的货币值(单位为元/美元/CNY/USD/yuan/dollars): ")
input_str='     123390   yuan    '
input_str=input_str.strip()
# print(input_str)
input_str=list(input_str)
# print(input_str)

end_of_number_index=-1
for c in input_str:
    if c.isnumeric():
        end_of_number_index+=1
    if c.isspace():
        input_str.remove(' ')
input_str.remove(' ')
# print(end_of_number_index)
print(input_str)

number_str=input_str[:end_of_number_index+1]
# print(number_str)
number=str(number_str)
print(number)

unit_str=input_str[end_of_number_index+1:]
print(unit_str)


# if unit_str in ['元','CNY','yuan']: