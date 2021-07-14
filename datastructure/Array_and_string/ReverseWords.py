#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/24 19:45
# @File    : ReverseWords.py


class ReverseWords(object):

    def __init__(self):
        pass

    def reverseWords(self, s: str) -> str:
        return ''.join([i for i in s.split(" ") if i][::-1])
