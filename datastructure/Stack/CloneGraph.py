#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/20 15:10
# @File    : CloneGraph.py


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph(object):
    """
    克隆图
    """

    def __init__(self):
        pass

    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = dict()

        def dfs(cur_node):
            if not cur_node:
                return

            if cur_node in visited:
                return visited[cur_node]

            clone_node = Node(cur_node.val)
            visited[cur_node] = clone_node
            for _ in cur_node.neighbors:
                clone_node.neighbors.append(dfs(_))

            return clone_node

        return dfs(node)

    def cloneGraph1(self, node: 'Node') -> 'Node':
        if not node:
            return

        from collections import deque
        # bfs 广度优先遍历，层次克隆
        visited = dict()
        queue = deque()
        queue.append(node)

        clone_node = Node(node.val, [])
        visited[node] = clone_node
        while queue:
            cur_node = queue.popleft()

            for _ in cur_node.neighbors:
                if _ not in visited:
                    visited[_] = Node(_.val, [])
                    queue.append(_)
                visited[cur_node].neighbors.append(visited[_])

        return clone_node


if __name__ == '__main__':
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    map_set = dict()
    for i in range(len(adjList)):
        node = Node(i + 1)
        map_set[i + 1] = node
        for cur_value in adjList[i]:
            if cur_value not in map_set:
                neighbor_node = Node(cur_value)
            else:
                neighbor_node = map_set[cur_value]
            node.neighbors.append(neighbor_node)

    print(CloneGraph().cloneGraph(map_set[1]).val)
