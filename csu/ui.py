#coding=utf-8
import wx
import wx.grid
import csu

class UI(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title="成绩查询",size=(1050,560))


        grid = wx.grid.Grid(self,pos=(10,0),size=(1050,500))
        grid.CreateGrid(100,9)
        for i in range(100):
            for j in range(9):
                grid.SetCellAlignment(i,j,wx.ALIGN_CENTER,wx.ALIGN_CENTER)
        grid.SetColLabelValue(0, "序号") #第一列标签
        grid.SetColLabelValue(1, "初修学期")
        grid.SetColLabelValue(2, "获得学期")
        grid.SetColLabelValue(3, "课程")
        grid.SetColLabelValue(4, "成绩")  # 第一列标签
        grid.SetColLabelValue(5, "学分")
        grid.SetColLabelValue(6, "课程属性")
        grid.SetColLabelValue(7, "课程性质")
        grid.SetColLabelValue(8, "获得方式")  # 第一列标签

        grid.SetColSize(0,50)
        grid.SetColSize(1,100)
        grid.SetColSize(2,100)
        grid.SetColSize(3,350)
        grid.SetColSize(4,50)
        grid.SetColSize(5,50)
        grid.SetColSize(6,50)
        grid.SetColSize(7,100)
        grid.SetColSize(8,100)


        grid.SetCellTextColour("NAVY")
        data = csu.search()
        data.remove(data[0])
        print(data)
        for i,item1 in enumerate(data):
            for j,item2 in enumerate(item1):
                grid.SetCellValue(i,j,data[i][j])

        pass


app = wx.App()
frame = UI()
frame.Show()
app.MainLoop()
