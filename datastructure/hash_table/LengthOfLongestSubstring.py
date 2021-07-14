#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/5 0:14
# @File    : LengthOfLongestSubstring.py


class LengthOfLongestSubstring(object):

    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        使用双指针，加哈希表
        :param s:
        :return:
        """
        if not s:
            return 0

        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(max_len, cur_len)
            lookup.add(s[i])

        return max_len


if __name__ == '__main__':
    print(LengthOfLongestSubstring().lengthOfLongestSubstring("dvdf"))
