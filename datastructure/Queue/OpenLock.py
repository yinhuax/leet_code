#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/17 23:36
# @File    : OpenLock.py

# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
# 每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/queue-stack/kj48j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from collections import deque
from typing import List


class OpenLock(object):

    def __init__(self):
        pass

    def openLock(self, deadends: List[str], target: str) -> int:
        # 广度优先遍历、深度优先遍历
        queue = deque()
        queue.append("0000")

        visited = set()
        visited.add("0000")
        step = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return step

                if curr in deadends:
                    continue

                for j in range(len(curr)):
                    for temp in (-1, 1):
                        temp_j = (int(curr[j]) + temp) % 10
                        next_s = curr[:j] + str(temp_j) + curr[j + 1:]

                        if next_s not in visited:
                            visited.add(next_s)
                            queue.append(next_s)

            step += 1
        return -1

    def openLock1(self, deadends: List[str], target: str) -> int:
        # 广度优先遍历、深度优先遍历，优化计算
        dict_neighbors = {
            "0": "19",
            "1": "02",
            "2": "13",
            "3": "24",
            "4": "35",
            "5": "46",
            "6": "57",
            "7": "68",
            "8": "79",
            "9": "80"
        }
        queue = deque()
        queue.append("0000")

        visited = set()
        visited.add("0000")
        step = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return step

                if curr in deadends:
                    continue

                for j in range(len(curr)):
                    next_s1 = curr[:j] + dict_neighbors[curr[j]][0] + curr[j + 1:]
                    next_s2 = curr[:j] + dict_neighbors[curr[j]][1] + curr[j + 1:]
                    if next_s1 not in visited:
                        visited.add(next_s1)
                        queue.append(next_s1)

                    if next_s2 not in visited:
                        visited.add(next_s2)
                        queue.append(next_s2)
            step += 1
        return -1

    def openLock2(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        # 双向BFS + 缓存计算 + 使用集合代替列表遍历，提高效率，使用
        dict_neighbors = {
            "0": "19",
            "1": "02",
            "2": "13",
            "3": "24",
            "4": "35",
            "5": "46",
            "6": "57",
            "7": "68",
            "8": "79",
            "9": "80"
        }
        deadends = set(deadends)

        left = set()
        left.add("0000")

        right = set()
        right.add(target)

        step = 0

        while left:
            temp_set = set()
            # 每次都搜索节点较少的一边
            if len(left) > len(right):
                left, right = right, left

            for node in left:
                for i in range(4):
                    for change in dict_neighbors[node[i]]:
                        cur = node[:i] + change + node[i + 1:]
                        if cur in right:
                            return step + 1

                        if cur not in deadends:
                            deadends.add(cur)
                            temp_set.add(cur)

            step += 1
            left = temp_set

        return -1


if __name__ == '__main__':
    p = OpenLock()
    print(p.openLock(['8888'], '0009'))
