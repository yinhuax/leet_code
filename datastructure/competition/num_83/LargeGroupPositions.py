#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 22:15
# @File    : LargeGroupPositions.py
from typing import List

"""
在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。

我们称所有包含大于或等于三个连续字符的分组为 较大分组 。

找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。
"""


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 3:
            return []

        result = []
        left = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                if i == len(s) - 1 and i - left + 1 >= 3:
                    result.append([left, i])
            else:
                if i - left >= 3:
                    result.append([left, i - 1])
                left = i

        return result


if __name__ == '__main__':
    print(Solution().largeGroupPositions("abbxxxxzyy"))
