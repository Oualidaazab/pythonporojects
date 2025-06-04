from string import punctuation
f = open('texte.txt','rt')

txt = f.read()
f.close()
clean_txt = ''
for c in txt:
    if c not in punctuation:
        clean_txt += c

clean_txt = clean_txt.lower()
occurence_dict = {}

for word in clean_txt.split():
    if word not in occurence_dict.keys():
        i =1
    else:
        i += 1
    occurence_dict[word] = i

for k,v in occurence_dict.items():
    print(f'{k}:{v}')

