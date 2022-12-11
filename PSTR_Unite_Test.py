import unittest

from unittest import TestCase

from math import sqrt

from PSTR_Unite import *

class TestUnite(TestCase) :

    def setUp (self):
        self.U = Unite(1,2,3,100,100,100,150,150,2)
        self.H = Unite(1,2,3,100,100,100,150,150,5)
        
    def test_Get_x(self):
        self.assertEqual(self.U.Get_x(), self.U.x)

    def test_Get_y(self):
        self.assertEqual(self.U.Get_y(), self.U.y)

    def test_Get_z(self):
        self.assertEqual(self.U.Get_z(), self.U.z)

    def test_Get_pv_mx(self):
        self.assertEqual(self.U.Get_pv_mx(), self.U.pv_mx)

    def test_Get_pv(self):
        self.assertEqual(self.U.Get_pv(), self.U.pv)

    def test_Get_pc(self):
        self.assertEqual(self.U.Get_pc(), self.U.pc)

    def test_Get_shield(self):
        self.assertEqual(self.U.Get_shield(), self.U.shield)

    def test_Get_gold(self):
        self.assertEqual(self.U.Get_gold(), self.U.gold)

    def test_Get_lv(self):
        self.assertEqual(self.U.Get_lv(), self.U.lv)

    def test_Get_cost_m(self):
        self.assertEqual(self.U.Get_cost_m(), self.U.cost_m)

    def test_Get_cost_e(self):
        self.assertEqual(self.U.Get_cost_e(), self.U.cost_e)

    def test_Get_xp(self):
        self.assertEqual(self.U.Get_xp(), self.U.xp)
        
    def test_Get_typ(self):
        self.assertEqual(self.U.Get_typ(), self.U.typ)

    def test_deplacer(self):
        self.U.deplacer(3,2,1)
        self.assertEqual(self.U.Get_x(), 4)
        self.assertEqual(self.U.Get_y(), 4)
        self.assertEqual(self.U.Get_z(), 4)

    def test_afficher_statistiques (self):
        self.assertEqual(self.U.afficher_statistiques(),"L'abscisse de l'unité est  4,L'ordonnée de l'unité est  4,La hauteur de l'unité est 4,Le nombre de points de vie maximum de l'unité est 100,Le nombre de points de vie actuel de l'unité est 100, Le nombre de points d'attaque de l'unité est 100,Le nombre de points d'armure de l'unité est 100, Le niveau de l'unité est 1,Le nombre de pièce d'or de l'unité est 0,Le coût en métal de l'unité est 150,Le coût en énergie de l'unité est 150,Le nombre de points d'expérience de l'unité est 0,Le type de l'unité est 5")

    def test_augmenter_po(self):
        self.U.augmenter_po(100)
        self.assertEqual(self.U.Get_gold,100)

    def test_subir_degats(self):
        self.U.subir_degats(75)
        self.assertEqual(self.U.Get_pv, 75 - (round(75 - (75*(100/(100 + 100))))))

    def test_reparer (self):
        self.U.reparer(500)
        self.assertEqual(self.U.Get_pv, 100)

    def test_augmenter_niveau(self):
        self.U.augmenter_niveau()
        self.assertEqual(self.U.Get_lv, 2)
        self.assertEqual(self.U.Get_pv,110)
        self.assertEqual(self.U.Get_pv_mx,110)
        self.assertEqual(self.U.Get_pc,110)
        self.assertEqual(self.U.Get_shield,110)

    def test_ressuciter(self):
        self.U.subir_degats(500)
        self.U.ressusciter()
        self.assertEqual(self.U.Get_pv,100)

    def test_augmenter_xp(self):
        self.U.augmenter_xp(1000)
        self.assertEqual(self.U.Get_xp, 1000)
        
    def test_soigner(self):
        self.U.subir_degats(75)
        self.H.soigner(U,500)
        self.assertEqual(self.U.Get_pv, 100)
    
    
    
