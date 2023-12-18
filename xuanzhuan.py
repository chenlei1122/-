import os,sys
import time
import tkinter as tk
from tkinter import filedialog
from alive_progress import alive_bar


win = tk.Tk()
win.title("批量旋转视频")
win.withdraw()
path = os.path.normpath(filedialog.askdirectory())#获得选择好的文件夹
filelist = os.listdir(path)   #该文件夹下所有的文件（包括文件夹）


for files in filelist:   #遍历所有文件
    
    with alive_bar(len(filelist)) as bar: 
        try:
            Olddir = os.path.join(path, files)    #原来的文件路径
            f2="sp_" + files
            Newdir = os.path.join(path, f2)
            #print(os.path.splitext(Olddir)[1])
            if os.path.isdir(Olddir):       #如果是文件夹则跳过
                print("跳过文件夹"+Olddir)
                continue
            elif os.path.splitext(Olddir)[1] != ".mp4" and os.path.splitext(Olddir)[1] != ".MP4":

                print(Olddir+"不需要转换")
                continue

            else:
                #使用硬件加速-hwaccel cuda(使用ffmpeg -hwaccels命令查看支持的硬件加速选项) 
                #多线程-threads 5 -preset ultrafast  
                # transpose 1：旋转90度 2：旋转180度 3：旋转270度
                cmd1='ffmpeg -i {} -vf "transpose=3"  -threads 5 -preset ultrafast {}'.format(Olddir,Newdir)
                #print(cmd1)
                os.system(cmd1)
                print(files + "转换完成")                
        except Exception as e:    
                 print (str(e))
        bar()

input("please input any key to exit!")