from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
import GAME as g

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Load(GUI):
    file_path = filedialog.askopenfilename( title="Select Level File",filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")) )
    if file_path:
        Level = g.Load_level(file_path)
        if Level is not None:
            g.Game(GUI,Level)
window = Tk()

window.geometry("800x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    600.0,
    fill="#31A1F2",
    outline="")

canvas.create_rectangle(
    50.0,
    50.0,
    750.0,
    550.0,
    fill="#75CD74",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:Load(window),
    relief="flat"
)
button_1.place(
    x=176.0,
    y=338.0,
    width=489.0,
    height=67.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda : g.Game(GUI = window),
    relief="flat"
)
button_2.place(
    x=177.0,
    y=236.0,
    width=488.0,
    height=68.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command = g.Quit,
    relief="flat"
)
button_3.place(
    x=177.0,
    y=439.0,
    width=489.0,
    height=66.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    421.0,
    167.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
