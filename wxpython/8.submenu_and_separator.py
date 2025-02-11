import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, "New")
        fileMenu.Append(wx.ID_OPEN, "Open")
        fileMenu.Append(wx.ID_SAVE, "Save")
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, "Import newsfeed list...")
        imp.Append(wx.ID_ANY, "Import bookmarks...")
        imp.Append(wx.ID_ANY, "Import mail...")

        fileMenu.Append(wx.ID_ANY, "Import", imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, "&QuittCtrl+W")
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle("Submenu")
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == "__main__":
    main()
