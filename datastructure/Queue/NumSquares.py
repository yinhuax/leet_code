#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/18 22:31
# @File    : NumSquares.py


class NumSquares(object):

    def numSquares(self, n: int) -> int:
        # 最优化子问题
        # 1. 使用广度优先遍历寻找最小值
        # 2. dp 寻找
        from collections import deque
        queue = deque()
        queue.append(n)
        visited = set()

        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                targets = [cur - i * i for i in range(1, int(cur ** 0.5) + 1)]
                for target in targets:
                    if target == 0:
                        return step + 1

                    if target not in visited:
                        queue.append(target)
                        visited.add(target)

            step += 1

        return 0

    def numSquares1(self, n: int) -> int:
        # dp
        square_nums = [i ** 2 for i in range(0, int(n ** 0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


if __name__ == '__main__':
    print(NumSquares().numSquares(12))
