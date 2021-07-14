#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 15:31
# @File    : MinWindow.py

"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        """
        滑动窗口
        :param s:
        :param t:
        :return:
        """
        # 使用2个哈希表记录 2个字符出现的次数
        need_dict = dict()
        window_dict = dict()
        for t_i in t:
            need_dict.setdefault(t_i, 0)
            need_dict[t_i] += 1

        left, right = 0, 0
        start = 0
        valid = 0  # 验证window是否满足need条件，表示满足条件的字符个数
        length = len(s) + 1
        while right < len(s):
            c = s[right]
            right += 1
            if c in need_dict:
                window_dict.setdefault(c, 0)
                window_dict[c] += 1
                if window_dict[c] == need_dict[c]:
                    valid += 1

            while valid == len(need_dict):
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1
                # 更新窗口
                if d in need_dict:
                    if window_dict[d] == need_dict[d]:
                        valid -= 1
                    window_dict[d] -= 1

        return s[start:start + length] if length != len(s) + 1 else ''


if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
