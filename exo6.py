#---------------------------------------------------------------------------- 
# Exercice 6
#Objectif : Comprendre l’héritage multi-niveaux.
#Consignes :
#. Créer une classe Vehicule avec :
# marque (str)
#. Créer une classe Voiture héritant de Vehicule, avec :
# nb_portes (int)
#. Créer une classe VoitureElectrique héritant de Voiture, avec :
# autonomie (int, en km)
#4. Ajouter une méthode infos() dans chaque classe qui affiche les infos spécifiques.
#5. Créer un objet VoitureElectrique et afficher toutes les infos.
#-----------------------------------------------------------------------------------
class Vehicule:
    def __init__(self,marque):
        self.marque = marque

    def infos(self):
        for k,v in self.__dict__.items():
            print(f'{k} : {v}')

class Voiture(Vehicule):
    def __init__(self,marque,nb_portes):
        super().__init__(marque)
        self.nb_portes = nb_portes


class VoitureElectrique(Voiture):
    def __init__(self,marque,nb_portes,autonomie):
        super().__init__(marque,nb_portes)
        self.autonomie = autonomie

v = Vehicule('Renault')
v.infos()

v2 = Voiture('Dacia',4)
v2.infos()

ve = VoitureElectrique('Toyota',2,120)
ve.infos()
