#-*-coding:utf-8 -*-

'''
负责处理文本消息
'''

from config import *

def txt_process(content):
    return "{0}".format(help())


def help():
    ret = ''
    for id, project in Projects.PROJECTS.items():
        ret += "{0}\tab{1}\r\n".format(id, project)
    return ret