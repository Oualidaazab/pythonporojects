#-------------------------------------------------------------------------------------- 
# this python project is can generat a password and save in "motdepasse.txt" file 
#-------------------------------------------------------------------------------------


import random
from string import ascii_lowercase,ascii_uppercase,digits,punctuation

text = ascii_lowercase+ascii_uppercase+digits+punctuation
password = ''
for i in range(12):
    password += random.choice(text)

o = open('motdepasse.txt','at')
o.write(password+'\n')

o.close()

if len(password) == 12:
    print('Success')
else:
    print('Fail ')
