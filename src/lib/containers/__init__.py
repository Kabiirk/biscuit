import tkinter as tk

# from .left import LeftPane
from .right import RightPane
from ..components.dirtree import DirTreePane
from ..components.sidebar import Sidebar

class BasePane(tk.PanedWindow):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base
        
        self.configure(orient=tk.HORIZONTAL)

        self.right = RightPane(self)
        self.dirtree = DirTreePane(self, before=self.right)
        self.left_panes = [self.dirtree]

        self.sidebar = Sidebar(self)

        self.add(self.sidebar)
        self.add(self.right)
