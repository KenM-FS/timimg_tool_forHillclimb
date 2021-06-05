from datetime import date, datetime
from datetime import timedelta
import serial
import wx

class MainFrame(wx.Frame):

    def __init__(self, parent, ID, title):

        wx.Frame.__init__(self, parent, title=title)
        self.last_time = datetime.now() - timedelta(seconds=30)

        self.__create_widget()
        self.__do_layout()
        self.SetSize((300,200))
        self.Centre()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(1)

    def __create_widget(self):
        self.clock = wx.StaticText(self, label = "")

        self.text = wx.StaticText(self, label = "計測時間")
        self.check = wx.StaticText(self, label = "計測無し")

        self.button = wx.Button(self, label = "手動計測")
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

        self.combobox = wx.ComboBox(self, choices = ["COM1_tmp", "COM2_tmp"], style=wx.CB_READONLY)

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.clock, flag=wx.ALIGN_LEFT)
        sizer.Add(self.text, flag=wx.ALIGN_LEFT)
        sizer.Add(self.check, flag=wx.ALIGN_LEFT)
        sizer.Add(self.button, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        sizer.Add(self.combobox, flag=wx.ALIGN_CENTER | wx.TOP, border=5)
        self.SetSizer(sizer)

    def OnButton(self, button_label):
        current = datetime.now()

        ts = (current.strftime('%H:%M:%S.%f')[:-3])
        if current - self.last_time > timedelta(seconds=5):
            self.check.SetLabel(ts)
            self.last_time = current

    def OnTimer(self, event):
        current = datetime.now()

        ts = (current.strftime('%H:%M:%S.%f')[:-3])
        self.clock.SetLabel(ts)
        line = arduino.read()
        val = int.from_bytes(line, 'big')
        if val == 1:
            self.OnButton(self.button)
        arduino.reset_input_buffer()

class TimingApp(wx.App):

    def OnInit(self):
        # フレームオブジェクトの生成
        frame = MainFrame(None, -1, "時間計測")
        
        # メインフレームに設定
        self.SetTopWindow(frame)

        # フレーム表示
        frame.Show(True)
        return True

def main():
    app = TimingApp()
    app.MainLoop()

if __name__ == '__main__':
    try:
        arduino = serial.Serial('COM3', 9600, timeout=0)
    except:
        print("Failed to connect")
        exit()

    main()