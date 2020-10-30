# ch3ex1_weight.py
# ab00b
# 地球月亮体重增长计算
# 2020.9.30

# docstring和输出都用了英文, 因为这些单词比较简单哈哈哈

def moon_weight(earth_weight):
    ''' Input weight on earth, Return weight on the moon'''
    return earth_weight * 16.5 / 100


def grow(init_value, speed, time):
    '''Calculate the growth with given initial value, speed and time'''
    return init_value + speed * time


init_weight = int(input("Your current weight is (kg): "))
for i in range(0, 11):
    earth_weight = grow(init_weight, 0.5, i)

    print("Year {:2}".format(i) + " : Earth : {:.1f}".format(earth_weight) +
          " kg \n\t  Moon  : {:.1f}".format(moon_weight(earth_weight)) +
          " kg ")
