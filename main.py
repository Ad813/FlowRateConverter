from lib import litres_per_min_to_cubic_metre_per_sec
from tkinter import Tk
from enum import IntEnum

class Volume(IntEnum):
    CUBIC_METRE = 0

class Capacity(IntEnum):
    LITRE = 0

class Time(IntEnum):
    SECOND = 0


root = Tk()
root.title("Volumetric Flow Rate Converter")
root.geometry("400x400")


# Volume Drop Down
volume_label = Label(root, text="Volume")
volume_label.grid(row=0, column=0)

volume_dropdown = OptionMenu(root, Volume, Volume.CUBIC_METRE)
volume_dropdown.grid(row=1, column=0)

root.mainloop()
