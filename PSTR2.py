# Créé par FARGIERE, le 10/11/2022 en Python 3.7
from PSTR_Unite import*
from tkinter import*
from PIL import*

indice = 0
x_matt = 0
x_matt_2 = 150
x_matt_3 = 300
x_matt_4 = 450
x_matt_5 = 600
x_matt_6 = 750


x = 0
y = 0

def anim():

    global x_matt, x_matt_2, x_matt_3, x_matt_4, x_matt_5, x_matt_6, indice, Fichier
    x_matt += 4
    x_matt_2 += 4
    x_matt_3 += 4
    x_matt_4 += 4
    x_matt_5 += 4
    x_matt_6 += 4

    if x_matt > 900:
        x_matt = -10
    if x_matt_2 > 900:
        x_matt_2 = -10
    if x_matt_3 > 900:
        x_matt_3 = -10
    if x_matt_4 > 900:
        x_matt_4 = -10
    if x_matt_5 > 900:
        x_matt_5 = -10
    if x_matt_6 > 900:
        x_matt_6 = -10


    indice +=1
    if indice == 8:
        indice = 0

    PUB.itemconfig(Matt, image = Fichier[indice])
    PUB.itemconfig(Matt2, image = Fichier[indice])
    PUB.itemconfig(Matt3, image = Fichier[indice])
    PUB.itemconfig(Matt4, image = Fichier[indice])
    PUB.itemconfig(Matt5, image = Fichier[indice])
    PUB.itemconfig(Matt6, image = Fichier[indice])

    PUB.coords(Matt, x_matt, 0)
    PUB.coords(Matt2, x_matt_2, 0)
    PUB.coords(Matt3, x_matt_3, 0)
    PUB.coords(Matt4, x_matt_4, 0)
    PUB.coords(Matt5, x_matt_5, 0)
    PUB.coords(Matt6, x_matt_6, 0)

    fen.after(50, anim)

def ferme():
    fen.destroy()

def reduire():
    fen.state("iconic")

def creer_trp(nb):
    if nb == 1:
        Soldat_cac = Unite(x,y,0,100,20,50,50,50,1)
    if nb == 2:
        Medecin = Unite(x,y,0,100,0,100,75,75,4)
    if nb == 3:
        Soldat_dst = Unite(x,y,0,75,20,25,75,100,1)
    if nb == 4:
        Char = Unite(x,y,0,200,99,50,200,150,2)
    else:
        Mecano = Unite(x,y,0,100,0,100,100,100,3)

fen = Tk()
fen.title("PSTR")
fen.attributes("-fullscreen", True)
fen.config(bg="black")

fen.update()
width = fen.winfo_width()
height = fen.winfo_height()

#IMAGES
pixel_ref = PhotoImage(width=1,height=1)
pixel_ref_button = PhotoImage(width=width//5,height=3*height//20)

#FRAMES
frame_haut = Frame(fen, bg = "white", width = width, height = height//20)
frame_millieu = Frame(fen, bg = "blue", width = width, height = (16*height//20))
frame_bas = Frame(fen, bg = "red", width = width, height = (3*height//20))

#BOUTONS HAUT
BF = Button(frame_haut, text = "X", width = 5, height = 1, command = ferme)
BR = Button(frame_haut, text="-", width = 5, height = 1, command = reduire)

#CANVAS HAUT
PUB = Canvas(frame_haut, width = width - 500 - 5, height = 22, bg = "white")
RES = Canvas(frame_haut, width = 500, height = 22, bg = "yellow")

#CANVAS MILLIEU
JEU = Canvas(frame_millieu, width = width, height = (16*height//20), bg = "Gray")

#BOUTONS BAS
BT1 = Button(frame_bas,bg = "black", image = pixel_ref_button, command = creer_trp(1))
BT2 = Button(frame_bas,bg = "white", image = pixel_ref_button, command = creer_trp(2))
BT3 = Button(frame_bas,bg = "black", image = pixel_ref_button, command = creer_trp(3))
BT4 = Button(frame_bas,bg = "white", image = pixel_ref_button, command = creer_trp(4))
BT5 = Button(frame_bas,bg = "black", image = pixel_ref_button, command = creer_trp(5))

#CREATION DE LA PUB
Fichier = []
for i in range(1,9):
    Fichier.append(PhotoImage(file="matt" + str(i) + ".gif").subsample(13,13))

indice, x_matt = 0, 0

Matt = PUB.create_image(x_matt, 0, image=Fichier[indice], anchor='nw')
Matt2 = PUB.create_image(x_matt_2, 0, image=Fichier[indice], anchor='nw')
Matt3 = PUB.create_image(x_matt_3, 0, image=Fichier[indice], anchor='nw')
Matt4 = PUB.create_image(x_matt_4, 0, image=Fichier[indice], anchor='nw')
Matt5 = PUB.create_image(x_matt_5, 0, image=Fichier[indice], anchor='nw')
Matt6 = PUB.create_image(x_matt_6, 0, image=Fichier[indice], anchor='nw')

#PACKS FRAMES
frame_haut.pack(side = TOP)
frame_millieu.pack(side = TOP)
frame_bas.pack(side = TOP)

#PACKS BOUTONS HAUT
BF.pack(side = RIGHT)
BR.pack(side = RIGHT)

#PACKS CANVAS HAUT
PUB.pack(side = RIGHT)
RES.pack(side = RIGHT)

#PACKS CANVAS MILLIEU
JEU.pack()

#PACKS BOUTONS BAS
BT1.pack(side = LEFT)
BT2.pack(side = LEFT)
BT3.pack(side = LEFT)
BT4.pack(side = LEFT)
BT5.pack(side = LEFT)

anim()
fen.mainloop()
