'''

os.system()方法是简单粗暴的执行cmd指令，没有办法获取到cmd输出的内容。
'''
#导入库
import os
import subprocess
from tkinter import *
from time import strftime
from tkinter.filedialog import *
#初始化窗口root
root = Tk()
#设置窗口root的标题
root.title('adb调试工具')
root.minsize(460,300)
#声明reply为文本变量
reply=StringVar()
reply.set(strftime("%Y年%m月%d日%H时%M分%S秒")+':此处显示执行结果')
Label(root,textvariable=reply,fg='red',font=('楷体',12,'bold')).place(x=0,y=0,width=460,height=60)
def excuteInstall():
    if os.popen("adb install "+askopenfilename()).read():
        reply.set(strftime("%Y年%m月%d日%H时%M分%S秒")+":安装命令已经执行完成！")
    else:
        reply.set(strftime("%Y年%m月%d日%H时%M分%S秒")+":安装命令执行失败！")
def excutePower():
    os.popen("adb shell input keyevent 26")
    reply.set(strftime("%Y年%m月%d日%H时%M分%S秒")+":电源键已经按下！")
def excuteReboot():
    os.popen("adb reboot")
    reply.set(strftime("%Y年%m月%d日%H时%M分%S秒")+":手机重启中！")
def showDevices():
    reply.set(os.popen("adb devices").read()+strftime("%Y年%m月%d日%H时%M分%S秒"))
def debug():
    os.popen("adb shell am set-debug-app -w "+inputValue.get())
    reply.set(strftime("%Y年%m月%d日%H时%M分%S秒")+":开始特殊调试！")
def normalDebug():
    os.popen("adb shell am start -D -n "+inputValue0.get())
    reply.set(strftime("%Y年%m月%d日%H时%M分%S秒")+":开始普通调试！")
h=60
Button(root,text="选择一个apk文件用adb命令安装到手机",command=excuteInstall).place(x=0,y=h,width=230,height=30)
Button(root,text="电源键",command=excutePower).place(x=230,y=h,width=50,height=30)
Button(root,text="手机重启",command=excuteReboot).place(x=280,y=h,width=70,height=30)
Button(root,text="显示连接的设备",command=showDevices).place(x=350,y=h,width=110,height=30)
Button(root,text="右边输入需要调试的包名后点我调试apk的oncreate()",command=debug).place(x=0,y=h+30,width=300,height=30)
inputValue=StringVar()
Entry(root,textvariable=inputValue).place(x=300,y=h+30,width=160,height=30)

Button(root,text="右边输入需要普通调试的'包名/activity'后点我开始调试",command=normalDebug).place(x=0,y=h+30+30,width=300,height=30)
inputValue0=StringVar()
Entry(root,textvariable=inputValue0).place(x=300,y=h+30+30,width=160,height=30)
#每一个gui都要有这个结尾
root.mainloop()
