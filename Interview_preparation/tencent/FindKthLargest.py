#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/28 12:56
# @File    : FindKthLargest.py
from typing import List

"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

 

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class QuickSort(object):
    # 快排实现

    def sort(self, nums: List[int], left, right):

        if left >= right:
            return

        # 定义一个哨兵
        x = nums[(left + right) // 2]

        i = left
        j = right
        while i < j:
            while nums[i] < x:
                i += 1
            while nums[j] > x:
                j -= 1

            if i < j:
                # 交互位置
                nums[i], nums[j] = nums[j], nums[i]
                # 避免重复元素死循环
                if nums[i] == nums[j] == x:
                    i += 1
                    j -= 1

        self.sort(nums, left, j)
        self.sort(nums, j + 1, right)


class MergeSort(object):
    """
    归并排序实现
    """

    def sort(self, nums, left, right):
        if left >= right:
            return

        mid = left + right >> 1
        self.sort(nums, left, mid)
        self.sort(nums, mid + 1, right)
        self.merge(nums, left, right, mid)

    def merge(self, nums, left, right, mid):
        """
        分治
        :param nums:
        :param left:
        :param right:
        :param mid:
        :return:
        """
        i = left
        j = mid + 1
        tmp = []
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1

        # 提前结束处理
        tmp.extend(nums[i: mid + 1])
        tmp.extend(nums[j: right + 1])
        nums[left: right + 1] = tmp


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # MergeSort().sort(nums, 0, len(nums) - 1)
        # 构建小顶堆
        head = nums[:k]
        n = len(nums)
        for i in range(k // 2 - 1, -1, -1):
            # 从第一个非叶子节点开始构建小顶堆
            self.build_head(i, k - 1, head)

        for j in range(k, n):
            if nums[j] > head[0]:
                head[0] = nums[j]
                # 重新调整小顶堆
                self.build_head(0, k - 1, head)

        return head[0]

    def build_head(self, i, n, head):
        """
        小顶堆构建
        :param i:
        :param n:
        :param head:
        :return:
        """
        left, right = 2 * i + 1, 2 * i + 2
        min_index = i

        if left <= n and head[left] < head[min_index]:
            min_index = left
        if right <= n and head[right] < head[min_index]:
            min_index = right

        if min_index != i:
            head[min_index], head[i] = head[i], head[min_index]
            self.build_head(min_index, n, head)


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], k=2))
