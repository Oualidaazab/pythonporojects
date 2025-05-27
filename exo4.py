class Personne:                                 # this project use opp inheritance 
    def __init__(self,nom,age):
        self.nom = nom
        self.age =age

    def __str__(self):
        return f'Nom : {self.nom}\nAge : {self.age}'

class Employe(Personne):
    def __init__(self,nom,age,salaire):
        super().__init__(nom,age)
        self.salaire = salaire

    def __str__(self):
        return super().__str__()+f'\nSalaire : {self.salaire}'

class Manager(Employe):
    def __init__(self,nom,age,salaire,equipe):
        super().__init__(nom,age,salaire)
        self.equipe = equipe

    def __str__(self):
        return super().__str__()+f'\nEquipes : {self.equipe}'

p = Personne('Ahmed',24)
print(p)

e = Employe('Rachid',32,3500)
print(e)

m = Manager('Fatima',45,7500,[e])
print(m)
