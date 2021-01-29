import random
import time
import tkinter as tk
import Elements as Ele
from tkinter import filedialog
from tkinter import simpledialog
import threading
import Grafo as g

class StartPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(width=1280, height=720)

        load_btn = tk.Button(self, text="Load a netlist", command=lambda: self.go_to_cicuit())
        load_btn.pack()

        build_btn = tk.Button(self, text="Build your circuit", command= lambda: controller.show_frame("CircuitBuilder"))
        build_btn.pack()

    def go_to_cicuit(self):
        self.controller.set_netlist()
        self.controller.show_frame("CircuitShow")
        self.controller.parsed_file = self.controller.getnetlist().readlines()


class CircuitShow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parsed_file = []
        self.resistors = []
        self.power_sources = []
        self.nodes = []
        self.graph = {}
        self.populated = False
        self.old_parsed = self.controller.parsed_file
        self.pop_thread = threading.Thread(target=self.populate_activator)
        self.pop_thread.start()

    def populate_activator(self):

        while not self.populated:
            if self.old_parsed != self.controller.parsed_file:
                self.populate_aux()
                self.populated = True
            time.sleep(1)


    def populate_aux(self):
        # format of the netlist is:
        # name connector_a connector_b value coordx coordy
        for i in self.controller.parsed_file:
            line = i.split(" ")
            name = line[0]
            conn_a = line[1]
            conn_b = line[2]
            x_coord = int(line[4])

            y_coord = int(line[5])
            print (name, x_coord, y_coord)
            if line[3][-1:] == ";":
                value = line[3][:-1]
            else:
                value = line[3]


            if conn_a not in self.graph.keys():
                self.graph[conn_a] = {}
            if conn_b not in self.graph[conn_a].keys():
                self.graph[conn_a][conn_b] = random.randint(0, 10)

            if conn_b not in self.graph.keys():
                self.graph[conn_b] = {}

            if conn_a not in self.graph[conn_b].keys():
                self.graph[conn_b][conn_a] = random.randint(0, 10)

            if line[0][0] == "R" or line[0][0] == "r":
                resistor = Ele.Resistor(self, name, value, conn_a, conn_b)
                resistor.place(x=x_coord, y = y_coord)
                self.resistors.append(resistor)
            elif line[0][0] == "V" or line[0][0] == "v" or line[0][0] == "f" or line[0][0] == "F":
                power_source = Ele.PowerSource(self, name, value, conn_a, conn_b)
                power_source.place(x=x_coord, y = y_coord)
                self.power_sources.append(power_source)
            self.controller.graph.generate(self.graph)
            print(self.graph)


class CircuitBuilder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(width=1280, height=720)
        self.canvas = tk.Canvas(self)
        self.canvas.config(width=1280, height=720)
        self.canvas.pack()

        self.add_resistor_btn = tk.Button(self.canvas, text= "RESISTOR", command=lambda: self.add_resistor())
        self.add_resistor_btn.place(x=0, y=0)
        self.add_power_btn = tk.Button(self.canvas, text="DC POWER", command=lambda: self.add_dc())
        self.add_power_btn.place(x=0, y=20)
        self.r_list = []


    def add_dc(self):
        pwr_name = tk.simpledialog.askstring (title="Power Source´s name", prompt="Write the Power Source´s name",
                                                   parent=self.canvas)
        pwr_value = tk.simpledialog.askstring (title="Power Source´s value", prompt="Write the power source´s value",
                                                    parent=self.canvas)
        pw = Ele.PowerSource(self.canvas, pwr_name, pwr_value)
        # self.r_list.append(r)
        pw.place(x=300, y=300)

        self.make_draggable(pw)
        pw.bind ("<Button-3>", pw.rotate)

    def add_resistor(self):
        resistor_name = tk.simpledialog.askstring(title="Resistor´s name", prompt="Write the resistor´s name"
                                                  , parent=self.canvas)
        resistor_value = tk.simpledialog.askstring(title="Resistor´s value", prompt="Write the resistor´s value",
                                                   parent=self.canvas)
        r = Ele.Resistor(self.canvas, resistor_name, resistor_value)
        # self.r_list.append(r)
        r.place(x=300, y=300)
        self.make_draggable(r)
        r.bind("<Button-3>",  r.rotate)

    def make_draggable(self, widget):
        widget.bind("<Button-1>", self.on_drag_start)
        widget.bind ("<B1-Motion>", self.on_drag_motion)
    def on_drag_start(self, event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y
    def on_drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() -widget._drag_start_y + event.y
        widget.place(x=x, y=y)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # netlist file
        self.title("CIRCUIT DESIGNER")
        self.geometry("1280x720")
        self.netlist_file = ""
        self.parsed_file = []
        container = tk.Frame(self)
        container.config(width=1280, height=720)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=0)

        self.graph = g.Grafo()

        self.frames = {}
        for F in (StartPage, CircuitShow, CircuitBuilder):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def set_netlist(self):
        self.netlist_file = filedialog.askopenfile(mode="r", filetypes=[("Netlist files", "*.cir")])

    def getnetlist(self):
        return self.netlist_file


app = Application()
app.mainloop()
