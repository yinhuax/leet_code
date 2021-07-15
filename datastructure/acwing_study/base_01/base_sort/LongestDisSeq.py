#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/15 7:42
# @File    : LongestDisSeq.py


class LongestDisSeq(object):

    def __init__(self):
        pass

    def get_max_length(self, arr):
        from collections import defaultdict
        # 左指针
        j = 0
        # 右指针移动
        max_length = 0
        # 记录当前窗口每个数字出现次数
        counter = defaultdict(int)
        for i in range(len(arr)):
            counter[arr[i]] += 1
            # 当出现重复元素时，移动左指针
            while counter[arr[i]] > 1:
                counter[arr[j]] -= 1
                j += 1

            max_length = max(max_length, i - j + 1)
        return max_length


if __name__ == '__main__':
    print(LongestDisSeq().get_max_length([1, 2, 2, 3, 5]))
