#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/26 15:43
# @File    : FindDuplicates.py
from typing import List

"""
数组中的重复数据
"""


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        使用额外空间，时间复杂度O(n)
        :param nums:
        :return:
        """
        from collections import defaultdict
        map_count = defaultdict(int)
        for i in range(len(nums)):
            map_count[nums[i]] += 1

        return [k for k, v in map_count.items() if v == 2]

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        if not nums: return []
        res = []
        n = len(nums)
        # 1<=num<=n 遍历到 num 则令第 num 个元素变成-num
        for i in range(n):
            num = abs(nums[i])
            # 如果第num个数字已经是负的 说明之前遇到过num 说明num出现两次
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return res


if __name__ == '__main__':
    print(Solution().findDuplicates2([4, 3, 2, 7, 8, 2, 3, 1]))
