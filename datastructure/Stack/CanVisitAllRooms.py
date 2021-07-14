#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/14 22:46
# @File    : CanVisitAllRooms.py
from typing import List


class CanVisitAllRooms(object):

    def __init__(self):
        pass

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        深度优先遍历
        :param rooms:
        :return:
        """
        # 判断该钥匙是否已经使用
        seen = set()

        def dfs(cur_room):
            if cur_room in seen:
                return

            seen.add(cur_room)
            for room in rooms[cur_room]:
                dfs(room)

        dfs(0)
        return len(seen) == len(rooms)

    def canVisitAllRooms1(self, rooms: List[List[int]]) -> bool:
        """
        广度优先遍历
        :param rooms:
        :return:
        """
        from collections import deque
        queue = deque()
        queue.append(0)
        seen = set()
        seen.add(0)

        while queue:
            for _ in range(len(queue)):
                cur_room = queue.popleft()
                for room in rooms[cur_room]:
                    if room not in seen:
                        queue.append(room)
                        seen.add(room)
        return len(seen) == len(rooms)


if __name__ == '__main__':
    print(CanVisitAllRooms().canVisitAllRooms1([[1, 3], [3, 0, 1], [2], [0]]))
