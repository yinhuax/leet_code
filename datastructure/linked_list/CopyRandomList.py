#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/8 6:16
# @File    : CopyRandomList.py

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        复制带随机指针的链表，使用遍历+队列方式，先生成next链表，使用hash表存储index信息
        :param head:
        :return:
        """

        if not head:
            return

        # 存储node -> new_node映射
        hash_table = dict()
        cur = head
        while cur:
            node = Node(cur.val)
            hash_table[cur] = node
            cur = cur.next

        cur = head
        while cur is not None:
            hash_table[cur].next = hash_table[cur.next] if cur.next else None
            hash_table[cur].random = hash_table[cur.random] if cur.random else None
            cur = cur.next

        return hash_table[head]

    def copyRandomList1(self, head: 'Node') -> 'Node':
        """
        创建一个节点，放在原节点后面，额外空间O（0）
        :param head:
        :return:
        """
        if not head:
            return

        cur = head
        # 第一步，在每个原节点后面创建一个新节点
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        cur = head
        # 第二步设置random
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 第三步，分离两个链表
        dummy = Node(-1)
        cur = head
        pre_node = dummy
        while cur:
            pre_node.next = cur.next
            pre_node = pre_node.next
            cur.next = pre_node.next
            cur = cur.next

        return dummy.next


if __name__ == '__main__':
    head = Node(7)
    h1 = Node(13)
    h2 = Node(11)
    h3 = Node(10)
    h4 = Node(1)

    head.next = h1
    head.random = None
    h1.next = h2
    h1.random = 0

    h2.next = h3
    h2.random = 4

    h3.next = h4
    h3.random = 2

    h4.random = 0

    print(Solution().copyRandomList(head))
