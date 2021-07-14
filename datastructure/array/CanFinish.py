#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/16 15:26
# @File    : CanFinish.py
from typing import List

"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        回溯算法
        :param numCourses:
        :param prerequisites:
        :return:
        """
        # 课程长度
        c_len = len(prerequisites)
        if c_len == 0:
            return True

        # 深度优先遍历
        # 记录是否访问过该节点
        # 使用三个状态记录，1. 0对应没有访问过  2. 1对应访问过 3. 2对应正在访问，如果遍历时遇到2状态的节点，表示存在环
        visited = [0 for i in range(numCourses)]

        # 逆邻接表
        inverse_adj = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            inverse_adj[second].add(first)

        for i in range(numCourses):
            if self._dfs(i, inverse_adj, visited):
                return False

        return True

    def _dfs(self, vertex, inverse_adj, visited):
        """
        返回表示是否有环
        :param vertex:
        :param inverse_adj:
        :param visited:
        :return:
        """
        if visited[vertex] == 2:
            return True

        if visited[vertex] == 1:
            return False

        visited[vertex] = 2
        for precursor in inverse_adj[vertex]:
            if self._dfs(precursor, inverse_adj, visited):
                return True

        visited[vertex] = 1
        return False
