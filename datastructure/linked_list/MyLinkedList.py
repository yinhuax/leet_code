#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/5 21:28
# @File    : MyLinkedList.py

"""
链表自实现
"""


class Node(object):
    def __init__(self, val=None, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.link_len = -1
        self.link_head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.link_len or index < 0:
            return -1

        i = 0
        node = self.link_head
        while i < index:
            node = node.next
            i += 1

        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        head = Node(val=val)
        if self.link_head:
            head.next = self.link_head
            self.link_head.pre = head
        self.link_head = head
        self.link_len += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # 如果头部没有元素添加到头部
        if not self.link_head:
            self.addAtHead(val)
            return

        # 否则，遍历到末尾添加
        i = 0
        node = self.link_head
        while i < self.link_len and node.next:
            node = node.next
            i += 1

        last_node = Node(val)
        last_node.pre = node
        node.next = last_node
        self.link_len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # 有添加到末尾的操作
        if index > self.link_len + 1:
            return

        if index <= 0:
            self.addAtHead(val)
            return

        if index == self.link_len + 1:
            self.addAtTail(val)
            return

        # 正常情况下，添加元素到指定位置， 可能是末尾的情况
        i = 0
        node = self.link_head
        pre_node = self.link_head
        while i < index:
            pre_node = node
            node = node.next
            i += 1

        add_node = Node(val=val)
        add_node.pre = pre_node
        pre_node.next = add_node
        node.pre = add_node
        add_node.next = node

        self.link_len += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.link_len or index < 0:
            return

        # 特殊情况，index=0 or index=self.link_head
        i = 0
        node = self.link_head
        pre_node = self.link_head
        while i < index:
            pre_node = node
            node = node.next
            i += 1

        if index == 0:
            # 删除表头
            self.link_head = pre_node.next
        elif index == self.link_head:
            # 删除表末尾
            pre_node.next = None
        else:
            # 正常删除元素
            pre_node.next = node.next

        self.link_len -= 1


if __name__ == '__main__':
    my_link = MyLinkedList()
    my_link.addAtHead(7)
    my_link.addAtHead(2)
    my_link.addAtHead(1)
    my_link.addAtIndex(3, 0)
    print(my_link.deleteAtIndex(2))
    my_link.addAtHead(6)
    my_link.addAtTail(4)
    print(my_link.get(4))
    my_link.addAtHead(4)
    my_link.addAtIndex(5, 0)
    my_link.addAtHead(6)
    # print(my_link.deleteAtIndex(1))
    # print(my_link.get(1))
    print()
