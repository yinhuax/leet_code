#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/27 18:36
# @File    : DecodeString.py


class Solution:

    def decodeString(self, s: str) -> str:
        nums = set([str(_) for _ in range(10)])
        stack = []

        num = 0
        cur_str = ''
        for i in s:
            if i in nums:
                num = num * 10 + int(i)
            elif i == '[':
                stack.append((cur_str, num))
                cur_str, num = "", 0
            elif i == ']':
                top = stack.pop()
                cur_str = top[0] + cur_str * top[1]
            else:
                cur_str += i

        return cur_str


if __name__ == '__main__':
    print(Solution().decodeString("3[a2[c]]"))
