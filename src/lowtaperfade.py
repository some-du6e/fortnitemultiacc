import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# sybau pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import gui

def main():
    def sure():
        with open(os.path.expanduser('~/.config/fnmanager/ignoresafetywarnings'), 'w') as fp:
            pass
        window.destroy()

    window = Tk()
    # tuff
    WIDTH = 1234
    HEIGHT = 420
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=HEIGHT,
        width=WIDTH,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    # Create title
    canvas.create_text(
        WIDTH / 2 - 250,
        0.0,
        anchor="nw",
        text="be deaduzz read the readme blud",
        fill="#000000",
        font=("ComicNeue Regular", 32 * -1)
    )
    button = Button(
        window,
        text="yeah i read it",
        command=lambda: sure()
    )
    button.place(x=WIDTH / 2 - 50, y=HEIGHT - 50)
    button = Button(
        window,
        text="hell nah exit",
        command=lambda: exit()
    )
    button.place(x=999, y=HEIGHT - 50)

    window.resizable(False, False)
    window.mainloop()

main()