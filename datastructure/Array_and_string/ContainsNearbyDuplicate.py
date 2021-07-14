#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 16:22
# @File    : ContainsNearbyDuplicate.py
from typing import List

"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-lockup-table/xhn7c6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class ContainsNearbyDuplicate(object):

    def __init__(self):
        pass

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        哈希表
        :param nums:
        :param k:
        :return:
        """
        ans = dict()
        for i in range(len(nums)):
            if nums[i] in ans:
                dif = i - ans[nums[i]]
                if dif <= k:
                    return True

            ans[nums[i]] = i

        return False


if __name__ == '__main__':
    print(ContainsNearbyDuplicate().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
