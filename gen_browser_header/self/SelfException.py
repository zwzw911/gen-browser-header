#! /usr/bin/env python3

# -*- coding:utf-8 -*-


class ResponseException(Exception):
    CodeMatchMsg = {
        404: '404，页面不存在',
        503: '503, 服务不可用',
    }

    def __init__(self, code):
        self.code = code
        if code in ResponseException.CodeMatchMsg:
            self.msg = ResponseException.CodeMatchMsg[self.code]
        else:
            self.msg = '错误代码%d没有匹配的错误信息' % self.code
        super().__init__(ResponseException.CodeMatchMsg[self.code])

    def __str__(self):
        return '错误代码: %d，%s' % (self.code, self.msg)
