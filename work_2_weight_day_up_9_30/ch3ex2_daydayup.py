# ch3ex2_daydayup.py
# ab00b
# 一个学习能力增长模型及其验证
# 2020.9.30


def day_up(learn_status_series, initial_power, power_up_threshold_days,
           power_up_period_days, power_up_rate_over_threshold_days):
    '''建立学习能力算法模型, 
       包含参数为 :一个学习状态序列(用布尔值表示每天是否学习),
                初始能力值
                提高能力所需的连续学习天数阈值
                每个学习周期的天数
                能力提升比率(周期内连续学习学习天数达到阈值后, 每天的能力相比前一天增加多少比例)'''
    current_power = initial_power
    continuous_learning_days_in_a_period = 0
    # day_index = 0    #用于调试时检查模型工作情况

    for this_day_learn_status in learn_status_series:
        # day_index += 1

        if this_day_learn_status == True:
            continuous_learning_days_in_a_period += 1

        elif this_day_learn_status == False:
            continuous_learning_days_in_a_period = 0

        if continuous_learning_days_in_a_period > power_up_threshold_days:
            if continuous_learning_days_in_a_period <= power_up_period_days:
                current_power = current_power * (
                    1 + power_up_rate_over_threshold_days)
            #如果连续学习超出一个周期的天数, 那么连续学习天数改为1天
            elif continuous_learning_days_in_a_period > power_up_period_days:
                continuous_learning_days_in_a_period = 1

    return current_power


def create_continuous_learning_series(continuous_learning_days):
    '''创建连续学习一定天数的学习状态布尔序列'''
    continuous_learning_series = []
    n = 0
    while n < continuous_learning_days:
        continuous_learning_series.append(True)
        n += 1
    return continuous_learning_series


def verify_continuous_learning_series(continuous_learning_days):
    '''用另一算法验证连续学习序列'''
    up_days = 0
    remainder = continuous_learning_days % power_up_period_days
    if remainder > power_up_threshold_days:
        up_days += (remainder - power_up_threshold_days)
    up_days += int(continuous_learning_days / power_up_period_days) * (
        power_up_period_days - power_up_threshold_days)
    expected_power = (initial_power) * (
        (1 + power_up_rate_over_threshold_days)**(up_days))
    return expected_power


# 连续学习365天

#设定条件
initial_power = 1
power_up_threshold_days = 3
power_up_period_days = 7
power_up_rate_over_threshold_days = 1 / 100

# 创建连续学习序列
learn_status_series_365 = create_continuous_learning_series(365)

# 执行模型并输出结果
current_power = day_up(learn_status_series_365, initial_power,
                       power_up_threshold_days, power_up_period_days,
                       power_up_rate_over_threshold_days)
print("\nCurrent : {:.4f}".format(current_power))

# 用另一算法验证连续学习序列并输出结果
expected_power = verify_continuous_learning_series(365)
print("Expected : {:.4f}".format(expected_power))

#################作业内容完成#################

## 以下不是作业要求的内容

## 测试模型工作情况的其他例子

# # series_1
# learn_status_series_1 = [
#     True, False, True, True, True, True, True, True, True, True, True, True,
#     True
# ]
# current_power = day_up(learn_status_series_1, initial_power,
#                        power_up_threshold_days, power_up_period_days,
#                        power_up_rate_over_threshold_days)
# print("\nCurrent : {}".format(current_power))
# # 验证series_1
# # 后面11天连续True, 一共up了4+1=5天
# up_days = 5
# expected_power = (initial_power) * (
#     (1 + power_up_rate_over_threshold_days)**(up_days))
# print("Expected : {}".format(expected_power))
