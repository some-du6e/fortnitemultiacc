from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

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

# create entries




window.resizable(False, False)
window.mainloop()
