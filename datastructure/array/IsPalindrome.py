#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 6:19
# @File    : IsPalindrome.py
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
"""


class IsPalindrome(object):

    def __init__(self):
        pass

    def isPalindrome(self, s: str) -> bool:
        """
        双指针，有效字符串判断，忽略字母大小写
        :param s:
        :return:
        """
        if not s:
            return True

        letter_set = set([chr(i) for i in range(97, 123)])
        number_set = set([str(i) for i in range(10)])
        palindrome_set = letter_set | number_set

        left, right = 0, len(s) - 1

        while left < right:
            if s[left].lower() not in palindrome_set:
                left += 1
                continue

            if s[right].lower() not in palindrome_set:
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return s[left].lower() == s[right].lower()

    def isPalindrome1(self, s: str) -> bool:
        if not s:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return s[left].lower() == s[right].lower()


if __name__ == '__main__':
    print(IsPalindrome().isPalindrome1("9,8"))
