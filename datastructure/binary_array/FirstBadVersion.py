#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 9:57
# @File    : FirstBadVersion.py


class FirstBadVersion(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left < right:
            # 左边界查找
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
