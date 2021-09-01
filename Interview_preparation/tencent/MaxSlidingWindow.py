#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/31 17:10
# @File    : MaxSlidingWindow.py
from typing import List

"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MaxHeap(object):

    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.li = [None] * maxSize
        self.count = 0

    def length(self):
        # 求数组的长度
        return self.count

    def show(self):
        if self.count <= 0:
            print("null")
        else:
            print(self.li[:self.count])

    def push(self, value):
        if self.count >= self.maxSize:  # 判断是否数组越界
            raise Exception("full")

        self.li[self.count] = value  # 将新节点增加到最后
        self._shift_up(self.count)  # 递归构建大顶堆
        self.count += 1

    def _shift_up(self, index):
        # 往大顶堆中添加元素，并保证根节点是最大值:
        # 1. 增加新的值到最后一个节点
        # 2. 与父节点比较，如果比父节点值大，则交换
        if index > 0:
            parent = (index - 1) // 2  # 找到根节点
            # 交换节点
            if self.li[index][0] > self.li[parent][0]:
                self.li[parent], self.li[index] = self.li[index], self.li[parent]
                # 继续递归从底网上判断
                self._shift_up(parent)

    def pop(self):
        # 弹出堆顶节点
        # 1. 删除根节点，将最后一个节点作为根节点
        # 2. 判断根节点与左右节点的大小，交换左右节点较大的
        if not self.count:
            raise Exception("null")

        value = self.li[0]
        self.count -= 1
        self.li[0] = self.li[self.count]  # 将最后一个值变为第一个
        self._shift_down(0)
        return value

    def _shift_down(self, index):
        left, right = 2 * index + 1, 2 * index + 2

        max_index = index
        if left < self.length() and self.li[left][0] > self.li[max_index][0]:
            max_index = left

        if right < self.length() and self.li[right][0] > self.li[max_index][0]:
            max_index = right

        if max_index != index:
            self.li[max_index], self.li[index] = self.li[index], self.li[max_index]
            return self._shift_down(max_index)


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        构建大顶堆
        :param nums:
        :param k:
        :return:
        """
        # 先对前k个数据构建大顶堆
        n = len(nums)
        head = MaxHeap(n)
        for i in range(k):
            head.push((nums[i], i))

        # 保存滑动窗口最大值
        ans = [head.li[0][0]]
        for j in range(k, len(nums)):
            head.push((nums[j], j))
            while head.li[0][1] <= (j - k):
                head.pop()

            ans.append(head.li[0][0])
        return ans


if __name__ == '__main__':
    print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
