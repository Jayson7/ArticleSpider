#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
import hashlib
import re
import webbrowser
from webbrowser import Chrome


def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def extract_num(text):
    # 字符串中提取数字
    match_re = re.match(r'.*?(\d+).*', text)
    if match_re:
        nums = match_re.group(1)
    return nums


def webtest():
    # webbrowser.open("http://jobbole.com", new=0, autoraise=1)
    # webbrowser.open_new("http://jobbole.com")
    # webbrowser.open_new_tab("http://jobbole.com")
    webbrowser.register(name="chrome", klass=Chrome)
    webbrowser.get('chrome').open("http://jobbole.com")
        # .open('www.baidu.com', new=1, autoraise=True)

    chromePath = r'你的浏览器目录'  # 例如我的：C:\***\***\***\***\Google\Chrome\Application\chrome.exe
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))  # 这里的'chrome'可以用其它任意名字，如chrome111，这里将想打开的浏览器保存到'chrome'
    webbrowser.get('chrome').open('www.baidu.com', new=1, autoraise=True)


def choose(bool, a, b):
    return (bool and a or [b])[0]


def reversed(sequence):
    x = []
    for i in range(len(sequence)-1, -1, -1):
        # print(i)
        x.append(sequence[i])
        # x = sequence[i]
        # print(sequence[i])
    return x


def to_list(t):
        return [i if not isinstance(i, tuple) else to_list(i) for i in t]

#
# def to_list(t):
#     return [i for i in t]

if __name__ == '__main__':
    # webtest()
    # print(get_md5("http://jobbole.com"))
    # print(1)

    # print(choose(True, 1, 2))
    # print(forxinreversed([1, 2, 3, 3, 4, 5]))
    # sequence = [1, 2, 3, 4, 5]
    # sequence.reverse()
    # print(sequence)
    # x = [sequence[i] for i in range(len(sequence)-1, -1, -1)]
    # print(x)

    # print(int('1234'))
    # print(float(12))
    # print(str(98))
    # print(list('abcd'))
    # print(dict.fromkeys(['name', 'age']))
    # print(tuple([1, 2, 3, 4]))

    # a_list = [1, 2, [1, 2, 3], 3, 4, 5]
    # print(tuple(a_list))
    # t = tuple(a_list)
    # t = (1, 2, (1, 2, 3), 3, 4)
    # print(t)
    # print(to_list(t))

    # 10
    # L1 = [4, 1, 3, 2, 3, 5, 1]
    # L2 = []
    # [L2.append(i) for i in L1 if i not in L2]
    # print(L2)

    from copy import deepcopy
    L1 = [1, [1, 2, 3], 2, 3]
    print("before copy L1: ", L1)
    L2 = L1.copy()
    L2[1][2] = 1
    print("after copy L2: ", L2)
    print("after copy L1: ", L1)
    L1 = [3, [3, 4, 5], 4, 5]
    print("before deepcopy L1: ", L1)
    L2 = deepcopy(L1)
    L2[1][2] = 1
    print("after deepcopy L2: ", L2)
    print("after deepcopy L1: ", L1)
