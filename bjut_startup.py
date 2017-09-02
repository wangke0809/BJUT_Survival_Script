# coding=utf-8

from bjutNet import *
from time import sleep
from win32api import SetCursorPos,mouse_event,ShellExecute
import win32con
import os
import re

# 启动延时(s)
sleep_time = 0

# 上网帐号和密码
userid = '<userid>'
userpass = '<passwd>'
# 认证类型 ipv4 ipv6 ipv46
usertype = 'ipv46'

# 是否自动运行微信
wx_autorun = True
# 微信的路径
wx_path    = 'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe'
# 是否自动点击确定登录按钮 需要win32api库 安装:pip install pypiwin32
wx_click   = True
# 登录按钮的位置
wx_click_point = (685,445)

# 需要自动运行的程序列表 建议用双斜杠(特别是紧跟着数字)
# ['路径','附加命令']
auto_run_paths = [
                    #['C:\\Program Files\\360\\360AP\\360AP.exe','/desktopfree'],
                    ['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe','fm.baidu.com ']
]

def run_exe(path):
    #os.system("start \"\" " + '"' + path + '"')
    ShellExecute(0, 'open', path[0], path[1], '', 1)

sleep(sleep_time)

net = bjutNet(userid,userpass)

res = False

if usertype=='ipv4' : 
    res |= net.login_ipv4()
elif usertype=='ipv6' : 
    res |= net.login_ipv6()
else:
    res |= net.login_ipv46()

if res : 
    print("已用时长 %s 小时 , 已用流量 %s MB , 余额 %s 元"%net.get_account_info())
    if wx_autorun : 
        print('开启微信...')
        run_exe((wx_path,''))
        if wx_click : 
            x,y = wx_click_point
            # 测试发现系统刚启动是调用SetCursorPos函数出错，估计是没有加载完成
            while True : 
                try:
                    SetCursorPos((x,y))
                    break
                except Exception as e:
                    pass
            sleep(1)
            mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
            mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        sleep(2)
        print('自动运行程序...')
        for p in auto_run_paths : 
            print('运行 ' + p[0] + ' ' + p[1])
            run_exe(p)
            sleep(0.5)
print('执行完成，准备结束...')
sleep(3)