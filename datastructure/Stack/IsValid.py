#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/19 0:01
# @File    : IsValid.py

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/queue-stack/g9d0h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class IsValid(object):

    def __init__(self):
        pass

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        # 思路遇到{、(、[ 入栈，遇到 }、)、]出栈
        result_dict = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for i in s:
            if i in result_dict:
                stack.append(i)
            else:
                if not stack or result_dict[stack[-1]] != i:
                    return False
                stack.pop()

        return not stack


if __name__ == '__main__':
    print(IsValid().isValid("()"))
