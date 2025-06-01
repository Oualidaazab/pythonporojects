f = open('journal.txt','rt')
error_dict = {}
i = 0
for line in f:
    if '[ERROR]' in line:
        i += 1
        error_dict[f'Erreur {i}'] = line
print(error_dict)
f.close()

o = open('erreurs.txt','wt')
for k,v in error_dict.items():
    o.write(f'{k}:{v}')
o.close()
o = open('erreurs.txt','rt')
txt = o.read()
print(txt)