#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 22:11
# @File    : Racecar.py
"""
你的赛车起始停留在位置 0，速度为 +1，正行驶在一个无限长的数轴上。（车也可以向负数方向行驶。）

你的车会根据一系列由 A（加速）和 R（倒车）组成的指令进行自动驾驶 。

当车得到指令 "A" 时, 将会做出以下操作： position += speed, speed *= 2。

当车得到指令 "R" 时, 将会做出以下操作：如果当前速度是正数，则将车速调整为 speed = -1 ；否则将车速调整为 speed = 1。  (当前所处位置不变。)

例如，当得到一系列指令 "AAR" 后, 你的车将会走过位置 0->1->3->3，并且速度变化为 1->2->4->-1。

现在给定一个目标位置，请给出能够到达目标位置的最短指令列表的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/race-car
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    def racecar(self, target: int) -> int:
        def race(t):
            if t not in dp:
                n = t.bit_length()
                if (1 << n) - 1 == t:  # 如果刚好是全A指令就能到达的，如1/3/7
                    dp[t] = n
                else:  # 先n次A到达2^n-1后再R，已操作n+1次，然后转换为从2^n-1到t的正向问题的指令次数
                    dp[t] = n + 1 + race((1 << n) - 1 - t)
                    for m in range(n - 1):  # 2^m < 2^(n-1)
                        # 先n-1次A到达2^(n-1)-1后再R，然后m次A往回走，再R变为正向，已指令n-1+2+m次，
                        # 接着转换为剩余差值即t-(2^(n-1)-1)+(2^m-1)的正向问题即可
                        dp[t] = min(dp[t], n + m + 1 + race(t - (1 << n - 1) + (1 << m)))
            return dp[t]

        dp = {0: 0}
        return race(target)
