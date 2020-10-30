# goat_car.py
# ab00b
# 2020.10.8

from random import randint
from time import perf_counter


def get_unchange_change_choice_results(options, remove_item_every_time,
                                       win_item, try_times):
    '''设定一组选项、中途剔除的一个选项、获胜选项、尝试次数, 
    输出中途剔除选项后改变选择/不改变选择的获胜次数, 以及该方法运行的时间'''
    start_time = perf_counter()
    unchanged_win_times = 0
    changed_win_times = 0
    # 尝试若干次
    for i in range(try_times):
        # 每次运行时的选项都复制自初始选项
        options_this_try = options[:]
        # 第一次随机选择
        first_choice = options_this_try[randint(0, len(options_this_try) - 1)]
        # 主持人去掉了一个山羊选项
        options_this_try.remove(remove_item_every_time)
        # 不更改选择的选项
        unchanged_choice = first_choice
        # 更改选择的话, 即再去掉最初的选项, 在剩下的的选项里随机选一个
        # 对于最初只有三个选项而言, 到这里其实只剩下一个可选项了, 必定选择到最后的一个选项
        options_this_try.remove(first_choice)
        changed_choice = options_this_try[randint(0,
                                                  len(options_this_try) - 1)]
        # 记录更改选择和不更改选择的结果
        if unchanged_choice == win_item:
            unchanged_win_times += 1
        if changed_choice == win_item:
            changed_win_times += 1
        end_time = perf_counter()
        time_spend = end_time - start_time
    return unchanged_win_times, changed_win_times, time_spend


# 开始测试
options = ['goat', 'car', 'goat']
# 测试更多初始选项的情况(非作业要求)
# options = ['goat', 'car', 'goat', 'goat', 'goat','goat']
try_times = 1000000
remove_item_every_time = 'goat'
win_item = 'car'

unchanged_win_times, changed_win_times, time_spend = get_unchange_change_choice_results(
    options, remove_item_every_time, win_item, try_times)
print("\nTotally try {} times in {:03.2f} s".format(try_times, time_spend))
print("Unchanged win times: {}, win rate:{:03.2f}%".format(
    unchanged_win_times, unchanged_win_times / try_times * 100))
print("Changed win times:   {}, win rate:{:03.2f}%".format(
    changed_win_times, changed_win_times / try_times * 100))
