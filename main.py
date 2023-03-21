from lib import litres_per_min_to_cubic_metre_per_sec
from tkinter import Tk, Label, OptionMenu, StringVar
from enum import StrEnum


class Volume(StrEnum):
    CUBIC_METRE = "Cubic Metre"
    CUBIC_CM = "Cubic CM"
    CUBIC_MM = "Cubic mm"
    CUBIC_MicroM = "Cubic um"

class Capacity(StrEnum):
    LITRE = "L"
    MILLILITRE = "mL"
    MICROLITRE = "uL"

class Time(StrEnum):
    SECOND = "Second"
    MINUTES = "Minutes"
    HOURS = "Hours"
    DAY = "Day"


root = Tk()
root.title("Volumetric Flow Rate Converter")
root.geometry("400x400")


# Volume Drop Down
volume_label = Label(root, text="Volume")
volume_label.grid(row=0, column=0)

volume_value = StringVar()
volume_dropdown = OptionMenu(root, volume_value, *[e.value for e in Volume])
volume_dropdown.grid(row=1, column=0)

root.mainloop()
