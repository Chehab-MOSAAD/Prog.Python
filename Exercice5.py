# Importer les modules os et datetime
import os
import datetime

# Créer une fonction pour vérifier si un répertoire existe
def repertoire_existe(repertoire):
    # Si le répertoire est vide, renvoyer False
    if not repertoire:
        return False
    # Sinon, essayer de convertir le répertoire en un chemin absolu
    try:
        repertoire = os.path.abspath(repertoire)
    # Si une erreur se produit, renvoyer False
    except OSError:
        return False
    # Sinon, vérifier si le répertoire est un dossier valide
    return os.path.isdir(repertoire)

# Créer une fonction pour vérifier si une date est valide
def date_valide(date):
    # Si la date est vide, renvoyer False
    if not date:
        return False
    # Sinon, essayer de convertir la date en un objet datetime
    try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
    # Si une erreur se produit, renvoyer False
    except ValueError:
        return False
    # Sinon, renvoyer True
    # Vérifier si la date limite est dans le futur
    if date_future(date):
        # Afficher un message indiquant qu'il n'y a pas de fichiers créés après cette date
        print("Il n'y a pas de fichiers créés après le", date.strftime("%d/%m/%Y"), "parce que cette date n'est pas encore arrivée.")
        # Demander à l'utilisateur si c'était une faute de frappe
        reponse = input("Est-ce que c'était une faute de frappe ? (O/N) : ")
        # Si la réponse est oui, recommencer le programme
        if reponse.upper() == "O":
           #print("Veuillez relancer le programme et entrer une nouvelle date.")
            return False
        # Sinon, terminer le programme
        else:
            #print("Le programme est terminé.")
            return True
    return True


# Créer une fonction pour vérifier si une date est dans le futur
def date_future(date):
    # Récupérer la date d'aujourd'hui
    aujourdhui = datetime.datetime.now()
    # Comparer la date avec la date d'aujourd'hui
    return date > aujourdhui

# Créer une boucle pour demander à l'utilisateur de saisir le nom du répertoire à explorer
while True:
    # Demander à l'utilisateur de saisir le nom du répertoire à explorer
    repertoire = input("Entrez le nom du répertoire à explorer : ")
    # Si le répertoire existe, sortir de la boucle
    if repertoire_existe(repertoire):
        break
    # Sinon, afficher un message d'erreur et recommencer
    else:
        print("Le répertoire que vous avez entré n'existe pas. Veuillez réessayer.")

# Créer une boucle pour demander à l'utilisateur de saisir la date limite au format jj/mm/aaaa
while True:
    # Demander à l'utilisateur de saisir la date limite au format jj/mm/aaaa
    date_limite = input("Entrez la date limite au format jj/mm/aaaa : ")
    # Si la date est valide, sortir de la boucle
    if date_valide(date_limite):
        break
    # Sinon, afficher un message d'erreur et recommencer
    else:
        print("La date que vous avez entrée n'est pas valide. Veuillez réessayer.")

# Convertir la date limite en un objet datetime
date_limite = datetime.datetime.strptime(date_limite, "%d/%m/%Y")
# Créer une liste vide pour stocker les fichiers qui répondent aux critères
fichiers = []
# Parcourir le répertoire et ses sous-répertoires
for chemin, sous_repertoires, noms_fichiers in os.walk(repertoire):
    # Pour chaque fichier rencontré
    for nom_fichier in noms_fichiers:
        # Récupérer le chemin complet du fichier
        chemin_fichier = os.path.join(chemin, nom_fichier)
        # Récupérer la date de création du fichier
        date_creation = os.path.getctime(chemin_fichier)
        # Convertir la date de création en un objet datetime
        date_creation = datetime.datetime.fromtimestamp(date_creation)
        # Si la date de création est supérieure à la date limite
        if date_creation > date_limite:
            # Ajouter le fichier à la liste des fichiers qui répondent aux critères
            fichiers.append(chemin_fichier)

# Sinon, vérifier si la liste des fichiers est vide
if not fichiers:
    # Afficher un message indiquant qu'il n'y a pas de fichiers créés après cette date
    print("Il n'y a pas de fichiers créés après le", date_limite.strftime("%d/%m/%Y"), ".")
    # Terminer le programme
    print("Le programme est terminé.")
# Sinon, afficher la liste des fichiers qui répondent aux critères
else:
    print("Les fichiers créés après le", date_limite.strftime("%d/%m/%Y"), "sont :\n")
    for fichier in fichiers:
        print(fichier)
    # Terminer le programme
    print("Le programme est terminé.")
