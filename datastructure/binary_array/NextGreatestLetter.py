#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 14:16
# @File    : NextGreatestLetter.py
from typing import List

"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：

如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xeiuui/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        二分查找
        :param letters:
        :param target:
        :return:
        """
        left, right = 0, len(letters) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1

        return letters[left] if letters[left] > target else letters[0]


if __name__ == '__main__':
    print(Solution().nextGreatestLetter(["c", "f", "j"], 'c'))
