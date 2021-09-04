#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/4 15:09
# @File    : IsValid.py
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def isValid(self, s: str) -> bool:
        """
        有效括号，思路，使用栈
        :param s:
        :return:
        """
        visited = {")": "(", "}": "{", "]": "["}

        stack = []
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if stack and stack[-1] == visited[s[i]]:
                    stack.pop()
                else:
                    return False
        return not stack
