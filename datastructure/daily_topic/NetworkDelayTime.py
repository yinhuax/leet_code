#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/2 6:41
# @File    : NetworkDelayTime.py

"""
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/network-delay-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        深度优先遍历, 超时
        :param times:
        :param n:
        :param k:
        :return:
        """
        from collections import defaultdict
        # 先构建图

        graph = defaultdict(list)
        for v, u, w in times:
            graph[v].append((u, w))

        distance = {node: float('inf') for node in range(1, n + 1)}
        self.dfs(graph, distance, k, 0)

        totalTime = max(distance.values())
        return -1 if totalTime == float('inf') else totalTime

    def dfs(self, graph, distance, node, timeSum):
        if timeSum > distance[node]:  # 信号已经到达此节点
            return

        distance[node] = timeSum
        for neighbor, time in sorted(graph[node]):
            self.dfs(graph, distance, neighbor, timeSum + time)

    def networkDelayTime1(self, times: List[List[int]], n: int, k: int) -> int:
        """
        广度优先遍历
        :param times:
        :param n:
        :param k:
        :return:
        """
        from collections import defaultdict
        from collections import deque
        # 先构建图

        graph = defaultdict(list)
        for v, u, w in times:
            graph[v].append((u, w))

        deque = deque()
        deque.appendleft((k, 0))
        visited = {k: 0}

        while deque:
            cur_node, cur_time = deque.pop()
            for node, time in graph[cur_node]:
                t = cur_time + time
                if node not in visited or t < visited[node]:
                    visited[node] = t
                    deque.appendleft((node, t))

        return max(visited.values()) if len(visited) == n else -1
