#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/1 7:36
# @File    : MaxVowels.py
"""
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        """
        维持一个大小为k的元音数量滑动数组
        :param s:
        :param k:
        :return:
        """
        vowels = set(list(['a', 'e', 'i', 'o', 'u']))

        counter = 0
        for i in range(k):
            if s[i] in vowels:
                counter += 1
        max_count = counter

        for j in range(k, len(s)):
            if s[j] in vowels:
                counter += 1

            if s[j - k] in vowels:
                counter -= 1

            max_count = max(max_count, counter)

        return max_count


if __name__ == '__main__':
    print(Solution().maxVowels(s="tryhard", k=4))
