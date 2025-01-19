import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pygame
import src.gui

def main():
    pygame.mixer.init()
    def massive():
        pygame.mixer.music.load("src/massive.mp3")
        pygame.mixer.music.play()
    def lazyahh():
        pygame.mixer.music.load("src/massive.mp3")
        pygame.mixer.music.play()
        os.system()
        os.system("python %USERPROFILE%/.config/fnmanager/src/lowtaperfade.py")

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
        text="MASSIVE SAFETY RISK (read readme)",
        fill="#000000",
        font=("ComicNeue Regular", 32 * -1)
    )
    canvas.create_text(
        WIDTH / 2 - 617,
        100.0,
        anchor="nw",
        text='do "python %USERPROFILE%/.config/fnmanager/src/lowtaperfade.py" in cmd to get rid of ts',
        fill="#000000",
        font=("ComicNeue Regular", 16 * -1)
    )

    button = Button(
        window,
        text="ok",
        command=lambda: massive()
    )
    button.place(x=WIDTH / 2 - 50, y=HEIGHT - 50)
    button = Button(
        window,
        text="do it for me",
        command=lambda: lazyahh()
    )
    button.place(x=999, y=HEIGHT - 50)

    window.resizable(False, False)
    window.mainloop()

