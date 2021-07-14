#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/19 16:44
# @File    : DailyTemperatures.py
from typing import List


class DailyTemperatures(object):

    def __init__(self):
        pass

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 单调栈
        result = [0] * len(T)
        stack = []
        for i in range(len(T)):
            temperature = T[i]
            while stack and T[stack[-1]] < temperature:
                cur_index = stack.pop()
                result[cur_index] = i - cur_index
            stack.append(i)

        return result


if __name__ == '__main__':
    print(DailyTemperatures().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
