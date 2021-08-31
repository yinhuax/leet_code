#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/31 1:20
# @File    : IsPalindrome.py

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。



"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        def is_str(cur_str):
            return cur_str.lower().isalnum()

        left, right = 0, len(s) - 1
        while left < right:
            while (not is_str(s[left])) and left < right:
                left += 1

            while (not is_str(s[right])) and right > left:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("0P"))
