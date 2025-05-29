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
