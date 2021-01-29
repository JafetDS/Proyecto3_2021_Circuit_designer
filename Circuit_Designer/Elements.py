import tkinter as tk
from PIL import Image, ImageTk


class ElectricalElement (tk.Canvas):
    """
    this class is inherited from tkinter Canvas. It shows an image of an electrical element and its attributes

    ...
    Attributes
    ----------
    name_label : tk.Label
        a label that contains the name of the element
    value_label : tk.Label
        a label that contains the value fo the element. It has to be a numeric value

    Methods
    -------
    set_value(value)
        Sets the text of the value_label to the input parameter
    set_name(name)
        Sets the text of the name_label to the input parameter
    """
    def __init__(self, master, name, value, conn_a=None, connn_b=None):
        tk.Canvas.__init__(self, master=master)
        self.config(width=100, height=150)

        # Connections
        self.connection_a = conn_a
        self.connection_b = connn_b



        # resistor image
        self.image_label = tk.Label(self)

        # Resistor´s name label
        self.name_label = tk.Label(self)

        # Resistor´s value label
        self.value_label = tk.Label(self)

        # Sets name and value for the resistor
        self.name_label["text"] = name
        self.value_label["text"] = value

        # packing
        self.image_label.place(x=0, y=0)
        self.name_label.place(x=0, y=60)
        self.value_label.place(x=0, y=80)

        # Connection buttons
        self.a_btn = tk.Button(self, height=1, width=1)
        self.a_btn.place(x=0, y=25)

        self.b_btn = tk.Button(self, height=1, width=1)
        self.b_btn.place(x=90, y=25)


        #position (0 horizontal, 1 vertical)
        self.position = 0
    def set_image(self, imagepath):
        load = Image.open(imagepath)
        render = ImageTk.PhotoImage(load)
        self.image_label["image"] = render
        self.image_label.image = render

    def set_value(self, value):
        if value.isinstance(int) or value.isinstance(float):
            self.value_label["text"] = str(value)

    def set_name(self, name):
        self.name_label["text"] = name
    def get_name(self):
        return self.name_label["text"]


class PowerSource(ElectricalElement):
    def __init__(self,master, name, value, conn_a=None, conn_b=None):
        ElectricalElement.__init__(self, master, name, value, conn_a, conn_b)
        self.set_image("images/Fuente.png")
        self.update()

    def rotate(self, event):
        if self.position==1:
            self.set_image("images/Fuente.png")
            self.position = 0
        else:
            self.set_image("images/Fuente_rotada.png")
            self.position = 1

class Resistor(ElectricalElement):
    def __init__(self,master, name, value, conn_a=None, conn_b=None):
        ElectricalElement.__init__(self, master, name, value, conn_a, conn_b)
        self.set_image("images/resistorsmall.png")
        self.update()
    def rotate(self, event):
        if self.position==1:
            self.set_image("images/resistorsmall.png")
            self.position = 0
        else:
            self.set_image("images/resistorsmall_rotada.png")
            self.position = 1