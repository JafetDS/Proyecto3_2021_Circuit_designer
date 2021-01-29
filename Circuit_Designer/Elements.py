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
    def __init__(self, master, name, value, conn_a, connn_b):
        tk.Canvas.__init__(self, master=master)
        self.config(width=100, height=150)

        # Connections
        self.connection_a = None
        self.connection_b = None

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
        self.image_label.pack()
        self.name_label.pack()
        self.value_label.pack()

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
    def __int__(self, master, name, value, conn_a, conn_b):
        ElectricalElement.__init__(self, master, name, value, conn_a, conn_b)
        self.set_image("images/Fuente.png")
        self.update()

class Resistor(ElectricalElement):
    def __init__(self,master, name, value, conn_a, conn_b):
        ElectricalElement.__init__(self, master, name, value, conn_a, conn_b)
        self.set_image("images/resistorsmall.png")
        self.update()
