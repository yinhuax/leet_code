#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/19 6:27
# @File    : LongestOnes.py
from typing import List

"""
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。

 

示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释： 
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        N = len(A)
        res = 0
        left, right = 0, 0
        zeros = 0
        while right < N:
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res

    def longestOnes1(self, A: List[int], K: int) -> int:
        """
        二分查找法，也就是说，
        我们需要找到最小的满足 (1)(1) 式的 left。由于数组 A 中仅包含 0/1，
        因此前缀和数组是一个单调递增的数组，我们就可以使用二分查找的方法得到left。

        :param A:
        :param K:
        :return:
        """
        n = len(A)
        P = [0]
        for num in A:
            P.append(P[-1] + (1 - num))

        res = 0
        for right in range(len(A)):
            left = self.binary_search_left(P, P[right + 1] - K)
            res = max(res, right - left + 1)

        return res

    def binary_search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    print(Solution().longestOnes1(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))
