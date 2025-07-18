
class Animal : 
    def __init__(self,cat): 
        self.cat=cat 
    def parler(self): 
        return "je suis un animal"  
class chien  : 
    def __init__(self,chiene):
        self.chiene=chien
    def parler(self): 
        return  'wouf'
class chat : 
    def __init__(self,chat):
        self.chat=chat 
    def parler(self) : 
        return  'Miaou ' 
class Oiseau : 
    def __init__(self,oiseau):
        self.oiseau=oiseau 
    def parler(self): 
        return 'CUI-CUI ' 
o1=Oiseau("oo") 
print(o1.parler()) 
chat1=chat("oo") 
print(chat1.parler()) 
 
