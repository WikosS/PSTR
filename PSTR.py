# Créé par FARGIERE, le 19/10/2022 en Python 3.7

from PSTR_Unite import*
from tkinter import*

def ferme():
    fen.destroy()

def reduire():
    fen.state("iconic")

fen = Tk()
fen.title("Projet stratégie temps réel")
fen.attributes("-fullscreen", True)
fen.config(bg="black")

fen.update()
width = fen.winfo_width()
height = fen.winfo_height()

x = width/2
y = height/2

jeu = Canvas(fen, bg = "black", width = width, height = height)

grass = PhotoImage(file = "Grass.png")

gras = jeu.create_image(x, y, image= grass)

bouton_ferme = Button(fen, text="X", width=5, height=1, command = ferme)
bouton_reduire = Button(fen, text="-", width=5, height=1, command = reduire)

jeu.pack()
bouton_ferme.place(x = width - 45, y = 0, anchor= NW)
bouton_reduire.place(x = width - 90, y = 0, anchor= NW)

fen.mainloop()