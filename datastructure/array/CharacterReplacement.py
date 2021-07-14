#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/28 20:25
# @File    : CharacterReplacement.py
"""
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，
总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。


注意：字符串长度 和 k 不会超过 104。

 

示例 1：

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        """
        替换后的最大重复字符
        :param s:
        :param k:
        :return:
        """
        if len(s) < 2:
            return len(s)

        # 滑动窗口，记录窗口中频次最多的字符，判断right - left - max_count <= k是否成立
        word_list = [0] * 26
        left, right = 0, 0
        res = 0
        max_count = 0
        while right < len(s):
            word_list[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, word_list[ord(s[right]) - ord('A')])
            right += 1

            while (right - left) > (max_count + k):
                # 收缩左边窗口
                word_list[ord(s[left]) - ord('A')] -= 1
                left += 1
            res = max(res, right - left)

        return res


if __name__ == '__main__':
    print(Solution().characterReplacement(s="AABABBA", k=1))
