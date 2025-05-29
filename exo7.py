#-------------------------------------------TASK-------------------------------------------------------|
#Objectif : Appliquer le polymorphisme via des méthodes redéfinies.                                    |
#Consignes :                                                                                           |
#1. Créer une classe Animal avec une méthode parler() qui retourne "Je suis un                         |
#animal".                                                                                              |
#. Créer trois classes dérivées :                                                                      |
#• Chien → "Wouf !"                                                                                    |
# Chat → "Miaou !"                                                                                     |
#• Oiseau → "Cui-cui !"                                                                                |
#3. Créer une fonction faire_parler(animal) qui prend un objet Animal en paramètre                     |
#et affiche le résultat de parler().                                                                   |
#4. Tester cette fonction avec des objets des trois classes.                                           |
#  From HackerRank                                                                                     |
#------------------------------------------------------------------------------------------------------|



class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Wouf !"

class Chat(Animal):
    def parler(self):
        return 'Miaou !'

class Oiseau(Animal):
    def parler(self):
        return 'Cui-cui !'

def faire_parler(a):
    print(a.parler())

animaux = [Chat(),Chien(),Oiseau()]

for a in animaux:
    faire_parler(a)
