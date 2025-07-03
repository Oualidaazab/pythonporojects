# ========================== INHERETANCE ============================ 
class Personne : 
    def __init__(self,nom,age):
         self.nom =nom 
         self.age= int(age) 
    def __str__(self):
         return f'name is {self.nom} and his age is {self.age}'  
class Employ (Personne ) : 
     def __init__(self, nom, age,salaire):
          super().__init__(nom, age) 
          self.salaire =salaire  
     def __str__(self):
          return super().__str__() 
class Manager (Employ) : 
     def __init__(self, nom, age, salaire,equipe):
          super().__init__(nom, age, salaire) 
          self.equipe=equipe
     def __str__(self):
          return super().__str__() 
Personne1=Personne("oualid ",20) 
Employ1=Employ("AAZAB",20,200000000) 
Manager1=Manager("AAZAB",29,2,22) 

print(Personne1) 
