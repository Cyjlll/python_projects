# _*_ coding: UTF-8 _*_
# @Time : 2021/5/10 20:28
# @Author : caoyujie
# @Site : 
# @File : yingping.py
# @Software : PyCharm
import moviepy.editor as mpy


# 截取背景音乐
audio_background = mpy.AudioFileClip(r'C:\Users\Administrator\Desktop\f3a93ef4e5a0c2aadd2820cf2af7ee78.mp4').subclip(1, 60)
audio_background.write_audiofile(r'C:\Users\Administrator\Desktop\222.mp3')
