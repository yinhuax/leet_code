#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 15:42
# @File    : LongestValidParentheses.py

"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

"""


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        """
        使用栈
        :param s:
        :return:
        """
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res

    def longestValidParentheses1(self, s: str) -> int:
        """
        使用动态规划
        当s[i] == ')' 时  1.判断s[i - 1] 是否等于'(' 如果s[i - 1] 等于 '(', dp[i] = dp[i - 2] + 2
                        2. 如果s[i - 1] 等于 ')' 并且s[i - 1 - dp[i - 1]] 为 '(', 那么dp[i] = dp[i - 1 - dp[i - 1]] + 2 + dp[i - 1]
        当s[i] == '(' 是赋值为0
        :param s:
        :return:
        """
        dp = [0] * len(s)
        res = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ')' and i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                    dp[i] = dp[i - dp[i - 1] - 2] + 2 + dp[i - 1]

                res = max(res, dp[i])
        return res


if __name__ == '__main__':
    print(Solution().longestValidParentheses1(")()())"))
