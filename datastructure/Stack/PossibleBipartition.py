#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/24 23:36
# @File    : PossibleBipartition.py
from typing import List

"""
给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。

每个人都可能不喜欢其他人，那么他们不应该属于同一组。

形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。

当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/possible-bipartition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        """
        使用图，存储节点以及邻接节点信息
        :param N:
        :param dislikes:
        :return:
        """
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c

            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all([dfs(i) for i in range(1, N + 1) if i not in color])


if __name__ == '__main__':
    print(Solution().possibleBipartition(N=4, dislikes=[[1, 2], [1, 3], [2, 4]]))
