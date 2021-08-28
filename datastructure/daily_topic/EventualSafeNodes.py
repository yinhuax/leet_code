#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/5 16:11
# @File    : EventualSafeNodes.py
from typing import List

"""
在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。

对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。

返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。

该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，满足 (i, j) 是图的一条有向边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-eventual-safe-states
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        深度优先遍历，记录能够到达终点的节点，剪枝优化
        :param graph:
        :return:
        """
        # 记录能够走到最后的节点，用于剪枝
        color = [0] * len(graph)

        def dfs(cur_i):
            if color[cur_i] > 0:
                return color[cur_i] == 2

            color[cur_i] = 1
            for y in graph[cur_i]:
                if not dfs(y):
                    return False
            color[cur_i] = 2
            return True

        return [i for i in range(len(graph)) if dfs(i)]


if __name__ == '__main__':
    print(Solution().eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))
