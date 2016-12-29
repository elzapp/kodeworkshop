#-*- Coding: UTF-8 -*-
"""
tre på rad-program fra leksjon 6, her kan vi spille tre på rad
mot en annen person, annenhvert trekk.

I leksjon 7 skal vi utvide dette programmet slik at vi kan spille
mot datamaskinen
"""

from tkinter import Tk, Canvas, mainloop

main = Tk()

c = Canvas(main, width=600, height=600)
c.pack()

c.create_line(200, 0, 200, 600)
c.create_line(400, 0, 400, 600)

c.create_line(0, 200, 600, 200)
c.create_line(0, 400, 600, 400)

grid = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8",
]

def click(event):
    """
    Denne funksjonen kjører når du klikker i spillebrettet
    """
    shape = choose_shape()
    across = int(c.canvasx(event.x) / 200)
    down = int(c.canvasy(event.y) / 200)
    square = across + (down * 3)

    if grid[square] == "X" or grid[square] == "O":
        return

    if winner():
        return

    if shape == "O":
        c.create_oval(across * 200, down * 200,
                      (across+1) * 200, (down+1) * 200)
        grid[square] = "O"
    else:
        c.create_line(across * 200, down * 200,
                      (across+1) * 200, (down+1) * 200)
        c.create_line(across * 200, (down+1) * 200,
                      (across+1) * 200, down * 200)
        grid[square] = "X"

def choose_shape():
    """
    Finner ut hvem som skal ta neste trekk, ved å
    sjekke hvem som har færrest brikker på brettet
    """
    if grid.count("O") > grid.count("X"):
        return "X"
    else:
        return "O"

def winner():
    """
    Sjekker om vi har fått en vinner
    """
    for across in range(3):
        row = across * 3
        line = grid[row] + grid[row+1] + grid[row+2]
        if line == "XXX" or line == "OOO":
            return True

    for down in range(3):
        line = grid[down] + grid[down+3] + grid[down+6]
        if line == "XXX" or line == "OOO":
            return True

    line = grid[0] + grid[4] + grid[8]
    if line == "XXX" or line == "OOO":
        return True

    line = grid[2] + grid[4] + grid[6]
    if line == "XXX" or line == "OOO":
        return True

c.bind("<Button-1>", click)

mainloop()
