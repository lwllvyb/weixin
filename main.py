#-*-coding:utf-8 -*-
import werobot
import process_txt
from config import ExceptSignalHandle

robot = werobot.WeRoBot(token='weixinliwenlong')

# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def echo(message):
    return process_txt.txt_process(message.content)

# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    return message.img

#监听signal
ExceptSignalHandle.handle_signal()

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 12233
robot.run()