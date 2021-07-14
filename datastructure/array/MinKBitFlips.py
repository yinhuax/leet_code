#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/28 21:26
# @File    : MinKBitFlips.py
from typing import List

"""
在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。

返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。

 

示例 1：

输入：A = [0,1,0], K = 1
输出：2
解释：先翻转 A[0]，然后翻转 A[2]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        """
        K连续位最小翻转次数
        :param A:
        :param K:
        :return:
        """
        # 贪心算法
        # 从第i个0开始翻转后面i + k 个数字
        n = len(A)
        ans = 0
        for i in range(n):
            if A[i] == 0:
                if i + K > n:
                    return -1
                for j in range(K):
                    A[i + j] ^= 1
                ans += 1
        return ans

    def minKBitFlips1(self, A, K):
        windowFlip = res = 0
        for i in range(len(A)):
            if i >= K and A[i - K] == 2:
                windowFlip -= 1
            if (windowFlip % 2) == A[i]:
                if i + K > len(A):
                    return -1
                A[i] = 2
                windowFlip, res = windowFlip + 1, res + 1
        return res


if __name__ == '__main__':
    print(Solution().minKBitFlips1(A=[0, 1, 0, 0], K=2))
