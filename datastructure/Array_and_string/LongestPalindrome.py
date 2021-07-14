#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/23 19:55
# @File    : LongestPalindrome.py


class LongestPalindrome(object):

    def __init__(self):
        pass

    def longestPalindrome(self, s: str) -> str:
        """
        回溯算法，计算最大长度回文数
        :param s:
        :return:
        """
        n = len(s)
        self.res = ""

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j - i - 1:
                self.res = s[i + 1:j]

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res

    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = ""
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j + 1 <= 3 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    res = max(res, s[j:i + 1], key=len)
        return res


if __name__ == '__main__':
    print(LongestPalindrome().longestPalindrome("aacabdkacaa"))
