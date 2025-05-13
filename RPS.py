import random 
list=["rock","scissor","paper"] 
chance =3
score=0
randomvalue=random.choice(list) 
print("YOU HAVE JUST 3 CHANCES")
while chance>0 :
       userinput=str(input("enter you :")).lower()
       if userinput==randomvalue: 
           print("nothing try again") 
           chance-=1
       elif randomvalue==list[0] and userinput=="scissor" :  
           chance-=1
           print(f"YOU LOST you have {chance}")
       elif   randomvalue==list[0] and userinput=="paper" : 
               print(f"you win you have {chance}")
               score+=1      
               chance-=1      
       elif randomvalue==list[1] and userinput=="paper" :
           chance-=1
           print(f"you win you have {chance}") 
           score+=1
       elif  randomvalue==list[1] and userinput=="rock" :
           print(f"you win you have this {chance} chance  ") 
           score+=1 
           chance-=1
       elif randomvalue==list[2] and userinput=="rock" :
           print(f"you win you have this {chance} ") 
           score+=1 
           chance-=1 
       elif randomvalue==list[2] and userinput=="scissor" :
           print(f"you win you have this {chance} ")
           score+=1  
           chance-=1
       elif score==3 :
           print("congratulation you win")  
       elif  userinput not in  list : 
           print("invalid input try againe ") 
    
           
           