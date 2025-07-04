class Vehicule : 
    def __init__(self,marque):
        self.marque=marque 
    def infos(self) :
        return f'le marque {self.marque}'
class voiture(Vehicule) :
    def __init__(self, marque,nb_portes):
        super().__init__(marque)         
        self.nb_portes =nb_portes 
    def infos(self):
        return super().infos()+f'les nomber des port sont {self.nb_portes}' 
class VoitureElectrique (voiture) : 
    def __init__(self, marque, nb_portes,autonomie):
        super().__init__(marque, nb_portes) 
        self.autonomie = int(autonomie) 
    def infos(self):
        return super().infos()+f'le autonomier sont {self.autonomie}' 
V=VoitureElectrique("BMW","22",100)
print(V.infos()) 
 

    