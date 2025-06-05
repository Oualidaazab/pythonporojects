class Contact:
    def __init__(self,nom,email,tel):
        self.nom = nom
        self.email = email
        self.tel = tel

f = open('contacts.txt','rt')
contacts = []
for line in f:
    liste = line.split(',')
    contact = Contact(liste[0],liste[1],liste[2])
    contacts.append(contact)

o = open('carnet_sauvegarde.txt','wt')
for contact in contacts:
    o.write(f'{contact.nom} - {contact.email} - {contact.tel}')
