

from PSTR_Unite import*
from tkinter import*
from PIL import Image, ImageTk
import random

fen = Tk()
fen.title("JEU")
fen.attributes("-fullscreen", True)
fen.config(bg="black")

fen.update()
width = fen.winfo_width()
height = fen.winfo_height()

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

Joueur = Unite(x, y, 0, 100, 50, 50, 42, 42, 1)
Joueur.gold = 1000

def combat(x, y):
    coord = [x, y]
    coord_boss = [Boss.x, Boss.y]
    coord_boss_2 = [Boss.x + width//31, Boss.y]
    coord_boss_3 = [Boss.x + 2*width//31, Boss.y]
    coord_boss_4 = [Boss.x, Boss.y + (16*(height//20)//17)]
    coord_boss_5 = [Boss.x + width//31, Boss.y + (16*(height//20)//17)]
    coord_boss_6 = [Boss.x + 2*width//31, Boss.y + (16*(height//20)//17)]
    coord_boss_7 = [Boss.x, Boss.y + 2*(16*(height//20)//17)]
    coord_boss_8 = [Boss.x + width//31, Boss.y + 2*(16*(height//20)//17)]
    coord_boss_9 = [Boss.x + 2*width//31, Boss.y + 2*(16*(height//20)//17)]

    for e in Ennemis:
        coord_ennemie = [e.x, e.y]
        if coord == coord_ennemie:
            cb = Tk()
            cb.title("Combat")
            cb.attributes("-fullscreen", True)
            strt = random.randint(1, 100)
            if strt > 100//Joueur.lv:
                while Joueur.pv > 0 and e.pv > 0:
                    Joueur.subir_degats(e.pc)
                    e.subir_degats(Joueur.Get_true_damage())
            else:
                while Joueur.pv > 0 and e.pv > 0:
                    e.subir_degats(Joueur.Get_true_damage())
                    Joueur.subir_degats(e.pc)
            cb.destroy()
            if Joueur.pv >= 0:
                if e.typ == 2:
                    JEU.coords(Mechant1_image, -100, -100)
                elif e.typ == 3:
                    JEU.coords(Mechant2_image, -100, -100)
                elif e.typ == 4:
                    JEU.coords(Mechant3_image, -100, -100)
                elif e.typ == 5:
                    JEU.coords(Mechant4_image, -100, -100)
                elif e.typ == 6:
                    JEU.coords(Mechant5_image, -100, -100)
                elif e.typ == 7:
                    JEU.coords(Mechant6_image, -100, -100)
                elif e.typ == 8:
                    JEU.coords(Mechant7_image, -100, -100)
                elif e.typ == 9:
                    JEU.coords(Mechant8_image, -100, -100)
                elif e.typ == 10:
                    JEU.coords(Mechant9_image, -100, -100)
                elif e.typ == 11:
                    JEU.coords(Mechant10_image, -100, -100)
                elif e.typ == 12:
                    JEU.coords(Mechant11_image, -100, -100)
                elif e.typ == 14:
                    JEU.coords(Mechant13_image, -100, -100)
                elif e.typ == 15:
                    JEU.coords(Mechant14_image, -100, -100)
                elif e.typ == 16:
                    JEU.coords(Mechant15_image, -100, -100)
                elif e.typ == 17:
                    JEU.coords(Mechant16_image, -100, -100)
                elif e.typ == 18:
                    JEU.coords(Mechant17_image, -100, -100)
                elif e.typ == 19:
                    JEU.coords(Mechant18_image, -100, -100)
                elif e.typ == 20:
                    JEU.coords(Mechant19_image, -100, -100)
    recalc_stats_label()

    if coord == coord_boss or coord == coord_boss_2 or coord == coord_boss_3 or coord == coord_boss_4 or coord == coord_boss_5 or coord == coord_boss_6 or coord == coord_boss_7 or coord == coord_boss_8 or coord == coord_boss_9:
        print("a")
        cb = Tk()
        cb.title("Combat")
        cb.attributes("-fullscreen", True)
        strt = random.randint(1, 100)
        if strt > 100//Joueur.lv:
            while Joueur.pv > 0 and e.pv > 0:
                Joueur.subir_degats(e.pc)
                e.subir_degats(Joueur.pc)
        else:
            while Joueur.pv > 0 and e.pv > 0:
                e.subir_degats(Joueur.pc)
                Joueur.subir_degats(e.pc)
        cb.destroy()
        fin()

def recalc_stats_label():
    global Stats_Label
    Stats_Label.config(text="PV : "+str(Joueur.Get_pv())+"/"+str(Joueur.Get_true_max_health())+"    DMG : "+
                            str(Joueur.Get_true_damage()) + "    Shield : "+str(Joueur.Get_true_shield())+"    Gold : " + str(Joueur.Get_gold()))
    BT1.config(text="Upgrade DMG    Cost : "+str(Joueur.Get_bonus_damage_cost())+" Gold")
    BT2.config(text="Upgrade Max Health  Cost : "+str(Joueur.Get_bonus_Health_cost())+" Gold")
    BT3.config(text="Upgrade Shield   Cost : "+str(Joueur.Get_bonus_armor_cost())+" Gold")

def deplacement(Joueur_Image, JEU):
    if Joueur_Image == Joueur_Image_H:
        if not colision_test(Joueur.x, Joueur.y-(16*(height//20)//17)):
            Joueur.y -= (16*(height//20)//17)
            JEU.coords(Joueur_Image_H, Joueur.x, Joueur.y)
            JEU.coords(Joueur_Image_D, -100, -100)
            JEU.coords(Joueur_Image_G, -100, -100)
            JEU.coords(Joueur_Image_B, -100, -100)
            combat(Joueur.x, Joueur.y)
    elif Joueur_Image == Joueur_Image_G:
        if not colision_test(Joueur.x - width//31, Joueur.y):
            Joueur.x -= width//31
            JEU.coords(Joueur_Image_G, Joueur.x, Joueur.y)
            JEU.coords(Joueur_Image_D, -100, -100)
            JEU.coords(Joueur_Image_H, -100, -100)
            JEU.coords(Joueur_Image_B, -100, -100)
            combat(Joueur.x, Joueur.y)
    elif Joueur_Image == Joueur_Image_B:
        if not colision_test(Joueur.x, Joueur.y+(16*(height//20)//17)):
            Joueur.y += (16*(height//20)//17)
            JEU.coords(Joueur_Image_B, Joueur.x, Joueur.y)
            JEU.coords(Joueur_Image_D, -100, -100)
            JEU.coords(Joueur_Image_H, -100, -100)
            JEU.coords(Joueur_Image_G, -100, -100)
            combat(Joueur.x, Joueur.y)
    else:
        if not colision_test(Joueur.x + width//31, Joueur.y):
            Joueur.x += width//31
            JEU.coords(Joueur_Image_D, Joueur.x, Joueur.y)
            JEU.coords(Joueur_Image_G, -100, -100)
            JEU.coords(Joueur_Image_H, -100, -100)
            JEU.coords(Joueur_Image_B, -100, -100)
            combat(Joueur.x, Joueur.y)


def acheter_damage_bonus():
    Joueur.acheter_damage_bonus()
    recalc_stats_label()

def acheter_health_bonus():
    Joueur.acheter_health_bonus()
    recalc_stats_label()

def acheter_armor_bonus():
    Joueur.acheter_armor_bonus()
    recalc_stats_label()


def colision_test(next_x, next_y):
    return [next_x, next_y] in colision or next_x >= 30*width//31 or next_y >= 17*(16*(height//20)//17) or next_x < 0 or next_y < 0

def anim():
    global x_matt, x_matt_2, x_matt_3, x_matt_4, x_matt_5, x_matt_6, indice, Fichier
    x_matt += (width-505)//300
    x_matt_2 += (width-505)//300
    x_matt_3 += (width-505)//300
    x_matt_4 += (width-505)//300
    x_matt_5 += (width-505)//300
    x_matt_6 += (width-505)//300

    if x_matt > width-505:
        x_matt = -10
    elif x_matt_2 > width-505:
        x_matt_2 = -10
    elif x_matt_3 > width-505:
        x_matt_3 = -10
    elif x_matt_4 > width-505:
        x_matt_4 = -10
    elif x_matt_5 > width-505:
        x_matt_5 = -10
    elif x_matt_6 > width-505:
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

def debut():
    deb = Tk()
    deb.title("DEBUT")
    deb.attributes("-fullscreen", True)
    deb.config(bg="black")

    deb.update()
    width = deb.winfo_width()
    height = deb.winfo_width()

    def Jouer():
        deb.destroy()

    def Stop():
        deb.destroy()
        fen.destroy()

    TEXT = Label(deb, bg="black", font=("Arial", width//40), text="BIENVENUE DANS NOTRE JEUX VIDEO", fg="white")
    START = Button(deb, text="JOUER", bg="blue", width=width//50, height=height //500, command=Jouer)
    STOP = Button(deb, text="FERMER", bg="red", width=width//50, height=height //500, command=Stop)

    TEXT.place(x=width//2, y=height//5, anchor='s')
    START.place(x=width//2-width//7, y=height//3, anchor='nw')
    STOP.place(x=width//2, y=height//3, anchor='nw')

    deb.mainloop()

def fin():
    fin = Tk()
    fin.title("FIN")
    fin.attributes("-fullscreen", True)
    fin.config(bg="black")

    FIN = Canvas(fin, bg = "black", width = width, height = height)

    FIN.pack()

    ferme()

    fin.mainloop()

#IMAGES
pixel_ref_button = PhotoImage(width=width//3, height=3*height//20, file="Textures/Buttons.png")
stats_label_img = Image.open("Textures/Buttons.png")

stats_label_img_resize = stats_label_img.resize((450, 30), resample=3)

stats_label_img = ImageTk.PhotoImage(stats_label_img_resize)
button_img = Image.open("Textures/Buttons.png")

button_img_resize = button_img.resize((width//3, 3*height//20), resample=3)
button_img_2_resize =button_img.resize((width//3-10, 3*height//20), resample=3)

button_img = ImageTk.PhotoImage(button_img_resize)
button_img_2 = ImageTk.PhotoImage(button_img_2_resize)

Mur = Image.open("Textures/%.png")
A = Image.open("Textures/A.png")
B = Image.open("Textures/B.png")
C = Image.open("Textures/C.png")
D = Image.open("Textures/D.png")
E = Image.open("Textures/E.png")
F = Image.open("Textures/F.png")
G = Image.open("Textures/G.png")
H = Image.open("Textures/H.png")
I = Image.open("Textures/I.png")
J = Image.open("Textures/J.png")
K = Image.open("Textures/K.png")
L = Image.open("Textures/L.png")
M = Image.open("Textures/M.png")
N = Image.open("Textures/N.png")
O = Image.open("Textures/O.png")
P = Image.open("Textures/P.png")
Q = Image.open("Textures/Q.png")
R = Image.open("Textures/R.png")
S = Image.open("Textures/S.png")
T = Image.open("Textures/T.png")
U = Image.open("Textures/U.png")
V = Image.open("Textures/V.png")
W = Image.open("Textures/W.png")
X = Image.open("Textures/X.png")
Y = Image.open("Textures/Y.png")
Z = Image.open("Textures/Z.png")
ZZ = Image.open("Textures/ZZ.png")
AB = Image.open("Textures/AB.png")
CD = Image.open("Textures/CD.png")
EF = Image.open("Textures/EF.png")
GH = Image.open("Textures/GH.png")
IJ = Image.open("Textures/IJ.png")
KL = Image.open("Textures/KL.png")
MN = Image.open("Textures/MN.png")
OP = Image.open("Textures/OP.png")
QR = Image.open("Textures/QR.png")

Mur_resize = Mur.resize((width//31, (16*(height//20)//17)), resample=3)
A_resize = A.resize((width//31, (16*(height//20)//17)), resample=3)
B_resize = B.resize((width//31, (16*(height//20)//17)), resample=3)
C_resize = C.resize((width//31, (16*(height//20)//17)), resample=3)
D_resize = D.resize((width//31, (16*(height//20)//17)), resample=3)
E_resize = E.resize((width//31, (16*(height//20)//17)), resample=3)
F_resize = F.resize((width//31, (16*(height//20)//17)), resample=3)
G_resize = G.resize((width//31, (16*(height//20)//17)), resample=3)
H_resize = H.resize((width//31, (16*(height//20)//17)), resample=3)
I_resize = I.resize((width//31, (16*(height//20)//17)), resample=3)
J_resize = J.resize((width//31, (16*(height//20)//17)), resample=3)
K_resize = K.resize((width//31, (16*(height//20)//17)), resample=3)
L_resize = L.resize((width//31, (16*(height//20)//17)), resample=3)
M_resize = M.resize((width//31, (16*(height//20)//17)), resample=3)
N_resize = N.resize((width//31, (16*(height//20)//17)), resample=3)
O_resize = O.resize((width//31, (16*(height//20)//17)), resample=3)
P_resize = P.resize((width//31, (16*(height//20)//17)), resample=3)
Q_resize = Q.resize((width//31, (16*(height//20)//17)), resample=3)
R_resize = R.resize((width//31, (16*(height//20)//17)), resample=3)
S_resize = S.resize((width//31, (16*(height//20)//17)), resample=3)
T_resize = T.resize((width//31, (16*(height//20)//17)), resample=3)
U_resize = U.resize((width//31, (16*(height//20)//17)), resample=3)
V_resize = V.resize((width//31, (16*(height//20)//17)), resample=3)
W_resize = W.resize((width//31, (16*(height//20)//17)), resample=3)
X_resize = X.resize((width//31, (16*(height//20)//17)), resample=3)
Y_resize = Y.resize((width//31, (16*(height//20)//17)), resample=3)
Z_resize = Z.resize((width//31, (16*(height//20)//17)), resample=3)
ZZ_resize = ZZ.resize((width//31, (16*(height//20)//17)), resample=3)
AB_resize = AB.resize((width//31, (16*(height//20)//17)), resample=3)
CD_resize = CD.resize((width//31, (16*(height//20)//17)), resample=3)
EF_resize = EF.resize((width//31, (16*(height//20)//17)), resample=3)
GH_resize = GH.resize((width//31, (16*(height//20)//17)), resample=3)
IJ_resize = IJ.resize((width//31, (16*(height//20)//17)), resample=3)
KL_resize = KL.resize((width//31, (16*(height//20)//17)), resample=3)
MN_resize = MN.resize((width//31, (16*(height//20)//17)), resample=3)
OP_resize = OP.resize((width//31, (16*(height//20)//17)), resample=3)
QR_resize = QR.resize((width//31, (16*(height//20)//17)), resample=3)

Mur_Tk = ImageTk.PhotoImage(Mur_resize)
A_Tk = ImageTk.PhotoImage(A_resize)
B_Tk = ImageTk.PhotoImage(B_resize)
C_Tk = ImageTk.PhotoImage(C_resize)
D_Tk = ImageTk.PhotoImage(D_resize)
E_Tk = ImageTk.PhotoImage(E_resize)
F_Tk = ImageTk.PhotoImage(F_resize)
G_Tk = ImageTk.PhotoImage(G_resize)
H_Tk = ImageTk.PhotoImage(H_resize)
I_Tk = ImageTk.PhotoImage(I_resize)
J_Tk = ImageTk.PhotoImage(J_resize)
K_Tk = ImageTk.PhotoImage(K_resize)
L_Tk = ImageTk.PhotoImage(L_resize)
M_Tk = ImageTk.PhotoImage(M_resize)
N_Tk = ImageTk.PhotoImage(N_resize)
O_Tk = ImageTk.PhotoImage(O_resize)
P_Tk = ImageTk.PhotoImage(P_resize)
Q_Tk = ImageTk.PhotoImage(Q_resize)
R_Tk = ImageTk.PhotoImage(R_resize)
S_Tk = ImageTk.PhotoImage(S_resize)
T_Tk = ImageTk.PhotoImage(T_resize)
U_Tk = ImageTk.PhotoImage(U_resize)
V_Tk = ImageTk.PhotoImage(V_resize)
W_Tk = ImageTk.PhotoImage(W_resize)
X_Tk = ImageTk.PhotoImage(X_resize)
Y_Tk = ImageTk.PhotoImage(Y_resize)
Z_Tk = ImageTk.PhotoImage(Z_resize)
ZZ_Tk = ImageTk.PhotoImage(ZZ_resize)
AB_Tk = ImageTk.PhotoImage(AB_resize)
CD_Tk = ImageTk.PhotoImage(CD_resize)
EF_Tk = ImageTk.PhotoImage(EF_resize)
GH_Tk = ImageTk.PhotoImage(GH_resize)
IJ_Tk = ImageTk.PhotoImage(IJ_resize)
KL_Tk = ImageTk.PhotoImage(KL_resize)
MN_Tk = ImageTk.PhotoImage(MN_resize)
OP_Tk = ImageTk.PhotoImage(OP_resize)
QR_Tk = ImageTk.PhotoImage(QR_resize)

Joueur_IMG_D = Image.open("Joueurs/Joueur_droite.png")
Joueur_IMG_G = Image.open("Joueurs/Joueur_gauche.png")
Joueur_IMG_B = Image.open("Joueurs/Joueur_bas.png")
Joueur_IMG_H = Image.open("Joueurs/Joueur_haut.png")

Joueur_resize_D = Joueur_IMG_D.resize((width//31, (16*(height//20)//17)), resample=3)
Joueur_resize_G = Joueur_IMG_G.resize((width//31, (16*(height//20)//17)), resample=3)
Joueur_resize_B = Joueur_IMG_B.resize((width//31, (16*(height//20)//17)), resample=3)
Joueur_resize_H = Joueur_IMG_H.resize((width//31, (16*(height//20)//17)), resample=3)

Joueur_Tk_D = ImageTk.PhotoImage(Joueur_resize_D)
Joueur_Tk_G = ImageTk.PhotoImage(Joueur_resize_G)
Joueur_Tk_B = ImageTk.PhotoImage(Joueur_resize_B)
Joueur_Tk_H = ImageTk.PhotoImage(Joueur_resize_H)

Mechant_IMG = Image.open("Joueurs/Mechant.png")
Boss_IMG = Image.open("Joueurs/Boss.png")

Mechant_resize = Mechant_IMG.resize((width//31, (16*(height//20)//17)), resample=3)
Boss_resize = Boss_IMG.resize((3*width//31, 3*(16*(height//20)//17)), resample=3)

Mechant_Tk = ImageTk.PhotoImage(Mechant_resize)
Boss_Tk = ImageTk.PhotoImage(Boss_resize)

#FRAMES
frame_haut = Frame(fen, bg="white", width=width, height=height//20)
frame_millieu = Frame(fen, bg="blue", width=width, height=(16*height//20))
frame_bas = Frame(fen, bg="red", width=width, height=(3*height//20))

#BOUTONS HAUT
BF = Button(frame_haut, text="X", width=5, height=1, command=ferme)
BR = Button(frame_haut, text="-", width=5, height=1, command=reduire)

#CANVAS HAUT
PUB = Canvas(frame_haut, width=width - 500 - 5, height=22, bg="white")
RES = Canvas(frame_haut, width=500, height=22, bg="yellow")

#CANVAS MILIEU
JEU = Canvas(frame_millieu, width=width, height=(16*height//20), bg="black")
COMBAT = Canvas(frame_millieu, width=width, height=(16*height//20), bg="Black")

#CREATION DE LA PUB
Fichier = []
for i in range(1,9):
    Fichier.append(PhotoImage(file="Matts/matt" + str(i) + ".gif").subsample(13, 13))

Matt = PUB.create_image(x_matt, 0, image=Fichier[indice], anchor='nw')
Matt2 = PUB.create_image(x_matt_2, 0, image=Fichier[indice], anchor='nw')
Matt3 = PUB.create_image(x_matt_3, 0, image=Fichier[indice], anchor='nw')
Matt4 = PUB.create_image(x_matt_4, 0, image=Fichier[indice], anchor='nw')
Matt5 = PUB.create_image(x_matt_5, 0, image=Fichier[indice], anchor='nw')
Matt6 = PUB.create_image(x_matt_6, 0, image=Fichier[indice], anchor='nw')

#BOUTONS BAS
BT1 = Button(frame_bas, width=width//3, height=(3*height//20), image=button_img, bg="black", command=acheter_damage_bonus, text="N/A", compound="center", fg='yellow', font=("Courrier", width//70))
BT2 = Button(frame_bas, width=width//3, height=(3*height//20), image=button_img, bg="black", command=acheter_health_bonus, text="N/A", compound="center", fg='yellow', font=("Courrier", width//70))
BT3 = Button(frame_bas, width=width//3, height=(3*height//20), image=button_img, bg="black", command=acheter_armor_bonus, text="N/A", compound="center", fg='yellow', font=("Courrier", width//70))

#GENERATION AFFICHAGE STATS
Stats_Label = Label(RES, text="N/A", width=500, image=stats_label_img, compound='center', fg='yellow', font=("Courier", width//200))
recalc_stats_label()

#GENERATION DE LA MAP
coord_y = 0 - (16*(height//20)//17)

fic = open("Map"+"1" + ".txt", "rt")
data = fic.readlines()
fic.close()

for i in range(len(data)):
    data[i] = data[i].rstrip()

for i in range(len(data)):
    coord_y += (16*(height//20)//17)
    coord_x = 0
    for e in data[i]:
        if e == "%":
            JEU.create_image(coord_x, coord_y, image=Mur_Tk, anchor='nw')
            colision.append([coord_x, coord_y])
        elif e == "!":
            JEU.create_image(coord_x, coord_y, image=X_Tk, anchor='nw')
        elif e == ":":
            JEU.create_image(coord_x, coord_y, image=Y_Tk, anchor='nw')
        elif e == "#":
            JEU.create_image(coord_x, coord_y, image=Z_Tk, anchor='nw')
        elif e == "@":
            JEU.create_image(coord_x, coord_y, image=ZZ_Tk, anchor='nw')
        elif e == "X":
            JEU.create_image(coord_x, coord_y, image=AB_Tk, anchor='nw')
        elif e == "Y":
            JEU.create_image(coord_x, coord_y, image=CD_Tk, anchor='nw')
        elif e == "Z":
            JEU.create_image(coord_x, coord_y, image=EF_Tk, anchor='nw')
        elif e == "?":
            JEU.create_image(coord_x, coord_y, image=GH_Tk, anchor='nw')
        elif e == "$":
            JEU.create_image(coord_x, coord_y, image=IJ_Tk, anchor='nw')
            colision.append([coord_x, coord_y])
        elif e == ">":
            JEU.create_image(coord_x, coord_y, image=KL_Tk, anchor='nw')
            colision.append([coord_x, coord_y])
        elif e == ")":
            JEU.create_image(coord_x, coord_y, image=MN_Tk, anchor='nw')
            colision.append([coord_x, coord_y])
        elif e == "(":
            JEU.create_image(coord_x, coord_y, image=OP_Tk, anchor='nw')
            colision.append([coord_x, coord_y])
        elif e == "<":
            JEU.create_image(coord_x, coord_y, image=QR_Tk, anchor='nw')
            colision.append([coord_x, coord_y])
        else:
            JEU.create_image(coord_x, coord_y, image=globals()[e+"_Tk"], anchor='nw')

        coord_x += (width//31)

#CREATION IMAGES JOUEUR
Joueur_Image_D = JEU.create_image((Joueur.x, Joueur.y), image=Joueur_Tk_D, anchor='nw')
Joueur_Image_G = JEU.create_image((-100, -100), image=Joueur_Tk_G, anchor='nw')
Joueur_Image_B = JEU.create_image((-100, -100), image=Joueur_Tk_B, anchor='nw')
Joueur_Image_H = JEU.create_image((-100, -100), image=Joueur_Tk_H, anchor='nw')

#CREATION ENNEMIS
Mechant1 = Unite(round(random.randint(1, 30))*(width//31), round(random.randint(15, 16))*(16*(height//20)//17), 0, 1, 5, 0, 42, 42, 2)
Mechant2 = Unite(round(random.randint(29, 30))*(width//31), round(random.randint(0, 14))*(16*(height//20)//17), 0, 20, 25, 50, 42, 42, 3)
Mechant3 = Unite(round(random.randint(0, 28))*(width//31), round(random.randint(0, 1))*(16*(height//20)//17), 0, 20, 25, 50, 42, 42, 4)
Mechant4 = Unite(round(random.randint(0, 28))*(width//31), round(random.randint(0, 1))*(16*(height//20)//17), 0, 20, 25, 50, 42, 42, 5)
Mechant5 = Unite(round(random.randint(0, 1))*(width//31), round(random.randint(2, 13))*(16*(height//20)//17), 0, 20, 25, 50, 42, 42, 6)
Mechant6 = Unite(round(random.randint(2, 26))*(width//31), round(random.randint(12, 13))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 7)
Mechant7 = Unite(round(random.randint(2, 26))*(width//31), round(random.randint(12, 13))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 8)
Mechant8 = Unite(round(random.randint(26, 27))*(width//31), round(random.randint(3, 11))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 9)
Mechant9 = Unite(round(random.randint(3, 24))*(width//31), round(random.randint(3, 4))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 10)
Mechant10 = Unite(round(random.randint(3, 24))*(width//31), round(random.randint(3, 4))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 11)
Mechant11 = Unite(round(random.randint(3, 4))*(width//31), round(random.randint(5, 10))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 12)
Mechant13 = Unite(8*(width//31), round(random.randint(6, 10))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 14)
Mechant14 = Unite(10*(width//31), round(random.randint(6, 10))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 15)
Mechant15 = Unite(12*(width//31), round(random.randint(6, 10))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 16)
Mechant16 = Unite(14*(width//31), round(random.randint(6, 10))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 17)
Mechant17 = Unite(16*(width//31), round(random.randint(6, 10))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 18)
Mechant18 = Unite(18*(width//31), round(random.randint(6, 10))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 19)
Mechant19 = Unite(20*(width//31), round(random.randint(6, 10))*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 20)
Boss = Unite(22*(width//31), 7*(16*(height//20)//17), 0, 100, 50, 50, 42, 42, 21)

#CREATION IMAGES ENNEMIS
Ennemis = [Mechant1,Mechant2,Mechant3,Mechant4,Mechant5,Mechant6,Mechant7,Mechant8,Mechant9,Mechant10,Mechant11,Mechant13,Mechant14,Mechant15,Mechant16,Mechant17,Mechant18,Mechant19]

Mechant1_image = JEU.create_image(Mechant1.x, Mechant1.y, image=Mechant_Tk, anchor='nw')
Mechant2_image = JEU.create_image(Mechant2.x, Mechant2.y, image=Mechant_Tk, anchor='nw')
Mechant3_image = JEU.create_image(Mechant3.x, Mechant3.y, image=Mechant_Tk, anchor='nw')
Mechant4_image = JEU.create_image(Mechant4.x, Mechant4.y, image=Mechant_Tk, anchor='nw')
Mechant5_image = JEU.create_image(Mechant5.x, Mechant5.y, image=Mechant_Tk, anchor='nw')
Mechant6_image = JEU.create_image(Mechant6.x, Mechant6.y, image=Mechant_Tk, anchor='nw')
Mechant7_image = JEU.create_image(Mechant7.x, Mechant7.y, image=Mechant_Tk, anchor='nw')
Mechant8_image = JEU.create_image(Mechant8.x, Mechant8.y, image=Mechant_Tk, anchor='nw')
Mechant9_image = JEU.create_image(Mechant9.x, Mechant9.y, image=Mechant_Tk, anchor='nw')
Mechant10_image = JEU.create_image(Mechant10.x, Mechant10.y, image=Mechant_Tk, anchor='nw')
Mechant11_image = JEU.create_image(Mechant11.x, Mechant11.y, image=Mechant_Tk, anchor='nw')
Mechant13_image = JEU.create_image(Mechant13.x, Mechant13.y, image=Mechant_Tk, anchor='nw')
Mechant14_image = JEU.create_image(Mechant14.x, Mechant14.y, image=Mechant_Tk, anchor='nw')
Mechant15_image = JEU.create_image(Mechant15.x, Mechant15.y, image=Mechant_Tk, anchor='nw')
Mechant16_image = JEU.create_image(Mechant16.x, Mechant16.y, image=Mechant_Tk, anchor='nw')
Mechant17_image = JEU.create_image(Mechant17.x, Mechant17.y, image=Mechant_Tk, anchor='nw')
Mechant18_image = JEU.create_image(Mechant18.x, Mechant18.y, image=Mechant_Tk, anchor='nw')
Mechant19_image = JEU.create_image(Mechant19.x, Mechant19.y, image=Mechant_Tk, anchor='nw')

Boss_image = JEU.create_image(Boss.x, Boss.y, image=Boss_Tk, anchor='nw')

#ASSIGNATION DES TOUCHES
fen.focus_set()

fen.bind("z", lambda event, tx="z" : deplacement(Joueur_Image_H, JEU))
fen.bind("q", lambda event, tx="q" : deplacement(Joueur_Image_G, JEU))
fen.bind("s", lambda event, tx="s" : deplacement(Joueur_Image_B, JEU))
fen.bind("d", lambda event, tx="d" : deplacement(Joueur_Image_D, JEU))
fen.bind("Z", lambda event, tx="Z" : deplacement(Joueur_Image_H, JEU))
fen.bind("Q", lambda event, tx="Q" : deplacement(Joueur_Image_G, JEU))
fen.bind("S", lambda event, tx="S" : deplacement(Joueur_Image_B, JEU))
fen.bind("D", lambda event, tx="D" : deplacement(Joueur_Image_D, JEU))

#PACKS FRAMES
frame_haut.pack(side=TOP)
frame_millieu.pack(side=TOP)
frame_bas.pack(side=TOP)

#PACKS BUTTON HAUT
BF.pack(side=RIGHT)
BR.pack(side=RIGHT)

#PACKS CANVAS HAUT
PUB.pack(side=RIGHT)
RES.pack(side=RIGHT)

#PACKS CANVAS MILIEU
JEU.pack()

#PACKS BUTTON BAS
BT1.pack(side=LEFT)
BT2.pack(side=LEFT)
BT3.pack(side=LEFT)

#PACKS STATS LABEL
Stats_Label.pack(side=LEFT)

anim()
debut()
fen.mainloop()