#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/19 17:16
# @File    : EvalRPN.py
from typing import List


# 根据 逆波兰表示法，求表达式的值。
#
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
#  
#
# 说明：
#
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/queue-stack/gomvm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class EvalRPN(object):

    def __init__(self):
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        operation = set(list(['/', '*', '+', '-']))
        stack = []
        for token in tokens:
            if token in operation:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(eval(str(num2) + token + str(num1))))
            else:
                stack.append(token)

        return int(stack[-1])


if __name__ == '__main__':
    print(EvalRPN().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
