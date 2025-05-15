print("Hello ...............................................................")

Gradebook = {}

student_name = input("Entrez le nom de l'élève : ")


control_number = int(input("Entrez le nombre de contrôles : "))


i = 0
notes = []
while i < control_number:
    i += 1
    note = int(input(f"Entrez la note {i} : "))
    notes.append(note)

# Store student and their notes
Gradebook[student_name] = notes
print(Gradebook)

# Function to search for a student
def list_eleve(name):
    if name not in Gradebook:
        print(f"L'élève {name} n'est pas dans la base de données. Veuillez réessayer !!")
    else:
        print(f"L'élève {name} est déjà dans la liste.")

# Function to delete a student
def delete_eleve(name):
    if name in Gradebook:
        del Gradebook[name]
        print(f"L'élève {name} a été supprimé.")
    else:
        print(f"L'élève {name} n'est pas dans la liste.")

# Function to calculate average
def moyenne(name):
    if name in Gradebook:
        notes = Gradebook.get(name)
        avg = sum(notes) / len(notes)
        print(f"La moyenne de l'élève {name} est : {avg:.2f} / 20")
    else:
        print(f"L'élève {name} n'est pas dans la base de données.")

# Menu
user_input = int(input(
    "\nMenu ..........................................................\n"
    "1 : Chercher un élève\n"
    "2 : Supprimer un élève\n"
    "3 : Calculer la moyenne\n"
    "Entrez votre choix : "
))

if user_input == 1:
    name_input = input("Entrez le nom de l'élève : ")
    list_eleve(name_input)
elif user_input == 2:
    name_input = input("Entrez le nom de l'élève : ")
    delete_eleve(name_input)
elif user_input == 3:
    name_input = input("Entrez le nom de l'élève : ")
    moyenne(name_input)
else:
    print("Choix invalide.")
print("Hello ...............................................................")

# Initialize an empty grade book
Gradebook = {}

# Get student name
student_name = input("Entrez le nom de l'élève : ")

# Get number of controls
control_number = int(input("Entrez le nombre de contrôles : "))

# Collect grades
i = 0
notes = []
while i < control_number:
    i += 1
    note = int(input(f"Entrez la note {i} : "))
    notes.append(note)

# Store student and their notes
Gradebook[student_name] = notes
print(Gradebook)

# Function to search for a student
def list_eleve(name):
    if name not in Gradebook:
        print(f"L'élève {name} n'est pas dans la base de données. Veuillez réessayer !!")
    else:
        print(f"L'élève {name} est déjà dans la liste.")

# Function to delete a student
def delete_eleve(name):
    if name in Gradebook:
        del Gradebook[name]
        print(f"L'élève {name} a été supprimé.")
    else:
        print(f"L'élève {name} n'est pas dans la liste.")

# Function to calculate average
def moyenne(name):
    if name in Gradebook:
        notes = Gradebook.get(name)
        avg = sum(notes) / len(notes)
        print(f"La moyenne de l'élève {name} est : {avg:.2f} / 20")
    else:
        print(f"L'élève {name} n'est pas dans la base de données.")

# Menu
user_input = int(input(
    "\nMenu ..........................................................\n"
    "1 : Chercher un élève\n"
    "2 : Supprimer un élève\n"
    "3 : Calculer la moyenne\n"
    "Entrez votre choix : "
))

if user_input == 1:
    name_input = input("Entrez le nom de l'élève : ")
    list_eleve(name_input)
elif user_input == 2:
    name_input = input("Entrez le nom de l'élève : ")
    delete_eleve(name_input)
elif user_input == 3:
    name_input = input("Entrez le nom de l'élève : ")
    moyenne(name_input)
else:
    print("Choix invalide.")
