#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/29 11:25
# @File    : PathInZigZagTree.py
from typing import List

"""
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):

    def pathInZigZagTree(self, label: int) -> List[int]:
        """
        思路，找规律
        :param label:
        :return:
        """
        if label == 1:
            return [1]
        import math
        # 计算深度
        depth = int(math.log2(label // 2)) + 1

        ans = []
        x = label
        ans.append(x)
        while depth > 0:
            min_node = 2 ** depth
            max_node = 2 ** (depth + 1) - 1
            x = (max_node + min_node - x) // 2
            depth -= 1
            ans.append(x)

        return ans[::-1]


if __name__ == '__main__':
    print(Solution().pathInZigZagTree(1))
