print("hello ...............................................................") 
Gradbook={}
studentname=str(input("enter le nom de eleve  : ")) 
controlnumber=int(input("enter combien des controle : ")) 
i =0 
notes=[]
while i<controlnumber :
     i+=1 
     note=int(input(f"enter le note {i} :"))  
     notes.append(note) 
Gradbook[studentname] =notes 
print(Gradbook) 
def listeleve(n) : 
     if n not in  Gradbook.keys() : 
          print(f"this student {n} not in databases please try again !!")
     for  item  in Gradbook.keys():
          if item == n: 
               print(f"l'evel et deja dans la list : ") 
    
def delelteleve(x) :  
     if x in Gradbook : 
          del Gradbook[x]  
          print(f'leleve {x} a etait suprime ')  
     elif x  not in Gradbook :  
          print(f"l'eleve ne pad dans la list :")  
def  moyen(s) : 
     v=Gradbook.get(s) 
     moyen = sum(v)/controlnumber  
     print(f"le moyen de eleve {s} est : {moyen } /20 ")

userinput=int(input("Menu .......................................................... \n 1 : chercher un eleve enter  : \n 2 :suprime une eleve \n 3 :pour avoir le moyen :\n enter votre choix ")) 
if userinput == 1  : 
     nameuser=str(input("Entre le nom de elve  : ")) 
     listeleve(nameuser)    
elif userinput  ==  2 : 
     nameuser2=str(input("Entre le nom de eleve : ")) 
     delelteleve(nameuser2)   
elif userinput == 3 : 
     nameuser3 =str(input("Entre le nome de eleve  : "))
     moyen(nameuser3) 
 
    
     
     

     






