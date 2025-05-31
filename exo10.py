class Musicien:
    def performer(self):
        return 'je joue de la musique'

class Danseur:
    def performer(self):
        return 'je danse !'

class ArtisteComplet(Musicien,Danseur):
    def performer(self):
        return 'Je danse et je joue de la musique'

artistes = [Musicien(),Danseur(),ArtisteComplet()]

for a in artistes:
    print(a.performer())