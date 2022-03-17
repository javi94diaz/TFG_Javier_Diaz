import sys
import tkinter as tk
from tkinter import ttk



class ButtonNotebook(ttk.Notebook):
    _initialized = False

    def __init__(self, *args, **kwargs):
        if not self._initialized:
            self._initialize()
            self._inititialized = True

        kwargs["style"] = "ButtonNotebook"
        super().__init__(*args, **kwargs)
        self._active = None

        self.bind("<ButtonPress-1>", self.on_tab_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_tab_close_release)

    def on_tab_close_press(self, event):
        name = self.identify(event.x, event.y)
        if name == "tab_btn_close":
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_tab_close_release(self, event):
        if not self.instate(['pressed']):
            return None

        name =  self.identify(event.x, event.y)

        if name == "tab_btn_close":
            index = self.index("@%d,%d" % (event.x, event.y))
            if self._active == index:
                self.forget(index)
                self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def _initialize(self):
        style = ttk.Style()
        if sys.platform == "win32":
            style.theme_use('winnative')

        self.images = (
            tk.PhotoImage("img_close", data='''
                          R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2f///////////////yH5
                          BAEKAAIALAAAAAAIAAgAAAMUCCAsCmO5OBVl8OKhoV3e9jQOkAAAOw==
                           '''),
            tk.PhotoImage("img_closeactive", data='''
                          R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2f///////////////yH5
                          BAEKAAMALAAAAAAIAAgAAAMPCDA8+gw+GGlVbWKqmwMJADs=
                          ''' ),
            tk.PhotoImage("img_closepressed", data='''
                          R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2f///////////////yH5B
                          AEKAAMALAAAAAAIAAgAAAMPGDE8+gw+GGlVbWKqmwsJADs=
                          ''')
        )

        style.element_create("tab_btn_close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')

        style.layout("ButtonNotebook", [("ButtonNotebook.client", {"sticky": "nswe"})])
        style.layout("ButtonNotebook.Tab", [
            ("ButtonNotebook.tab", {
                "sticky": "nswe", 
                "children": [
                    ("ButtonNotebook.padding", {
                        "side": "top", 
                        "sticky": "nswe",
                        "children": [
                            ("ButtonNotebook.focus", {
                                "side": "top", 
                                "sticky": "nswe",
                                "children": [
                                    ("ButtonNotebook.label", {"side": "left", "sticky": ''}),
                                    ("ButtonNotebook.tab_btn_close", {"side": "left", "sticky": ''}),
                                ]
                            })
                        ]
                    })
                ]
            })
        ])

        style.configure("ButtonNotebook.Tab", background="#fdd57e")         
        style.map('ButtonNotebook.Tab', background = [("selected", "#C70039"),
                                                      ("active", "#fc9292")],
                                        foreground = [("selected", "#ffffff"),
                                                      ("active", "#000000")]
                 ) 

# if __name__ == "__main__":
#     root = tk.Tk()
#     nb = ButtonNotebook(width=200, height=200)
#     nb.pressed_index = None
#     f1 = tk.Frame(nb)
#     f2 = tk.Frame(nb)
#     f3 = tk.Frame(nb)
#     nb.add(f1, text='Pestaña 1')
#     nb.add(f2, text='Pestaña 2')
#     nb.add(f3, text='Pestaña 3')
#     nb.pack(expand=1, fill='both')
#     root.mainloop()