#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/28 18:58
# @File    : IsMonotonic.py
from typing import List

"""
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/monotonic-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        """
        判断数组是否单调
        :param A:
        :return:
        """
        return all([True if A[i] >= A[i - 1] else False for i in range(1, len(A))]) or all(
            [True if A[i] <= A[i - 1] else False for i in range(1, len(A))])


if __name__ == '__main__':
    print(Solution().isMonotonic([1, 2, 2, 3]))
