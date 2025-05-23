class Etudiant:
    nombre_etudiants = 0 # variable de classe
    def __init__(self,nom,prenom,niveau):
        self.nom = nom # variable d'instance
        self.prenom = prenom
        self.niveau = niveau
        Etudiant.nombre_etudiants += 1 #acces a la variable de classe et
        #l'incrementer a chaque creation d'objet

    def afficher_infos(self):
        print(f'Nom complet : {self.nom} {self.prenom}\nNiveau : {self.niveau}')

e1 = Etudiant('Alami','Ahmed','TS')
e2 = Etudiant('Rachidi','Fatima','T')

print(e1.nombre_etudiants,e2.nombre_etudiants)
print(e1.nom,e2.nom)

e1.afficher_infos()
e2.afficher_infos()
