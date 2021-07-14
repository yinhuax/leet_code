#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/28 19:09
# @File    : EqualSubstring.py
"""
给你两个长度相同的字符串，s 和 t。

将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/get-equal-substrings-within-budget
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        滑动窗口
        :param s:
        :param t:
        :param maxCost:
        :return:
        """
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            # 字符相同，不需要花费预算
            if s[right] == t[right]:
                pass
            else:
                maxCost -= abs(ord(s[right]) - ord(t[right]))

            while maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


if __name__ == '__main__':
    print(Solution().equalSubstring(s="abcd", t="cdef", maxCost=0))
