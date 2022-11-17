class Unite :

    def __init__(self,x,y,z,pv_mx,pc,shield,cost_m,cost_e,typ):

        assert type(x) == int and type(y) == int and type(z) == int
        assert type(pv_mx) == int and pv_mx > 0
        assert type(pc) == int and pc >= 0
        assert type(shield) == int and shield >= 0
        assert type(cost_m) == int and cost_m > 0
        assert type(cost_e) == int and cost_e > 0
        assert 1 <= typ <= 4
        # Assignation des types : 1(organique) 2(mechanique) 3(mecano) 4(medecin)

        self.x = x
        self.y = y
        self.z = z
        self.pv_mx = pv_mx
        self.pv = pv_mx
        self.pc = pc
        self.shield = shield
        self.lv = 1
        self.gold = 0
        self.cost_m = cost_m
        self.cost_e = cost_e
        self.xp = 0
        self.typ = typ
        if typ == 2:
            self.tx = 5
            self.ty = 3
            self.tz = 3
        elif typ == 3:
            self.tx = 9
            self.ty = 9
            self.tz = 8
        else:
            self.tx = 1
            self.ty = 1
            self.tz = 2

    def Get_x(self):
        return(self.x)

    def Get_y(self):
        return(self.y)

    def Get_z(self):
        return(self.z)

    def Get_pv_mx(self):
        return(self.pv_mx)

    def Get_pv(self):
        return(self.pv)

    def Get_pc(self):
        return(self.pc)

    def Get_shield(self):
        return(self.shield)

    def Get_lv(self):
        return(self.lv)

    def Get_gold(self):
        return(self.gold)

    def Get_cost_m(self):
        return(self.cost_m)

    def Get_cost_e(self):
        return(self.cost_e)

    def Get_xp(self):
        return(self.xp)

    def Get_typ(self):
        return(self.typ)

    def deplacer(self,dx,dy,dz):
        self.x += dx
        self.y += dy
        self.z += dz

    def afficher_statistiques(self):

        #Description : affiche les statistiques de l'unité,
        #Paramètres : rien,
        #Valeur de retour : STR - Chaîne de caractère - Phrases contenants les statistiques de l'unité,
        #Préconditions : rien,
        #Postconditions : la méthode ne modifie pas les valeurs,

        print("L'abscisse de l'unité est ", self.x )
        print("L'ordonnée de l'unité est ", self.y )
        print("La hauteur de l'unité est ", self.z )
        print("Le nombre de points de vie maximum de l'unité est ", self.pv_mx )
        print("Le nombre de points de vie actuel de l'unité est ", self.pv )
        print("Le nombre de points d'attaque de l'unité est ", self.pc )
        print("Le nombre de points d'armure de l'unité est ", self.shield )
        print("Le niveau de l'unité est ", self.lv )
        print("Le nombre de pièce d'or de l'unité est ", self.gold )
        print("Le coût en métal de l'unité est ", self.cost_m )
        print("Le coût en énergie de l'unité est ", self.cost_e )
        print("Le nombre de points d'expérience de l'unité est ", self.xp )
        print("Le type de l'unité est ", self.typ )

    def augmenter_po(self,po_gagnees):

        #Description : augmente le nombre de pièces d'or en ajoutant la variable "po_gagnees",
        #Paramètres : po_gagnees - INT - entier positif ajouter au nombre de pieces d'or de l'unité,
        #Valeur de retour : rien,
        #Préconditions : "po_gagnees" doit-être un entier positif,
        #Postconditions : le nombre de pieces d'or de l'unité est modifié

        assert type(po_gagnees) == int and po_gagnees > 0

        self.gold += po_gagnees

    def subir_degats(self,degats):

        #Description : diminie le nombre de points de vie de l'unité en fonction des degats et du bouclier,
        #Paramètres : degats - INT - nombre de degats théoriquement infligés,
        #Valeur de retour : rien,
        #Préconditions : "degats" est un entier supérieur ou égal à 0,
        #Postconditions : le nombre de points de vie est modifié et est supérieur ou égal à 0,

        assert type(degats) == int and degats >= 0

        degats_subits = round(degats - (degats*(self.shield/(self.shield + 100))))
        if self.pv - degats_subits <= 0:
            self.pv = 0
        else:
            self.pv -= degats_subits

    def reparer (self,pv_gagnes):

        #Description : augment le nombre de points de vie de l'unité en fonction de "pv_gagnes",
        #Paramètres : pv_gagnes - INT - entier supèrieur,
        #Valeur de retour : rien,
        #Préconditions : "pv_gagnes" est supèrieur à 0 et le nombre de points de vie de l'unité est supèrieur à 0,
        #Postconditions : les points de vie de l'unité sont modifiés si ils étaient superieurs à 0,

        assert type(pv_gagnes) == int and pv_gagnes > 0

        if self.pv != 0:
            if self.pv + pv_gagnes >= self.pv_mx:
                self.pv = self.pv_mx
            else:
                self.pv += pv_gagnes

    def augmenter_niveau(self):

        #Description : augmente les statistiques de l'unité lors de la prise d'un niveau,
        #Paramètres : rien,
        #Valeur de retour : rien,
        #Préconditions : rien,
        #Postconditions : les statistiques sont modifiées

        self.lv += 1
        self.pv = round(self.pv * 1.1)
        self.pv_mx = round(self.pv_mx * 1.1)
        self.pc = round(self.pc * 1.1)
        self.shield = round(self.shield * 1.1)

    def ressusciter(self):

        #Description : ressuscite une unité,
        #Paramètres : rien,
        #Valeur de retour : rien,
        #Préconditions : rien,
        #Postconditions : le nombre de point de vie de l'unité est remis au maximum si il était différent de 0,

        if self.pv == 0:
            self.pv = self.pv_mx

    def augmenter_xp(self,xp_gagne):

        #Description : ajoute l'expérience gagné à celle déjà aquise par l'unité,
        #Paramètres : xp - INT - nombre de point d'expérience à ajouter,
        #Valeur de retour : rien,
        #Préconditions : "xp_gagne" est un entier positif,
        #Postconditions : le nombre de point d'expérience de l'unité est augmenté,

        assert type(xp_gagne) == int and xp_gagne > 0

        self.xp += xp_gagne

    def soigner(self,healer,pv_gagnes):

        #Description : vérifie que le type du soigneur correspond au type de l'unité soigné et appelles la fonction réparer,
        #Paramètres : healer - Unite - Unite soignée, pv_gagnes - INT - entier supèrieur,
        #Valeur de retour : rien,
        #Préconditions : les types correspondent ,"pv_gagnes" est un entier positif, "healer" est une Unite,
        #Postconditions : la méthode reparer est appliquée à "healer",

        assert self.typ + healer.typ == 7

        healer.reparer(pv_gagnes)


#carte = Canvas(fen, bg = "black", width = height, height = height)
#cart = PhotoImage(file = "Grass.png")
#gras = carte.create_image(x, y, image= cart)

#print (width)
#print (height)
#bouton_trp1 = Button(fen, bg= "yellow", text="Soldat corps à corps", width = width//33, height= height//80)
#bouton_trp2 = Button(fen, bg= "yellow", text="Docteur", width = width//33, height= height//80)
#bouton_trp3 = Button(fen, bg= "yellow", text="Soldat distance", width = width//33, height= height//80)
#bouton_trp4 = Button(fen, bg= "yellow", text="Char", width = width//33, height= height//80)
#bouton_trp5 = Button(fen, bg= "yellow", text="Mécanicien", width = width//33, height= height//80)
#bouton_trp0 = Button(fen, bg= "yellow", text="Ressources", width = width//33, height= height//80)

#bouton_ferme = Button(fen, text="X", width=5, height=1, command = ferme)
#bouton_reduire = Button(fen, text="-", width=5, height=1, command = reduire)

#bouton_trp0.pack(side = LEFT)
#bouton_trp1.place(x = 0,y = 7*height//40, anchor = NW)
#bouton_trp2.place(x = 0,y = 14*height//40, anchor = NW)
#bouton_trp3.place(x = 0,y = 21*height//40, anchor = NW)
#bouton_trp4.place(x = 0,y = 28*height//40, anchor = NW)
#bouton_trp5.place(x = 0,y = 35*height//40, anchor = NW)
#carte.place(x= (width-height)//2, y = 0, anchor = NW)
#bouton_ferme.place(x = width - 45, y = 0, anchor= NW)
#bouton_reduire.place(x = width - 90, y = 0, anchor= NW)

