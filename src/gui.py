from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
import accountmanager as am
def gui():
    window = Tk()
    # tuff
    WIDTH = 1234
    HEIGHT = 420
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.configure(bg = "#FFFFFF")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = HEIGHT,
        width = WIDTH,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    # Create title
    canvas.create_text(
        WIDTH / 2 - 150,
        0.0,
        anchor="nw",
        text="Fortnite account switcher 2025",
        fill="#000000",
        font=("ComicNeue Regular", 32 * -1)
    )
    class AccountTemplate:
        def __init__(self, nameandlevel, id):
            self.nameandlevel = nameandlevel
            self.id = id

        def create_gui(self):
            canvas.create_rectangle(
                36.0,
                60.0,
                150.0,
                176.0,
                fill="#D9D9D9",
                outline=""
            )
            canvas.create_text(
                50.0,
                70.0,
                anchor="nw",
                text=self.nameandlevel,
                fill="#000000",
                font=("ComicNeue Regular", 12 * -1)
            )
            button = Button(
                window,
                text="switch",
                command=lambda: accountmanager.switch_account(self.id)
            )
            button.place(x=WIDTH / 2 - 50, y=HEIGHT - 50)

    # Create entries


    window.resizable(False, False)
    window.mainloop()






