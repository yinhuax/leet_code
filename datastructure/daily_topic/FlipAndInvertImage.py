#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/24 7:55
# @File    : FlipAndInvertImage.py
from typing import List

"""
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flipping-an-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """
        一次遍历，双指针做法
        :param A:
        :return:
        """
        n = len(A)
        m = len(A[0])
        for i in range(n):
            left = 0
            right = m - 1
            while left < right:
                A[i][left], A[i][right] = A[i][right], A[i][left]
                A[i][left] = A[i][left] ^ 1
                A[i][right] = A[i][right] ^ 1
                left += 1
                right -= 1

            if (m - 1) % 2 == 0:
                A[i][left] = A[i][left] ^ 1

        return A


if __name__ == '__main__':
    print(Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
