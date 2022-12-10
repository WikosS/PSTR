# Créé par Ethan, le 07/12/2022 en Python 3.7
from PSTR_Unite import*
from tkinter import*
from PIL import Image, ImageTk
import random

fen = Tk()
fen.title("Not a PSTR")
fen.attributes("-fullscreen", True)
fen.config(bg="black")

fen.update()
width = fen.winfo_width()
height = fen.winfo_height()

def combat(x,y):
    coord = [x,y]
    for e in mechant:
        if coord == [e[1],e[2]]:
            cb = Tk()
            cb.title("Combat")
            cb.attributes("-fullscreen", True)
            if Joueur.pv or e[0].pv > 0:
                cb.destroy()

def deplacement(Joueur_Image,JEU):
    if Joueur_Image == Joueur_Image_H:
        if not colision_test(Joueur.x, Joueur.y-(16*(height//20)//17)):
            Joueur.y -= (16*(height//20)//17)
            JEU.coords(Joueur_Image_H,Joueur.x,Joueur.y)
            JEU.coords(Joueur_Image_D,-100,-100)
            JEU.coords(Joueur_Image_G,-100,-100)
            JEU.coords(Joueur_Image_B,-100,-100)
            combat(Joueur.x, Joueur.y)
    elif Joueur_Image == Joueur_Image_G:
        if not colision_test(Joueur.x - width//31, Joueur.y):
            Joueur.x -= width//31
            JEU.coords(Joueur_Image_G,Joueur.x,Joueur.y)
            JEU.coords(Joueur_Image_D,-100,-100)
            JEU.coords(Joueur_Image_H,-100,-100)
            JEU.coords(Joueur_Image_B,-100,-100)
            combat(Joueur.x, Joueur.y)
    elif Joueur_Image == Joueur_Image_B:
        if not colision_test(Joueur.x, Joueur.y+(16*(height//20)//17)):
            Joueur.y += (16*(height//20)//17)
            JEU.coords(Joueur_Image_B,Joueur.x,Joueur.y)
            JEU.coords(Joueur_Image_D,-100,-100)
            JEU.coords(Joueur_Image_H,-100,-100)
            JEU.coords(Joueur_Image_G,-100,-100)
            combat(Joueur.x, Joueur.y)
    else:
        if not colision_test(Joueur.x + width//31, Joueur.y):
            Joueur.x += width//31
            JEU.coords(Joueur_Image_D,Joueur.x,Joueur.y)
            JEU.coords(Joueur_Image_G,-100,-100)
            JEU.coords(Joueur_Image_H,-100,-100)
            JEU.coords(Joueur_Image_B,-100,-100)
            combat(Joueur.x, Joueur.y)

def acheter_damage_bonus():
    Joueur.acheter_damage_bonus()

def acheter_helth_bonus():
    Joueur.acheter_health_bonus()

def acheter_armor_bonus():
    Joueur.acheter_armor_bonus()

def acheter_damage_multiplier():
    Joueur.acheter_damage_multiplier()

def acheter_armor_multiplier():
    Joueur.acheter_armor_multiplier()

def colision_test(next_x, next_y):
    return [next_x, next_y] in colision or next_x >= 30*width//31 or next_y >= 17*(16*(height//20)//17) or next_x < 0 or next_y < 0

def anim():
    global x_matt, x_matt_2, x_matt_3, x_matt_4, x_matt_5, x_matt_6, indice, Fichier
    x_matt += 4
    x_matt_2 += 4
    x_matt_3 += 4
    x_matt_4 += 4
    x_matt_5 += 4
    x_matt_6 += 4

    if x_matt > fen.winfo_width():
        x_matt = -10
    if x_matt_2 > fen.winfo_width():
        x_matt_2 = -10
    if x_matt_3 > fen.winfo_width():
        x_matt_3 = -10
    if x_matt_4 > fen.winfo_width():
        x_matt_4 = -10
    if x_matt_5 > fen.winfo_width():
        x_matt_5 = -10
    if x_matt_6 > fen.winfo_width():
        x_matt_6 = -10


    indice +=1
    if indice == 8:
        indice = 0

    PUB.itemconfig(Matt, image=Fichier[indice])
    PUB.itemconfig(Matt2, image=Fichier[indice])
    PUB.itemconfig(Matt3, image=Fichier[indice])
    PUB.itemconfig(Matt4, image=Fichier[indice])
    PUB.itemconfig(Matt5, image=Fichier[indice])
    PUB.itemconfig(Matt6, image=Fichier[indice])

    PUB.coords(Matt, x_matt, 0)
    PUB.coords(Matt2, x_matt_2, 0)
    PUB.coords(Matt3, x_matt_3, 0)
    PUB.coords(Matt4, x_matt_4, 0)
    PUB.coords(Matt5, x_matt_5, 0)
    PUB.coords(Matt6, x_matt_6, 0)

    fen.after(25, anim)

def ferme():
    fen.destroy()

def reduire():
    fen.state("iconic")

indice = 0
x_matt = 0
x_matt_2 = 150
x_matt_3 = 300
x_matt_4 = 450
x_matt_5 = 600
x_matt_6 = 750

colision = []

x = 0
y = 15*(16*(height//20)//17)

Joueur = Unite(x,y,0,100,50,50,42,42,1)
Mechant = Unite(-100,-100,0,100,50,50,42,42,1)
mechant = [[Mechant,width//31,15*(16*(height//20)//17)]]


#IMAGES
pixel_ref = PhotoImage(width=1,height=1)
pixel_ref_button = PhotoImage(width=width//3,height=3*height//20)

Sable = Image.open("Textures/Sable.png")
Herbe = Image.open("Textures/Herbe.png")
Neige = Image.open("Textures/Neige.png")
Boss = Image.open("Textures/Boss.png")
Mur = Image.open("Textures/Mur.png")

Sable_resize = Sable.resize((width//31,(16*(height//20)//17)), resample = 3)
Herbe_resize = Herbe.resize((width//31,(16*(height//20)//17)), resample = 3)
Neige_resize = Neige.resize((width//31,(16*(height//20)//17)), resample = 3)
Boss_resize = Boss.resize((width//31,(16*(height//20)//17)), resample = 3)
Mur_resize = Mur.resize((width//31,(16*(height//20)//17)), resample = 3)

Sable_Tk = ImageTk.PhotoImage(Sable_resize)
Herbe_Tk = ImageTk.PhotoImage(Herbe_resize)
Neige_Tk = ImageTk.PhotoImage(Neige_resize)
Boss_Tk = ImageTk.PhotoImage(Boss_resize)
Mur_Tk = ImageTk.PhotoImage(Mur_resize)

Joueur_IMG_D = Image.open("Joueurs/Joueur_droite.png")
Joueur_IMG_G = Image.open("Joueurs/Joueur_gauche.png")
Joueur_IMG_B = Image.open("Joueurs/Joueur_bas.png")
Joueur_IMG_H = Image.open("Joueurs/Joueur_haut.png")

Joueur_resize_D = Joueur_IMG_D.resize((width//31,(16*(height//20)//17)), resample = 3)
Joueur_resize_G = Joueur_IMG_G.resize((width//31,(16*(height//20)//17)), resample = 3)
Joueur_resize_B = Joueur_IMG_B.resize((width//31,(16*(height//20)//17)), resample = 3)
Joueur_resize_H = Joueur_IMG_H.resize((width//31,(16*(height//20)//17)), resample = 3)

Joueur_Tk_D = ImageTk.PhotoImage(Joueur_resize_D)
Joueur_Tk_G = ImageTk.PhotoImage(Joueur_resize_G)
Joueur_Tk_B = ImageTk.PhotoImage(Joueur_resize_B)
Joueur_Tk_H = ImageTk.PhotoImage(Joueur_resize_H)

Mechant_IMG = Image.open("Joueurs/Mechant.png")

Mechant_resize = Mechant_IMG.resize((width//31,(16*(height//20)//17)), resample = 3)

Mechant_Tk = ImageTk.PhotoImage(Mechant_resize)

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

#CANVAS MILIEU
JEU = Canvas(frame_millieu, width = width, height = (16*height//20), bg = "Gray")
COMBAT = Canvas(frame_millieu, width = width, height = (16*height//20), bg = "Black")

#BOUTONS BAS
BT1 = Button(frame_bas, bg="black", image=pixel_ref_button, command=acheter_damage_bonus)
BT2 = Button(frame_bas, bg="white", image=pixel_ref_button, command=acheter_helth_bonus)
BT3 = Button(frame_bas, bg="black", image=pixel_ref_button, command=acheter_armor_bonus)

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
coord_y = 0 - (16*(height//20)//17)

fic = open("Map"+ "1" + ".txt", "rt")
data = fic.readlines()
fic.close()

for i in range (len(data)):
    data[i] = data[i].rstrip()

for i in range (len(data)):
    coord_y += (16*(height//20)//17)
    coord_x = 0
    for e in data[i]:
        if e == "%":
            JEU.create_image(coord_x, coord_y, image= Mur_Tk, anchor='nw')
            colision.append([coord_x,coord_y])
        elif e == "F":
            JEU.create_image(coord_x, coord_y, image= Boss_Tk, anchor='nw')
        elif e == "S":
            JEU.create_image(coord_x, coord_y, image= Sable_Tk, anchor='nw')
        elif e == "H":
            JEU.create_image(coord_x, coord_y, image= Herbe_Tk, anchor='nw')
        elif e == "N":
            JEU.create_image(coord_x, coord_y, image= Neige_Tk, anchor='nw')
        coord_x += (width//31)

#CREATION IMAGES JOUEURS
Joueur_Image_D = JEU.create_image((Joueur.x, Joueur.y),image=Joueur_Tk_D, anchor='nw')
Joueur_Image_G = JEU.create_image((-100,-100),image=Joueur_Tk_G, anchor='nw')
Joueur_Image_B = JEU.create_image((-100,-100),image=Joueur_Tk_B, anchor='nw')
Joueur_Image_H = JEU.create_image((-100,-100),image=Joueur_Tk_H, anchor='nw')

#CREATION ENNEMIS
Mechant1 = Unite(round(random.randint(1,31))*(width//31),round(random.randint(15,16))*(16*(height//20)//17),0,100,50,50,42,42,1)

Mechant2 = Unite(round(random.randint(29,30))*(width//31),round(random.randint(0,14))*(16*(height//20)//17),0,100,50,50,42,42,1)

Mechant3 = Unite(round(random.randint(0,28))*(width//31),round(random.randint(0,1))*(16*(height//20)//17),0,100,50,50,42,42,1)
Mechant4 = Unite(round(random.randint(0,28))*(width//31),round(random.randint(0,1))*(16*(height//20)//17),0,100,50,50,42,42,1)

Mechant5 = Unite(round(random.randint(0,1))*(width//31),round(random.randint(2,13))*(16*(height//20)//17),0,100,50,50,42,42,1)

Mechant6 = Unite(round(random.randint(2,26))*(width//31),round(random.randint(12,13))*(16*(height//20)//17),0,100,50,50,42,42,1)
Mechant7 = Unite(round(random.randint(2,26))*(width//31),round(random.randint(12,13))*(16*(height//20)//17),0,100,50,50,42,42,1)

Mechant8 = Unite(round(random.randint(25,26))*(width//31),round(random.randint(3,11))*(16*(height//20)//17),0,100,50,50,42,42,1)

Mechant9 = Unite(round(random.randint(3,24))*(width//31),round(random.randint(3,4))*(16*(height//20)//17),0,100,50,50,42,42,1)
Mechant10 = Unite(round(random.randint(3,24))*(width//31),round(random.randint(3,4))*(16*(height//20)//17),0,100,50,50,42,42,1)

Mechant11 = Unite(round(random.randint(3,4))*(width//31),round(random.randint(5,10))*(16*(height//20)//17),0,100,50,50,42,42,1)

#CREATION IMAGES ENNEMIS
Ennemis = [Mechant1,Mechant2,Mechant3,Mechant4,Mechant5,Mechant6,Mechant7,Mechant8,Mechant9,Mechant10,Mechant11]

for e in Ennemis:
    Mechant_nom = str(e)+"_image"
    Mechant_nom = JEU.create_image((e.x, e.y), image=Mechant_Tk, anchor='nw')

#ASSIGNATION DES TOUCHES
fen.focus_set()

fen.bind("z", lambda event, tx = "z" : deplacement(Joueur_Image_H,JEU))
fen.bind("q", lambda event, tx = "q" : deplacement(Joueur_Image_G,JEU))
fen.bind("s", lambda event, tx = "s" : deplacement(Joueur_Image_B,JEU))
fen.bind("d", lambda event, tx = "d" : deplacement(Joueur_Image_D,JEU))
fen.bind("Z", lambda event, tx = "Z" : deplacement(Joueur_Image_H,JEU))
fen.bind("Q", lambda event, tx = "Q" : deplacement(Joueur_Image_G,JEU))
fen.bind("S", lambda event, tx = "S" : deplacement(Joueur_Image_B,JEU))
fen.bind("D", lambda event, tx = "D" : deplacement(Joueur_Image_D,JEU))

#PACKS FRAMES
frame_haut.pack(side = TOP)
frame_millieu.pack(side = TOP)
frame_bas.pack(side = TOP)

#PACKS BUTTON HAUT
BF.pack(side = RIGHT)
BR.pack(side = RIGHT)

#PACKS CANVAS HAUT
PUB.pack(side = RIGHT)
RES.pack(side = RIGHT)

#PACKS CANVAS MILIEU
JEU.pack()

#PACKS BUTTON BAS
BT1.pack(side = LEFT)
BT2.pack(side = LEFT)
BT3.pack(side = LEFT)

anim()

fen.mainloop()
