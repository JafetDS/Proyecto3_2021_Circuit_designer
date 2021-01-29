import tkinter as tk
import Elements
from tkinter import filedialog


class StartPage (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(width=1280, height=720)

        load_btn = tk.Button(self, text="Load a netlist", command=lambda: self.go_to_cicuit())
        load_btn.pack()

        build_btn = tk.Button(self, text="Build your circuit", command= lambda: controller.show_frame("CircuitShow"))
        build_btn.pack()
    def go_to_cicuit(self):
        self.controller.set_netlist()
        self.controller.show_frame("CircuitShow")
        CircuitShow.parsedfile = self.controller.getnetlist.readlines()

class CircuitShow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parsed_file = None
        self.resistors = []
        self.power_sources = []
        self.nodes = []
    def populate(self):
        for i in self.parsed_file:
            line = i.split(" ")
            name = line[0]
            conn_a = line[1]
            conn_b = line[2]
            value = line[3][:-1]
            if line[0][0] == "R" or line[0][0] == "r":
                self.resistors.append(Elements.Resistor(self, name, value, conn_a, conn_b))
            if line[0][0] == "V" or line[0][0] == "v" or line[0][0] == "f" or line[0][0] == "F":
                self.power_sources.append (Elements.Resistor (self, name, value, conn_a, conn_b))
            if conn_a not in self.nodes:
                self.nodes.append(conn_a)
            if conn_b not in self.nodes:
                self.nodes.append(conn_b)





class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # netlist file
        self.title("CIRCUIT DESIGNER")
        self.geometry("1280x720")
        self.netlist_file = ""
        container = tk.Frame(self)
        container.config(width=1280, height=720)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=0)

        self.frames = {}
        for F in (StartPage, CircuitShow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def set_netlist(self):
        self.netlist_file = filedialog.askopenfile(mode="r", filetypes=[("Netlist files","*.cir")])
    def getnetlist(self):
        return self.netlist_file


app = Application()
app.mainloop()
