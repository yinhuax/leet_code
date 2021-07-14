#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 18:42
# @File    : TopK_Heap.py


class TopK_Heap(object):

    def __init__(self):
        pass

    def topKHeap(self, nums, K):
        """
        TopK 问题，小顶堆实现
        :param nums:
        :param K:
        :return:
        """
        n = len(nums)
        heap = nums[:K]
        # 建立含K个元素的小顶堆
        for i in range(K // 2 - 1, - 1, -1):
            self.build_head(i, K - 1, heap)

        print(heap)
        # 若K之后的元素大于根节点，则将该元素与跟节点交换，在做一次调整
        for j in range(K, n):
            # 找到前K大的数
            if nums[j] > heap[0]:
                heap[0] = nums[j]
                self.build_head(0, K - 1, heap)

        print(heap)
        return heap[0]

    def build_head(self, i, n, nums):
        left, right = 2 * i + 1, 2 * i + 2
        large_index = i
        if left <= n and nums[left] < nums[large_index]:
            large_index = left

        if right <= n and nums[right] < nums[large_index]:
            large_index = right
        # 找到三个元素中，最小的节点
        # 如果最小节点不等于当前根节点，需要和根节点交换位置，并重新调整小顶堆

        if large_index != i:
            nums[large_index], nums[i] = nums[i], nums[large_index]
            self.build_head(large_index, n, nums)


if __name__ == '__main__':
    print(TopK_Heap().topKHeap([1, 3, 7, 6, 5, 9, 8], 5))
