class Livre:
    def __init__(self,titre,auteur,annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def afficher_details(self):
        return f'Titre : {self.titre}\nAuteur : {self.auteur}\nAnnee Publication : {self.annee_publication}'

l1 = Livre('mille et une nuit','auteur1',1110)
l2 = Livre('Harry potter','auteur2',2003)

for l in [l1,l2]:
    print(l.titre,l.auteur,l.annee_publication)
    print(l.afficher_details())