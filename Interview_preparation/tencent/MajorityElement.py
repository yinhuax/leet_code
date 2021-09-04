#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/4 16:23
# @File    : MajorityElement.py
from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        """
        计数法，空间复杂度o(n)
        """

        ans_dict = dict()
        for num in nums:
            ans_dict[num] = ans_dict.get(num, 0) + 1

        return max(zip(ans_dict.values(), ans_dict.keys()))[1]

    def majorityElement1(self, nums: List[int]) -> int:
        """
        投票方式
        :param nums:
        :return:
        """
        candidates = 0
        count = 0
        for num in nums:
            if count == 0:
                candidates = num

            count += 1 if candidates == num else -1
        return candidates


if __name__ == '__main__':
    print(Solution().majorityElement1([2, 2, 1, 1, 1, 2, 2]))
