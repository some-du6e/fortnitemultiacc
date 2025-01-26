from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
import accountmanager
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
    canvas.create_text(
        WIDTH / 2 - 150,
        500,
        anchor="nw",
        text="hawjtyag",
        fill="#000000",
        font=("ComicNeue Regular", 32 * -1)
    )
    # Create entries
    for i in range(1):  # Adjust the range as needed
        canvas.create_rectangle(
            36.0,
            60.0,
            150.0,
            176.0,
            fill="#D9D9D9",
            outline=""
        )
    print(accountmanager.get_accounts())
    window.resizable(False, False)
    window.mainloop()