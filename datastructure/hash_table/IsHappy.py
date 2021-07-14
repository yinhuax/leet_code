#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 14:35
# @File    : IsHappy.py


class IsHappy(object):

    def __init__(self):
        pass

    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        def compute(num):
            num = str(num)
            return sum([int(num[i]) ** 2 for i in range(len(num))])

        while True:
            n = compute(n)
            if n == 1:
                return True

            if n in seen:
                return False
            seen.add(n)


if __name__ == '__main__':
    print(IsHappy().isHappy(1))
