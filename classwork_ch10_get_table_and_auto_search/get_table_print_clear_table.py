# get_table_print_clear_table
# ab00b

import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    """抓取给定的网址的文本"""
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return ""


def get_html_table_content(html_text):
    """输入html内容,调用soup库解析,返回一个表格内容列表和一个包含每列名称的列表"""
    soup = BeautifulSoup(html_text, "html.parser")
    tr_data = soup.find_all("tr")
    all_data = []
    column_names = []
    # 尝试从每个tr的th标签中寻找表头
    for tr in tr_data:
        lth = tr.find_all("th")
        if len(lth) == 0:
            continue
        for th in lth:
            column_names.append(str(th.string).strip())
    # 判断有没有找到表头
    if column_names == []:
        #  如果找不到th标签, 则认为表头在第一个tr中,做出标记以便后面删除这一项
        flag_col_name_in_tr_data_1 = True
        # 下面两种找表头的方法都可以,
        # 第一种更简洁, 而且在后面的例子中表现更好(方法二对某些列名称读取成了None)
        # 方法一
        column_names = tr_data[0].text.strip().split(" ")
        # 方法二
        # ltd = tr_data[0].find_all("td")
        # if len(ltd) == 0:
        #     pass
        # else:
        #     for td in ltd:
        #         column_names.append(str(td.string).strip())
    else:
        flag_col_name_in_tr_data_1 = False
    # 填充数据
    for tr in tr_data:
        ltd = tr.find_all("td")
        if len(ltd) == 0:
            continue
        single_data = []
        for td in ltd:
            single_data.append(str(td.string).strip())
        all_data.append(single_data)
    # 如果表头在第一个tr中,删除这一项
    if flag_col_name_in_tr_data_1 == True:
        all_data.pop(0)
    # 返回一个表格内容列表和一个包含每列名称的列表
    return all_data, column_names


def print_clear_list(all_data, column_names, num=-1):
    """给定列表,列名称,打印出一个整洁的列表(对齐每一列,且能处理中文),
    num指定打印前几项,默认num=-1即打印所有项"""
    if num == -1:
        num = len(all_data)
    # 如果给定num超过总项数, 则打印所有项,并标记以便于在打印结束后额外生成一句提示
    if num > len(all_data):
        num = len(all_data)
        flag_print_over_max = True
    else:
        flag_print_over_max = False
    column_num = len(column_names)
    # 检测内容的哪些列包含中文, 储存中文列序号, 便于后面排版
    chn_col_indexs = set()
    for i in range(0, column_num):
        for ch in all_data[0][i]:
            if "\u4e00" <= ch <= "\u9fa5":
                chn_col_indexs.add(i)
    # 生成每列宽,等于该列所有数据中的最大字符长度+3
    each_column_width = [
        max([len(str(each_univ[i])) for each_univ in all_data[: num + 1]]) + 3
        for i in range(0, column_num)
    ]
    # 废弃, 生成从左边起的累积列宽
    # culmulative_column_width = [
    #     sum(each_column_width[:i+1]) for i in range(0, column_num)
    # ]
    # 打印列名称栏, 居中, 宽度由之前得到的的列宽数据规定
    print(
        "".join(
            [
                "".join(["{:^", str(each_column_width[i]), "}"]).format(column_names[i])
                for i in range(0, column_num)
            ]
        )
    )
    for i in range(0, num):
        try:
            # 打印单项数据, 左对齐, 宽度由之前得到的的列宽数据规定
            single_data = all_data[i]
            single_data_string = "".join(
                [
                    "".join(["{:<", str(each_column_width[i]), "}"]).format(
                        single_data[i]
                    )
                    for i in range(0, column_num)
                ]
            )
            # 对于含中文的列, 为了排版美观, 要把中文前后填充的单个空格占位符替换成两个空格,
            # 替换的数量由列宽(最大)减去原有的中文字符数量决定
            for chn_col_index in chn_col_indexs:
                single_data_string = single_data_string.replace(
                    " ",
                    "  ",
                    each_column_width[chn_col_index] - len(single_data[chn_col_index]),
                )
            # 打印单项数据
            print(single_data_string)
        # 若打印数据出错, 指示出错的条目
        except:
            print("Error: line " + str(i))
    # 如果给定num超过总项数,在此时额外生成一句提示
    if flag_print_over_max == True:
        print("请求数量超过了最大数据量,将显示所有项目")


def main():
    # 世界大学排行
    # url = "https://news.sina.com.cn/zt_d/qswur2020/"
    # 中国大学排行
    url = "http://www.qianmu.org/2020USNEWS%E4%B8%AD%E5%9B%BD%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D"
    html_text = get_html_text(url)
    allUniv, column_names = get_html_table_content(html_text)
    print_clear_list(allUniv, column_names, 10)


main()

