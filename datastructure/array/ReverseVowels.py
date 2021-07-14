#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 6:40
# @File    : ReverseVowels.py
"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

LC 反转字符串中的元音字母
"""


class ReverseVowels(object):

    def __init__(self):
        pass

    def reverseVowels(self, s: str) -> str:
        vowels = set(list(['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']))
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            while left < right and not s[left] in vowels:
                left += 1

            while left < right and not s[right] in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)


if __name__ == '__main__':
    print(ReverseVowels().reverseVowels('hello'))
