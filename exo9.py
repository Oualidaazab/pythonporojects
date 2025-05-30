#----------------------------------------------------------------------------------------------------
#✅ Exercice 9                                                                                       | 
#Objectif : Implémenter une méthode redéfinie pour plusieurs types.                                  |
#Consignes :                                                                                         |
#1. Créer une classe Figure avec une méthode aire() retournant 0.                                    |
#2. Créer deux classes dérivées :                                                                    |
#• Cercle avec rayon → aire = π × r2                                                                 |
#• Rectangle avec longueur et largeur → aire = L × l                                                 |
#3. Créer une liste contenant des objets Cercle et Rectangle.                                        |
#4. Afficher l’aire de chaque figure avec une boucle.                                                |
#----------------------------------------------------------------------------------------------------


class Figure:
    def aire(self):
        return 0

class Cercle(Figure):
    def __init__(self,r):
        self.r = r

    def aire(self):
        return 3.14*self.r**2

class Rectangle(Figure):
    def __init__(self,l,L):
        self.l = l
        self.L = L

    def aire(self):
        return self.l * self.L


figures = [Cercle(2.5),Rectangle(12,14),Cercle(5.7),Rectangle(2,2)]

for f in figures:
    print(f"l'aire de la figure {type(f).__name__} est:{f.aire()}")
