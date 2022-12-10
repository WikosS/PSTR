# Créé par Ethan, le 07/12/2022 en Python 3.7
from PSTR_Unite import*
from tkinter import*
from PIL import Image, ImageTk
import random

fen = Tk()
fen.title("PSTR")
fen.geometry("x1000")
fen.config(bg="black")

def deplacement(Joueur_Image,JEU):
    if Joueur_Image == Joueur_Image_H:
        if not colision_test(Joueur.x, Joueur.y-100):
            Joueur.y -= 100
            JEU.coords(Joueur_Image_H,Joueur.x,Joueur.y)
            JEU.coords(Joueur_Image_D,-100,-100)
            JEU.coords(Joueur_Image_G,-100,-100)
            JEU.coords(Joueur_Image_B,-100,-100)
    elif Joueur_Image == Joueur_Image_G:
        if not colision_test(Joueur.x - 100, Joueur.y):
            Joueur.x -= 100
            JEU.coords(Joueur_Image_G,Joueur.x,Joueur.y)
            JEU.coords(Joueur_Image_D,-100,-100)
            JEU.coords(Joueur_Image_H,-100,-100)
            JEU.coords(Joueur_Image_B,-100,-100)
    elif Joueur_Image == Joueur_Image_B:
        if not colision_test(Joueur.x, Joueur.y+100):
            Joueur.y += 100
            JEU.coords(Joueur_Image_B,Joueur.x,Joueur.y)
            JEU.coords(Joueur_Image_D,-100,-100)
            JEU.coords(Joueur_Image_H,-100,-100)
            JEU.coords(Joueur_Image_G,-100,-100)
    else:
        if not colision_test(Joueur.x + 100, Joueur.y):
            Joueur.x += 100
            JEU.coords(Joueur_Image_D,Joueur.x,Joueur.y)
            JEU.coords(Joueur_Image_G,-100,-100)
            JEU.coords(Joueur_Image_H,-100,-100)
            JEU.coords(Joueur_Image_B,-100,-100)

def colision_test(next_x, next_y):
    return [next_x, next_y] in colision or next_x >= 3100 or next_y >= 1700 or next_x < 0 or next_y < 0

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

    fen.after(25, anim)

def charger_map():
    fic = open("Map"+ "1" + ".txt", "rt")
    data = fic.readlines()
    fic.close

    for i in range (len(data)):
        data[i] = data[i].rstrip()

    return data

indice = 0
x_matt = 0
x_matt_2 = 150
x_matt_3 = 300
x_matt_4 = 450
x_matt_5 = 600
x_matt_6 = 750

colision = []

x = 0
y = 300

Joueur = Unite(x,y,0,100,50,50,42,42,1)


#IMAGES
pixel_ref = PhotoImage(width=1,height=1)
pixel_ref_button = PhotoImage(width=250,height=200)

Sable = Image.open("Textures/Sable.png")
Herbe = Image.open("Textures/Herbe.png")
Neige = Image.open("Textures/Neige.png")
Boss = Image.open("Textures/Boss.png")
Eau = Image.open("Textures/Eau.png")

Sable_resize = Sable.resize((10,10), resample = 3)
Herbe_resize = Herbe.resize((10,10), resample = 3)
Neige_resize = Neige.resize((10,10), resample = 3)
Boss_resize = Boss.resize((10,10), resample = 3)
Eau_resize = Eau.resize((10,10), resample = 3)

Sable_Tk = ImageTk.PhotoImage(Sable_resize)
Herbe_Tk = ImageTk.PhotoImage(Herbe_resize)
Neige_Tk = ImageTk.PhotoImage(Neige_resize)
Boss_Tk = ImageTk.PhotoImage(Boss_resize)
Eau_Tk = ImageTk.PhotoImage(Eau_resize)

Joueur_IMG_D = Image.open("Joueurs/Joueur_droite.png")
Joueur_IMG_G = Image.open("Joueurs/Joueur_gauche.png")
Joueur_IMG_B = Image.open("Joueurs/Joueur_bas.png")
Joueur_IMG_H = Image.open("Joueurs/Joueur_haut.png")

Joueur_resize_D = Joueur_IMG_D.resize((100,100), resample = 3)
Joueur_resize_G = Joueur_IMG_G.resize((100,100), resample = 3)
Joueur_resize_B = Joueur_IMG_B.resize((100,100), resample = 3)
Joueur_resize_H = Joueur_IMG_H.resize((100,100), resample = 3)

Joueur_Tk_D = ImageTk.PhotoImage(Joueur_resize_D)
Joueur_Tk_G = ImageTk.PhotoImage(Joueur_resize_G)
Joueur_Tk_B = ImageTk.PhotoImage(Joueur_resize_B)
Joueur_Tk_H = ImageTk.PhotoImage(Joueur_resize_H)

#FRAMES
frame_haut = Frame(fen, bg = "white", width = 1000, height = 100)
frame_millieu = Frame(fen, bg = "blue", width = 1000, height = 1000)
frame_bas = Frame(fen, bg = "red", width = 1000, height = 200)

#CANVAS HAUT
PUB = Canvas(frame_haut, width = 700, height = 100, bg = "white")
RES = Canvas(frame_haut, width = 300, height = 100, bg = "yellow")

#CANVAS MILLIEU
JEU = Canvas(frame_millieu, width = 1000, height = 1000, bg = "Gray")
COMBAT = Canvas(frame_millieu, width = 1000, height = 1000, bg = "Black")

#BOUTONS BAS
BT1 = Button(frame_bas,bg = "black", image = pixel_ref_button)
BT2 = Button(frame_bas,bg = "white", image = pixel_ref_button)
BT3 = Button(frame_bas,bg = "black", image = pixel_ref_button)
BT4 = Button(frame_bas,bg = "white", image = pixel_ref_button)

#CREATION DE LA PUB
Fichier = []
for i in range(1,9):
    Fichier.append(PhotoImage(file="Matts/matt" + str(i) + ".gif").subsample(13,13))

indice, x_matt = 0, 0

Matt = PUB.create_image(x_matt, 0, image=Fichier[indice], anchor='nw')
Matt2 = PUB.create_image(x_matt_2, 0, image=Fichier[indice], anchor='nw')
Matt3 = PUB.create_image(x_matt_3, 0, image=Fichier[indice], anchor='nw')
Matt4 = PUB.create_image(x_matt_4, 0, image=Fichier[indice], anchor='nw')
Matt5 = PUB.create_image(x_matt_5, 0, image=Fichier[indice], anchor='nw')
Matt6 = PUB.create_image(x_matt_6, 0, image=Fichier[indice], anchor='nw')

#GENERATION DE LA MAP
coord_y = 0 - 10

#for i in charger_map():
#    coord_y += 10
#    coord_x = 0
#    for e in i:
#        if e == "O":
#            JEU.create_image(coord_x, coord_y, image= Eau_Tk, anchor='nw')
#            colision.append([coord_x,coord_y])
#        elif e == "B":
#            JEU.create_image(coord_x, coord_y, image= Boss_Tk, anchor='nw')
#        elif e == "S":
#            JEU.create_image(coord_x, coord_y, image= Sable_Tk, anchor='nw')
#        elif e == "H":
#            JEU.create_image(coord_x, coord_y, image= Herbe_Tk, anchor='nw')
#        elif e == "N":
#            JEU.create_image(coord_x, coord_y, image= Neige_Tk, anchor='nw')
#        coord_x += 10

#CREATION DES JOUEURS
Joueur_Image_D = JEU.create_image((Joueur.x, Joueur.y),image=Joueur_Tk_D, anchor='nw')
Joueur_Image_G = JEU.create_image((-100,-100),image=Joueur_Tk_G, anchor='nw')
Joueur_Image_B = JEU.create_image((-100,-100),image=Joueur_Tk_B, anchor='nw')
Joueur_Image_H = JEU.create_image((-100,-100),image=Joueur_Tk_H, anchor='nw')


#ASSIGNATION DES TOUCHES
fen.focus_set()

fen.bind("z", lambda event, tx = "z" :  deplacement(Joueur_Image_H,JEU))
fen.bind("q", lambda event, tx = "q" :  deplacement(Joueur_Image_G,JEU))
fen.bind("s", lambda event, tx = "s" :  deplacement(Joueur_Image_B,JEU))
fen.bind("d", lambda event, tx = "d" :  deplacement(Joueur_Image_D,JEU))
fen.bind("Z", lambda event, tx = "Z" :  deplacement(Joueur_Image_H,JEU))
fen.bind("Q", lambda event, tx = "Q" :  deplacement(Joueur_Image_G,JEU))
fen.bind("S", lambda event, tx = "S" :  deplacement(Joueur_Image_B,JEU))
fen.bind("D", lambda event, tx = "D" :  deplacement(Joueur_Image_D,JEU))




#PACKS FRAMES
frame_haut.pack(side = TOP)
frame_millieu.pack(side = TOP)
frame_bas.pack(side = TOP)

#PACKS CANVAS HAUT
RES.pack(side = LEFT)
PUB.pack(side = LEFT)

#PACKS CANVAS MILLIEU
JEU.pack()

#PACKS BOUTONS BAS
BT1.pack(side = LEFT)
BT2.pack(side = LEFT)
BT3.pack(side = LEFT)
BT4.pack(side = LEFT)

anim()

fen.mainloop()

