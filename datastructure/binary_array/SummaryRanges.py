#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/14 13:25
# @File    : SummaryRanges.py
from typing import List

"""
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b
 
示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


单调栈
"""


class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        使用单调栈
        :param nums:
        :return:
        """
        stack = []
        result = []
        for num in nums:
            if stack and num > (stack[-1] + 1):
                if len(stack) == 1:
                    result.append(str(stack[-1]))
                else:
                    result.append(str(stack[0]) + "->" + str(stack[-1]))
                stack.clear()
            stack.append(num)

        if stack:
            if len(stack) == 1:
                result.append(str(stack[-1]))
            else:
                result.append(str(stack[0]) + "->" + str(stack[-1]))
        return result


if __name__ == '__main__':
    print(Solution().summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
