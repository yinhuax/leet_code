#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 17:09
# @File    : NumDecodings.py
"""
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，从而得到 "AAA" ，
或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "6" 和 "06" 不同。

给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def numDecodings(self, s: str) -> int:
        """
        动态规划，
            分为以下四种情况：
                1. 如果i - 1 与 i能组成10 ~ 26之间的数
                    1. 如果组成的数是 10 or 20 dp[i] = dp[i - 2]
                    2. 如果组成的数是 11 ~ 26（不含20） dp[i] = dp[i - 1] + dp[i - 2]

                2. 如果第i - 1 与 i不能组成10 ~ 26的数
                    1. 如果第i位是0，不可编码 return 0
                    2. 如果第i位不是0， dp[i] = dp[i - 1]
        :param s:
        :return:
        """
        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(1, len(s)):
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] < '7'):
                if s[i] == '0':
                    dp[i + 1] = dp[i - 1]
                else:
                    dp[i + 1] = dp[i] + dp[i - 1]
            elif s[i] == '0':
                return 0
            else:
                dp[i + 1] = dp[i]

        # 涉及i - 2 所以使用n + 1的空间复杂度
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numDecodings("2611055971756562"))
