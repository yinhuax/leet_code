#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 12:34
# @File    : CountSubstrings.py
from typing import List

"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 
示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def countSubstrings(self, s: str) -> int:
        """
        dp[i][j] 表示字符串i -> j 是否为回文字符

        转移方程如果 dp[i + 1][j - 1] 为回文子串，且 s[i] == s[j] ，则 dp[i][j]也为回文子串
        :param tasks:
        :param n:
        :return:
        """
        dp = [[False for i in range(len(s))] for _ in range(len(s))]

        count = 0
        for i in range(len(s)):
            for j in range(i + 1):
                # 单字符情况
                if i == j:
                    dp[j][i] = True
                    count += 1
                # 两个字符的情况
                elif i - j == 1 and s[i] == s[j]:
                    dp[j][i] = True
                    count += 1
                # 多字符的情况
                elif i - j > 1 and dp[j + 1][i - 1] and s[i] == s[j]:
                    dp[j][i] = True
                    count += 1

        return count


if __name__ == '__main__':
    print(Solution().countSubstrings("aaa"))
