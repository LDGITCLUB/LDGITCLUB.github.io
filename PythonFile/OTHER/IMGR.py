from __future__ import print_function
import winreg
import ctypes, sys
from tkinter import messagebox
import time
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    messagebox.showinfo(title='提示',message='请先退出所有安全软件')
    FilePath = input("请输入您想映像劫持的软件(软件名+.exe):")
    ToPath = input("请输入您想劫持为哪个软件(路径,输入0以禁用该软件):")
    if FilePath == ToPath:
        messagebox.showinfo(title='Info',message='Repeat!')
        sys.exit(0)
    else:
        if ToPath == '0':
            ToPath = 'C:\\a\\b\\c\\d\\e\\f\\g\\iawaliwuehfauwlf\\ffjiuahfaoiaraeufhiewucaiwjaafdnasiufanhwdudnwiaundw.exe'

        try:
            winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Image File ExecutionOptions'+'\\'+FilePath,reserved=0,access=winreg.KEY_ALL_ACCESS)
            Handle = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Image File ExecutionOptions'+'\\'+FilePath,reserved=0,access=winreg.KEY_ALL_ACCESS)

            R = winreg.CreateKeyEx(Handle,reserved=0,access=winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(R,'Debugger',0,winreg.REG_SZ,ToPath)
            winreg.CloseKey(Handle)
            messagebox.showinfo(title='提醒',message='劫持完成')

        except Exception as E:
            messagebox.showerror(titie='错误',message='未知错误')
            sys.exit(1)

else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)