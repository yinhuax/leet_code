#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/3 18:32
# @File    : Multiply.py
"""

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        """
        字符串相乘
        :param num1:
        :param num2:
        :return:
        """
        if num1 == '0' or num2 == '0':
            return '0'

        # 反向遍历字符串
        m, n = len(num1), len(num2)
        res = [0] * (n + m)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                res[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            res[i - 1] += res[i] // 10
            res[i] %= 10

        index = 1 if res[0] == 0 else 0
        ans = "".join(str(x) for x in res[index:])
        return ans


if __name__ == '__main__':
    print(Solution().multiply(num1="123", num2="456"))
