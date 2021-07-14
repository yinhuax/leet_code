#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 9:04
# @File    : CheckRecord.py
"""
给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。

学生出勤记录是只包含以下三个字符的字符串：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。

示例 1:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/student-attendance-record-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def checkRecord(self, n: int) -> int:
        """
        动态规划，
        dp[i][j][k] i 表示第i个字符，j 表示 A出现的次数， k表示L连续出现的次数
        合法状态
        1. 没有出现过A，且前2次没有出现L
        2. 没有出现过A，且最近一次是L
        3. 没有出现过A，且最近两次是L
        4. 出现过A，且前2次没有出现L
        5. 出现过A，且最近一次是L
        6. 出现过A，且最近两次是L
        :param n:
        :return:
        """

        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        dp[1][0][0] = 1  # P
        dp[1][0][1] = 1  # L
        dp[1][0][2] = 0
        dp[1][1][0] = 1  # A
        dp[1][1][1] = 0
        dp[1][1][2] = 0

        mod = 10 ** 9 + 7
        for i in range(2, n + 1):
            dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % mod
            dp[i][0][1] = dp[i - 1][0][0]
            dp[i][0][2] = dp[i - 1][0][1]
            dp[i][1][0] = (dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2]) % mod
            dp[i][1][1] = dp[i - 1][1][0]
            dp[i][1][2] = dp[i - 1][1][1]

            # 当前状态可由dp[i - 1][0][0] 转换而来
            dp[i][1][0] += (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % mod

        return sum([sum(i) for i in dp[-1]]) % mod

    def checkRecord1(self, n: int) -> int:
        """
        空间优化，观察可知，当前状态只和前面i - 1相关
        :param n:
        :return:
        """
        dp = [[0 for _ in range(3)] for _ in range(2)]
        dp[0][0] = 1  # P
        dp[1][0] = 1  # A
        dp[0][1] = 1  # L

        # cur = [[0 for _ in range(3)] for _ in range(2)]
        mod = 10 ** 9 + 7
        for i in range(2, n + 1):
            cur = [[0 for _ in range(3)] for _ in range(2)]
            cur[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % mod
            cur[0][1] = dp[0][0]
            cur[0][2] = dp[0][1]
            cur[1][0] = (dp[1][0] + dp[1][1] + dp[1][2] + dp[0][1] + dp[0][0] + dp[0][2]) % mod
            cur[1][1] = dp[1][0]
            cur[1][2] = dp[1][1]
            dp = cur

        return sum([sum(i) for i in dp]) % mod


if __name__ == '__main__':
    print(Solution().checkRecord1(3))
