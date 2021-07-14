#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 21:31
# @File    : NumDistinct.py
"""
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        """
        动态规划：
        如果 s[i] == t[j]
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
        如果 s[i] != t[j]
            dp[i][j] = dp[i][j - 1]
        :param s:
        :param t:
        :return:
        """
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]

        for i in range(len(s) + 1):
            dp[0][i] = 1

        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().numDistinct(s="rabbbit", t="rabbit"))
