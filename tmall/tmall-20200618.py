#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: 侠骨留香(xiaguliuxiang)
# date: 2020-06-01
# 适配机型: Honor 10,屏幕分辨率:2280x1080
# github: https://github.com/xiaguliuxiang/xiaguliuxiang-python-games

import os
import random
import time

'''
天猫618理想生活列车,辅助完成任务领喵币

使用说明:
1.安装并配置 python 3 环境;
2.手机连接电脑,打开开发人员选项,并开启 USB 调试;
3.打开手机天猫(淘宝),进入618理想生活列车界面并点击领喵币打开领喵币中心;
4.根据不同任务所需次数,修改代码中 task_executor 的第一个参数,运行此程序.

本项目仅供学习研究使用,请勿用于商业用途!
'''


# 设置临时环境变量,免去配置adb的麻烦
def set_env():
    parent_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    tools = os.path.join(parent_path, 'tools')
    os.environ['PATH'] = tools + ';' + os.getenv('PATH')


# 随机整数[x,y)
def rnd(x, y):
    return int(random.uniform(x, y))


# 当前时间
def cur_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 模拟滑动
def swipe():
    x1 = rnd(600, 800)  # 横坐标1
    y1 = rnd(1500, 1600)  # 纵坐标1
    x2 = rnd(500, 600)  # 横坐标2
    y2 = rnd(600, 800)  # 纵坐标2
    os.system('adb shell input swipe {} {} {} {}'.format(x1, y1, x2, y2))  # 模拟从下往上滑动
    os.system('adb shell input swipe {} {} {} {}'.format(x2, y2, x1, y1))  # 模拟从上往下滑动


# 模拟点击
def simulation_click(x1, x2, y1, y2):
    os.system('adb shell input tap {} {}'.format(rnd(x1, x2), rnd(y1, y2)))
    time.sleep(1)


# 返回
def back():
    os.system('adb shell input keyevent KEYCODE_BACK')


# 执行任务
def task_executor(times, x1, x2, y1, y2):
    print('====== 做任务领喵币,任务开始执行啦(坐标:x:{}-{};y:{}-{}) ======'.format(x1, x2, y1, y2))
    for i in range(times):
        print('\r{} 浏览任务({}/{})开始执行,请稍等...'.format(cur_time(), i + 1, times), end="")
        # 点击去浏览
        os.system('adb shell input tap {} {}'.format(rnd(x1, x2), rnd(y1, y2)))
        for j in range(3):  # 滑动前等待3秒,避免网络不好,我的网络怎么这么垃圾!!!
            print("\r{} 浏览任务({}/{})执行中,请稍等...".format(cur_time(), i + 1, times), end="")
            time.sleep(1)
        swipe()
        browse_time = 20  # 浏览页面20秒,避免因计时延迟导致浏览时间不足
        for j in range(browse_time):
            print("\r{} 浏览任务({}/{})执行中,请等待 {} 秒".format(cur_time(), i + 1, times, browse_time - j), end="")
            time.sleep(1)
        print('\r{} 浏览任务({}/{})执行完成,喵喵喵赢红包'.format(cur_time(), i + 1, times))
        back()
        time.sleep(1)
    time.sleep(1)
    print('====== 做任务领喵币,任务执行完成啦(坐标:x:{}-{};y:{}-{}) ======'.format(x1, x2, y1, y2))


if __name__ == '__main__':
    print('***** 仅供学习研究使用,请勿用于商业用途 *****')
    set_env()
    # simulation_click(900, 990, 2020, 2130)  # 点击领喵币按钮(坐标:x:900-990;y:2020-2130),弹出领喵币中心
    simulation_click(820, 950, 925, 990)  # 签到任务,坐标:x:820-950;y:925-990
    # 任务1(邀请好友),不执行,坐标:x:825-960;y:1110-1175
    task_executor(1, 825, 960, 1300, 1365)  # 任务2,执行1次,坐标:x:825-960;y:1300-1365
    task_executor(1, 825, 960, 1485, 1550)  # 任务3,执行1次,坐标:x:825-960;y:1485-1550
    task_executor(1, 825, 960, 1675, 1740)  # 任务4,执行1次,坐标:x:825-960;y:1675-1740
    task_executor(1, 825, 960, 1860, 1930)  # 任务5,执行1次,坐标:x:825-960;y:1860-1930
    task_executor(1, 825, 960, 2045, 2075)  # 任务6,执行1次,坐标:x:825-960;y:2045-2075
    print('***** 仅供学习研究使用,请勿用于商业用途 *****')
    os.system("pause")
