import random
import time
import tkinter as tk
import Elements as Ele
from tkinter import filedialog
from tkinter import simpledialog
import threading
import Grafo as g
import Ordenamiento as o
from tkinter import messagebox

class StartPage (tk.Frame):
    """
    This is the start page frame. It offers the possibility between choosing a netlist file to build a circuit or building
    it in the interface
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(width=1280, height=720)

        load_btn = tk.Button(self, text="Load a netlist", command=lambda: self.go_to_cicuit())
        load_btn.pack()

        build_btn = tk.Button(self, text="Build your circuit", command= lambda: controller.show_frame("CircuitBuilder"))
        build_btn.pack()

    def go_to_cicuit(self):
        """
        It goes to frame with the circuit built from a Netlist file
        Returns
        -------

        """
        self.controller.set_netlist()
        self.controller.show_frame("CircuitShow")
        self.controller.parsed_file = self.controller.getnetlist().readlines()


class CircuitShow(tk.Frame):
    """
    It shows a circuit built from a netlist file and exports it to a graph to calculate the path with less tension
    between two nodes
    """
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

        #
        self.pop_thread = threading.Thread(target=self.populate_activator)

        # sorting buttons
        self.orden_ascendente_btn = tk.Button(self, text="Ordenar ▲", command=lambda: self.controller.ascendant_popup(self.resistors))
        self.orden_ascendente_btn.place(x=0, y=700)

        self.orden_descendente_btn = tk.Button(self, text="Ordenar ▼",command=lambda: self.controller.descendant_popup(self.resistors))
        self.orden_descendente_btn.place(x=150, y=700)

        self.pop_thread.start()

    def populate_activator(self):

        while not self.populated:
            if self.old_parsed != self.controller.parsed_file:
                self.populate_aux()
                self.populated = True
            time.sleep(1)


    def populate_aux(self):
        """
        It creates the objects (resistors and power sources) that are dictated in the netlist and shows them on the screen
        Returns
        -------

        """
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
    """
    On this fram you build your own circuit by creating and moving aroound resistors and direct current power sources
    """
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
        self.p_list = []

        self.orden_ascendente_btn = tk.Button(self.canvas, text = "Ordenar ▲",command=lambda: self.controller.ascendant_popup(self.r_list))
        self.orden_ascendente_btn.place(x=0, y=700)


        self.orden_descendente_btn = tk.Button(self.canvas, text = "Ordenar ▼",command=lambda: self.controller.descendant_popup(self.r_list))
        self.orden_descendente_btn.place(x=150, y=700)

    def add_dc(self):
        """
        it add a direct current power source to the screen with name and value specified by the user
        Returns
        -------

        """
        pwr_name = tk.simpledialog.askstring (title="Power Source´s name", prompt="Write the Power Source´s name",
                                                   parent=self.canvas)
        pwr_value = tk.simpledialog.askstring (title="Power Source´s value", prompt="Write the power source´s value",
                                                    parent=self.canvas)
        pw = Ele.PowerSource(self.canvas, pwr_name, pwr_value)
        self.p_list.append(pw)
        pw.place(x=300, y=300)

        self.make_draggable(pw)
        pw.bind ("<Button-3>", pw.rotate)

    def add_resistor(self):
        """
                it add a resistor to the screen with name and value specified by the user
                Returns
                -------

                """
        resistor_name = tk.simpledialog.askstring(title="Resistor´s name", prompt="Write the resistor´s name"
                                                  , parent=self.canvas)
        resistor_value = tk.simpledialog.askstring(title="Resistor´s value", prompt="Write the resistor´s value",
                                                   parent=self.canvas)
        r = Ele.Resistor(self.canvas, resistor_name, resistor_value)
        self.r_list.append(r)
        r.place(x=300, y=300)
        self.make_draggable(r)
        r.bind("<Button-3>",  r.rotate)

    def make_draggable(self, widget):
        """
        it allows the electronic elements to be dragged around the screen
        """
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
        """It shows a specifies frame"""
        frame = self.frames[page_name]
        frame.tkraise()

    def set_netlist(self):
        """it sets the netlist attribute according to the file that the user chooses"""
        self.netlist_file = filedialog.askopenfile(mode="r", filetypes=[("Netlist files", "*.cir")])

    def getnetlist(self):
        return self.netlist_file

    def ascendant_popup(self, lista):
        messagebox.showinfo(title="ascendant order", message=str(self.sort_elements(lista, "▲")))

    def descendant_popup(self, lista):
        messagebox.showinfo(title="descendant order", message=str(self.sort_elements(lista, "▼")))

    def sort_elements(self, lista, order):
        """

        Parameters
        ----------
        lista
        order

        Returns
        -------
        an ordered list in ascendant or descendent order
        """
        names = []
        for i in lista:
            names.append(i.get_name())
        ordered_names =[]
        if order == "▲":
            ordered_names = o.Ordenamiento.qsaux(names)
        elif order == "▼":
            ordered_names = o.Ordenamiento.insertsort(names)
        return ordered_names


app = Application()
app.mainloop()
