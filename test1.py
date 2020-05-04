from comtypes.client import CreateObject
import os

from winxpgui import FindWindow

try:
    lw = CreateObject('lw.lwsoft3')
except OSError:
    path =os.getcwd()
#print(path)
    os.system(r'regsvr32  %s\lw.dll'% path)
    lw=CreateObject('lw.lwsoft3')
print(lw.ver())
