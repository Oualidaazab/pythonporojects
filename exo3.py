class BankAcount:
    def __init__(self,titulaire,solde = 0):
        self.__titulaire = titulaire
        self.__solde = solde

    def deposer(self,montant):
        self.__solde += montant

    def retirer(self,montant):
        if self.__solde >= montant:
            self.__solde -= montant
        else:
            print('Solde Insuffisant !')

    def afficher_solde(self):
        return self.__solde

    def __str__(self):
        return f'Titulaire : {self.__titulaire}\nSolde : {self.__solde}'


comptes = [BankAcount('Mr Alami'),BankAcount'Mme Rachidi',3000)]

for cp in comptes:
    cp.deposer(1000)
    cp.retirer(2000)
    print(cp.afficher_solde())
    print(cp)
