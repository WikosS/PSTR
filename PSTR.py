# Créé par FARGIERE, le 19/10/2022 en Python 3.7

from PSTR_Unite import*
from tkinter import*

def ferme():
    fen.destroy()

def reduire():
    fen.state("iconic")

fen = Tk()
fen.title("Poké-clicker")
fen.attributes("-fullscreen", True)
fen.config(bg="black")

fen.update()
width = fen.winfo_width()
height = fen.winfo_height()

#Créations containers
frame_gauche = Frame(fen, bg="blue", width = (width-height)//2, height = height)
frame_centre = Frame(fen, bg="white", width = height, height = height)
frame_droite = Frame(fen, bg="red", width = (width-height)//2, height = height)

width_frame_gauche = width//4
height_frame_gauche = height

#Créations inventaires
PixelRef = PhotoImage(width = 1, height = 1)

Res = Canvas(frame_gauche, bg ="blue", width = width//4, height = round(height/4))
B0 = Button(frame_gauche, image = PixelRef, bg="white", width = width//4, height = round(height/8))
B1 = Button(frame_gauche, image = PixelRef, bg="red", width = width//4, height = round(height/8))
B2 = Button(frame_gauche, image = PixelRef, bg="blue", width = width//4, height = round(height/8))
B3 = Button(frame_gauche, image = PixelRef, bg="white", width = width//4, height = round(height/8))
B4 = Button(frame_gauche, image = PixelRef, bg="red", width = width//4, height = round(height/8))
B5 = Canvas(frame_gauche, bg="blue", width = width//4, height = round(height/8))

B12 = Canvas(frame_droite, bg ="blue", width = width//4, height = round(height/4))
B6 = Button(frame_droite, image = PixelRef, bg="white", width = width//4, height = round(height/8))
B7 = Button(frame_droite, image = PixelRef, bg="red", width = width//4, height = round(height/8))
B8 = Button(frame_droite, image = PixelRef, bg="blue", width = width//4, height = round(height/8))
B9 = Button(frame_droite, image = PixelRef, bg="white", width = width//4, height = round(height/8))
B10 = Button(frame_droite, image = PixelRef, bg="red", width = width//4, height = round(height/8))
B11 = Canvas(frame_droite, bg="blue", width = width//4, height = round(height/8))

BF = Button(frame_droite, text="X", width=5, height=1, command = ferme)
BR = Button(frame_droite, text="-", width=5, height=1, command = reduire)

frame_gauche.pack(side = LEFT)
frame_centre.pack(side = LEFT)
frame_droite.pack(side = LEFT)
Res.pack(side = TOP)


B0.pack(side = TOP)
B1.pack(side = TOP)
B2.pack(side = TOP)
B3.pack(side = TOP)
B4.pack(side = TOP)
B5.pack(side = TOP)

B12.pack(side = TOP)
B6.pack(side = TOP)
B7.pack(side = TOP)
B8.pack(side = TOP)
B9.pack(side = TOP)
B10.pack(side = TOP)
B11.pack(side = TOP)

BF.pack(side = RIGHT)
BR.pack(side = LEFT)




fen.mainloop()