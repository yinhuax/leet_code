#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 17:08
# @File    : FindDuplicate.py
"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

 

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xe6xnr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List


class FindDuplicate(object):

    def __init__(self):
        pass

    def findDuplicate(self, nums: List[int]) -> int:
        """
        插入排序算法原理
        :param nums:
        :return:
        """
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[j] != j + 1:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        print(nums)
        return nums[-1]

    def findDuplicate1(self, nums: List[int]) -> int:
        """
        二分法
        :param nums:
        :return:
        """
        n = len(nums)
        left = 1
        right = n - 1
        while left < right:
            mid = (right - left) // 2 + left

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            # 如果小于等于4的个数大于4个，那么此时重复元素在[left, mid]区间中
            if cnt > mid:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    print(FindDuplicate().findDuplicate1(nums=[4, 3, 1, 4, 2]))
