#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/28 17:06
# @File    : MedianFinder.py
import heapq

"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import heapq as hq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 构造大顶堆、小顶堆，保持堆中数据平衡，中位数是大顶堆和小顶堆 下标为0的值
        self.minHeap = []
        self.maxHeap = []

    def build_head(self, i, n, head, is_max=False):
        """
        构建堆，默认为大顶堆
        :param i:
        :param n:
        :param head:
        :param is_max:
        :return:
        """
        left, right = 2 * i + 1, 2 * i + 2
        index = i
        if left <= n and (head[left] > head[index] if is_max else head[left] < head[index]):
            index = left

        if right <= n and (head[right] > head[index] if is_max else head[right] < head[index]):
            index = right

        if index != i:
            head[index], head[i] = head[i], head[index]
            return self.build_head(index, n, head, is_max)

    def handle_num(self, head, is_max=False):
        """
        添加元素
        :param head:
        :param is_max:
        :return:
        """
        n = len(head)
        for i in range(n // 2 - 1, -1, -1):
            # 从第一个非叶子节点开始构建小顶堆
            self.build_head(i, n - 1, head, is_max)

        for j in range(n - 1, -1, -1):
            head[0], head[j] = head[j], head[0]
            self.build_head(0, j - 1, head, is_max)

    def addNum(self, num: int) -> None:
        """
        添加元素
        :param num:
        :return:
        """
        # 小顶堆存储的是比较大的元素，如果比大元素中最小的还大，那么进入min_head
        # if not self.minHeap or num > self.minHeap[0]:
        #     self.minHeap.append(num)
        #     self.handle_num(self.minHeap, is_max=True)
        # else:
        #     self.maxHeap.append(num)
        #     self.handle_num(self.maxHeap, is_max=False)
        # #
        # # # 判断两边长度是否差距太大
        # if len(self.minHeap) - len(self.maxHeap) > 1:
        #     self.maxHeap.append(self.minHeap.pop(0))
        #     self.handle_num(self.maxHeap, is_max=False)
        # elif len(self.maxHeap) - len(self.minHeap) > 1:
        #     # self.minHeap.insert(0, self.maxHeap.pop(0))
        #     self.minHeap.append(self.maxHeap.pop(0))
        #     self.handle_num(self.minHeap, is_max=True)
        hq.heappush(self.maxHeap, (-num, num))
        _, max_num = hq.heappop(self.maxHeap)
        hq.heappush(self.minHeap, max_num)

        # 这个操作是为了让左边的大顶堆总是比右边的堆多一个数字
        if len(self.maxHeap) < len(self.minHeap):
            min_num = hq.heappop(self.minHeap)
            hq.heappush(self.maxHeap, (-min_num, min_num))

    def findMedian(self) -> float:
        """
        返回中位数
        :return:
        """
        # 总长度为奇数时，返回更长那边的下标0，相同时各取一个
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0][1]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0][1]


if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(-1)
    print(medianFinder.findMedian())
    medianFinder.addNum(-2)
    print(medianFinder.findMedian())
    medianFinder.addNum(-3)
    print(medianFinder.findMedian())
    medianFinder.addNum(-4)
    print(medianFinder.findMedian())
    medianFinder.addNum(-5)
    print(medianFinder.findMedian())
