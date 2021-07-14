#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 7:18
# @File    : RemoveDuplicates2.py
from typing import List

"""
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

说明：

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下：

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-array/x9nivs/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        双指针+计数
        :param nums:
        :return:
        """
        left = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[left] = nums[i]
                left += 1

        return left

    def removeDuplicates1(self, nums: List[int]) -> int:
        k = 2
        i = 0
        for n in nums:
            if i < k or n != nums[i - k]:
                nums[i] = n
                i += 1

        print(nums)
        return i


if __name__ == '__main__':
    print(Solution().removeDuplicates1([1, 1, 1, 2, 2, 3]))
