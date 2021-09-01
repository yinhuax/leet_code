#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/1 6:46
# @File    : CompareVersion.py
"""
给你两个版本号 version1 和 version2 ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。

返回规则如下：

如果 version1 > version2 返回 1，
如果 version1 < version2 返回 -1，
除此之外返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-version-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        split 后双指针，空间复杂度(m + n)，时间复杂度O(max(n, m))
        :param version1:
        :param version2:
        :return:
        """
        version1 = version1.split(".")
        version2 = version2.split(".")

        n1 = len(version1)
        n2 = len(version2)
        i, j = 0, 0
        while i < n1 or j < n2:
            value1 = int(version1[i]) if i < n1 else 0
            value2 = int(version2[j]) if j < n2 else 0

            if value1 > value2:
                return 1
            elif value1 < value2:
                return -1

            i += 1
            j += 1

        return 0

    def compareVersion1(self, version1: str, version2: str) -> int:
        """
        不使用split， 额外空间O(1)
        :param version1:
        :param version2:
        :return:
        """
        n1 = len(version1)
        n2 = len(version2)

        i, j = 0, 0
        while i < n1 or j < n2:
            x = 0
            while i < n1 and version1[i] != ".":
                x = x * 10 + int(version1[i])
                i += 1

            y = 0
            while j < n2 and version2[j] != ".":
                y = y * 10 + int(version2[j])
                j += 1

            if x != y:
                return 1 if x > y else -1
            i += 1
            j += 1

        return 0


if __name__ == '__main__':
    print(Solution().compareVersion1(version1="0.1", version2="1.1"))
