#***************************************************************************** #
#                          FROM HACKERRANK                                    |
# ****************************************************************************


class  Etudiant: 
    nombre_etudiants=0
    def __init__(self,nom, prenom ,niveau ):
         self.nom =nom 
         self.prenom = prenom 
         self.niveau =niveau 
         Etudiant.nombre_etudiants+=1 
    def afficher_infos(self) : 
         return f" le nom est {self.nom} , est le prenom {self.prenom} est le niveau {self.niveau}" 
Etudiant1=Etudiant("oualid","aazab","bac +1 ") 
Etudiant2=Etudiant("ali ","ait bn ali ","bac") 
print(Etudiant1.afficher_infos()) 
print(Etudiant.nombre_etudiants) 
 
