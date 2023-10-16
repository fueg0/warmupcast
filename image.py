import wx
from Lifter import *
from PlateCounter import *

SCALE = {"red": 1,
         "blue": 1,
         "yellow": 0.8,
         "green": 0.6,
         "white": 0.4,
         "black": 0.2,
         "silver": 0.1}

COLOR = {"red": 0,
         "blue": 0,
         "yellow": 0,
         "green": 0,
         "white": 0,
         "black": 0,
         "silver": 0}


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        self.HEIGHT = 1080
        self.WIDTH = 1920
        super(Mywin, self).__init__(parent, title=title, size=(self.WIDTH, self.HEIGHT))
        self.current_lifter = "Nick"
        self.next_lifter = "Mario"
        self.weight_value = 220
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_COMMAND_LEFT_CLICK, self.OnButtonClick)
        self.Centre()
        self.Show(True)


    def OnPaint(self, e, ): #current, next):
        dc = wx.PaintDC(self)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()

        font = wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        dc.SetFont(font)

        ### CURRENT
        # liftername bar
        dc.DrawText(f"Current Lifter ------ {self.current_lifter} ------ {self.weight_value}kg", 0, 10)
        pen = wx.Pen(wx.Colour(0, 0, 255))
        dc.SetPen(pen)
        # x, y, end x, end y
        dc.DrawLine(1600, 50, 0, 50)
        pen = wx.Pen(wx.Colour(wx.BLACK))
        dc.SetPen(pen)

        # current barbell
        pen = wx.Pen(wx.Colour(wx.BLACK))
        dc.SetPen(pen)
        color = wx.Colour(wx.LIGHT_GREY)
        b = wx.Brush(color)
        dc.SetBrush(b)
        dc.DrawRectangle(0, 400, 201, 100)

        # current plates
        color = wx.Colour(wx.RED)
        b = wx.Brush(color)
        dc.SetBrush(b)

        # x, y, width, height
        # x = i*100 + i*offset (5) + bar_width
        dc.DrawRectangle(200, 50, 100, 725)
        dc.DrawRectangle(305, 50, 100, 725)
        dc.DrawRectangle(410, 50, 100, 725)
        dc.DrawRectangle(515, 50, 100, 725)


        ### NEXT
        # lifter name bar
        dc.DrawText(f"Next Lifter: \t {self.next_lifter}", 0, 800)
        pen = wx.Pen(wx.Colour(0, 0, 255))
        dc.SetPen(pen)
        # x, y, end x, end y
        dc.DrawLine(0, 775, 1600, 775)
        pen = wx.Pen(wx.Colour(wx.BLACK))
        dc.SetPen(pen)

        # next barbell
        pen = wx.Pen(wx.Colour(wx.BLACK))
        dc.SetPen(pen)
        color = wx.Colour(wx.LIGHT_GREY)
        b = wx.Brush(color)
        dc.SetBrush(b)
        # x, y, width, height
        # half max_x, bottom_space, plate_width, height - bottom_space
        dc.DrawRectangle(800, 800, 100, 40)

        # next plates
        color = wx.Colour(wx.RED)
        b = wx.Brush(color)
        dc.SetBrush(b)

        # x, y, width, height
        # x = i*100 + i*offset (5) + bar_width
        # y = 775
        # width = 100
        # height = 87
        dc.DrawRectangle(900, 775, 50, 87)
        dc.DrawRectangle(955, 775, 50, 87)
        dc.DrawRectangle(1010, 775, 50, 87)
        dc.DrawRectangle(1065, 775, 50, 87)

    def OnButtonClick(self, event):
        if True:
            pass
        else:
            event.Skip()



    def OnEvent(self, event):
        pass

    def PaintLoading(self, loading):
        dc = wx.PaintDC(self)
        brush = wx.Brush("black")
        dc.SetBackground(brush)
        dc.Clear()

        font = wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        dc.SetFont(font)
        upper_name = 0, self.HEIGHT * 0.25
        lower_name = self.HEIGHT - upper_name, self.HEIGHT
        center = upper_name[1], lower_name[0]

        # draw upper
        # liftername bar
        dc.DrawText(f"Current Lifter:  {self.current_lifter}", 0, upper_name[1])
        dc.DrawText(f"Weight:  {self.weight_value}kg / {round(self.weight_value * 2.2046, 1)}lbs", self.WIDTH / 2, upper_name[1])
        pen = wx.Pen(wx.Colour(0, 0, 255))
        dc.SetPen(pen)
        # x, y, end x, end y
        dc.DrawLine(1600, 50, 0, 50)
        pen = wx.Pen(wx.Colour(wx.BLACK))
        dc.SetPen(pen)


ex = wx.App()
Mywin(None, 'WarmupCast')
ex.MainLoop()
