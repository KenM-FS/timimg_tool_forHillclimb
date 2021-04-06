import wx
import serial
from serial.tools import list_ports
import datetime

def main():
    ports = list_ports.comports()
    print(ports)
    for info in ports:
        print(info.device)

if __name__ == "__main__":
    app = wx.App(True,None)
    frame = wx.Frame(None, -1, 'Hello World', size=(500,500))
    frame.Show()
    app.MainLoop()
