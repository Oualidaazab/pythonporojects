# =============================  ALL about oop ============================== 
# ============================= banc simulation ============================= 
class effectuer_paiment : 
    pass
class paiment_cart : 
    def afficher(self) : 
        return "Paiment par cart effectue " 
class Paimentpaypale : 
    def afficher(self):
        return  'Paiment par paypale  ' 
class Paimenrtcryptomonnaie : 
    def afficher(self ) : 
        return 'Paiment pat crypto ' 
list  = [paiment_cart,Paimentpaypale,Paimenrtcryptomonnaie] 
for  i  in  list : 
    print(i.afficher()) 
     
