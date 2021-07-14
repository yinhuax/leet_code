#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 21:16
# @File    : NumSimilarGroups.py
"""

如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。

总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？

 

示例 1：

输入：strs = ["tars","rats","arts","star"]
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/similar-string-groups
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class NumSimilarGroups(object):

    def __init__(self):
        pass

    def numSimilarGroups(self, strs: List[str]) -> int:
        visit = set()
        # 深搜所有相似字符串，加入记忆化集合
        count = 0
        n = len(strs)

        for i in range(n):
            if strs[i] not in visit:
                count += 1
                queue = []
                queue.append(strs[i])
                visit.add(strs[i])

                while queue:
                    s = queue.pop()
                    for j in range(n):
                        if strs[j] in visit:
                            continue
                        if self.similar_str(s, strs[j]):
                            queue.append(strs[j])
                            visit.add(strs[j])

        return count

    def similar_str(self, s1, s2):
        """
        判断是否相似，超过2个相同位置字符不等，即为不相似
        :param s1:
        :param s2:
        :return:
        """
        if len(s1) != len(s2):
            return False

        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1

            if count > 2:
                return False
        return True
