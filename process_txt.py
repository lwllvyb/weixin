#-*-coding:utf-8 -*-

'''
负责处理文本消息
'''

from config import *

def txt_process(content):
    return help()



def help():
    ret = ''
    for id, project in Projects.PROJECTS.items():
        ret += "{0}\t{1}\r\n".format(id, project)
    return "{0}".format(ret)