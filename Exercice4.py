# Écriture d'une fonction qui permet de vérifier si un code HTML donné a des balises correctement équilibrées
def balises_equilibrees(html):
    # Créer une pile vide pour stocker les balises d'ouverture
    pile = []
    
    # Parcourir le code HTML caractère par caractère
    i = 0
    while i < len(html):
        # Si on rencontre le caractère '<', on commence une balise
        if html[i] == '<':
            # On avance jusqu'au caractère '>'
            i += 1
            # On récupère le nom de la balise entre les caractères '<' et '>'
            nom_balise = ""
            while i < len(html) and html[i] != '>':
                nom_balise += html[i]
                i += 1
            
            # Si on a bien trouvé le caractère '>', on traite la balise
            if i < len(html) and html[i] == '>':
                # Si la balise commence par '/', c'est une balise de fermeture
                if nom_balise.startswith('/'):
                    # On retire le '/' du nom de la balise
                    nom_balise = nom_balise[1:]
                    # Si la pile est vide, il y a une balise de fermeture sans balise d'ouverture correspondante, le code HTML n'est pas équilibré
                    if not pile:
                        return False
                    # Sinon, on dépile la dernière balise d'ouverture de la pile
                    else:
                        balise_ouverte = pile.pop()
                        # Si la balise de fermeture ne correspond pas à la balise d'ouverture, le code HTML n'est pas équilibré
                        if nom_balise != balise_ouverte:
                            return False
                
                # Sinon, si la balise ne se termine pas par '/', c'est une balise d'ouverture
                elif not nom_balise.endswith('/'):
                    # On empile la balise d'ouverture dans la pile
                    pile.append(nom_balise)
            
            # Sinon, c'est une balise auto-fermante, on ne fait rien
        # On avance au caractère suivant
        i += 1
    
    # À la fin du parcours, si la pile est vide, le code HTML est équilibré
    if not pile:
        return True
    # Sinon, il reste des balises d'ouverture sans balise de fermeture correspondante, le code HTML n'est pas équilibré
    else:
        return False

# Écriture d'une fonction qui lit un fichier HTML et retourne le nombre d’occurrences de chaque balise HTML présente dans le fichier
def compter_balises(fichier):
    # Ouvrir le fichier HTML en mode lecture
    with open(fichier, 'r') as f:
        
        # Lire le contenu du fichier
        html = f.read()
        
        # Créer un dictionnaire vide pour stocker le nombre d'occurrences de chaque balise
        occurrences = {}
        
        # Parcourir le code HTML caractère par caractère
        i = 0
        while i < len(html):
            # Si on rencontre le caractère '<', on commence une balise
            if html[i] == '<':
                # On avance jusqu'au caractère '>'
                i += 1
                # On récupère le nom de la balise entre les caractères '<' et '>'
                nom_balise = ""
                while i < len(html) and html[i] != '>':
                    nom_balise += html[i]
                    i += 1
                
                # Si on a bien trouvé le caractère '>', on traite la balise
                if i < len(html) and html[i] == '>':
                    # Si la balise commence par '/', c'est une balise de fermeture, on ne la compte pas
                    if nom_balise.startswith('/'):
                        pass
                    # Sinon, c'est une balise d'ouverture ou auto-fermante, on la compte
                    else:
                        # Si la balise se termine par '/', on retire le '/' du nom de la balise
                        if nom_balise.endswith('/'):
                            nom_balise = nom_balise[:-1]
                        # Si la balise existe déjà dans le dictionnaire, on incrémente son nombre d'occurrences
                        if nom_balise in occurrences:
                            occurrences[nom_balise] += 1
                        # Sinon, on crée une nouvelle entrée dans le dictionnaire avec le nombre d'occurrences à 1
                        else:
                            occurrences[nom_balise] = 1
            
            # On avance au caractère suivant
            i += 1
        
        # Renvoyer le dictionnaire des occurrences
        return occurrences


# Écriture d'un programme qui permet de tester les fonctions précédentes
# Définir le menu principal
def menu_principal():
    # Afficher les options du menu
    print("1) Faire un test rapide et exécuter le code.")
    print("2) Essayer le code vous-même et interagir avec le programme.")
    print("3) Quitter le programme.")
    
    # Demander à l'utilisateur de choisir une option
    choix = input("Entrez le numéro de l'option que vous souhaitez choisir : ")
    
    # Si l'utilisateur choisit l'option 1
    if choix == "1":
        # Exécuter le code que j'ai écrit pour tester les fonctions
        tester_fonctions()
    
    # Sinon, si l'utilisateur choisit l'option 2
    elif choix == "2":
        # Afficher le menu interactif
        menu_interactif()
    
    # Sinon, si l'utilisateur choisit l'option 3
    elif choix == "3":
        # Afficher un message de remerciement
        print("Merci d'avoir utilisé ce programme. Au revoir !")
    
    # Sinon, si l'utilisateur choisit une option invalide
    else:
        # Afficher un message d'erreur
        print("Option invalide, veuillez réessayer.\n")
        # Afficher à nouveau le menu principal
        menu_principal()
        
# Définir la fonction tester_fonctions()
def tester_fonctions():
    # Test de la fonction balises_equilibrees
    code_html_equilibre = "<html><head></head><body></body></html>"
    code_html_non_equilibre = "<html><head></body></html>"
    
    print("\nL'exemple de code de ce test est : ", code_html_equilibre)
    # Vérifier si le code HTML équilibré est bien reconnu par la fonction
    if balises_equilibrees(code_html_equilibre):
        print("Test balises_equilibrees réussi pour un code équilibré.")
    else:
        print("Test balises_equilibrees échoué pour un code équilibré.")
    
    print("\nL'exemple de code de ce test est :", code_html_non_equilibre)
    # Vérifier si le code HTML non équilibré est bien reconnu par la fonction
    if not balises_equilibrees(code_html_non_equilibre):
        print("Test balises_equilibrees réussi pour un code non équilibré.")
    else:
        print("Test balises_equilibrees échoué pour un code non équilibré.")

    # Test de la fonction compter_balises
    fichier_test = "test.html"
    # Créer un fichier HTML de test avec le code HTML équilibré
    with open(fichier_test, 'w') as f:
        f.write("<html><head></head><body></body></html>")
    
    print("\nL'exemple de fichier de ce test est :", fichier_test)
    # Compter les occurrences des balises dans le fichier de test
    resultats = compter_balises(fichier_test)
    # Vérifier si les résultats sont conformes aux attentes
    if resultats == {'html': 1, 'head': 1, 'body': 1}:
        print("les resultats sont : ", resultats)
        print("Test compter_balises réussi.\n")
    else:
        print("Test compter_balises échoué.\n")
    
    # Afficher à nouveau le menu principal
    menu_principal()

# Définir le menu interactif
def menu_interactif():
    # Afficher les options du menu interactif
    print("\nMenu interactif :")
    print("1) Vérifier l'équilibre des balises HTML")
    print("2) Compter les occurrences des balises dans un fichier HTML")
    print("3) Quitter le programme")
    
    # Demander à l'utilisateur de choisir une option
    choix_interactif = input("Entrez le numéro de l'option que vous souhaitez choisir : ")
    
    # Exécuter l'option choisie
    if choix_interactif == "1":
        # Demander à l'utilisateur d'entrer le code HTML à vérifier
        code_html = input("\nEntrez le code HTML à vérifier : ")
        # Appeler la fonction balises_equilibrees avec le code HTML entré
        if balises_equilibrees(code_html):
            # Afficher un message positif si le code est équilibré
            print("Le code HTML est équilibré.")
        else:
            # Afficher un message négatif si le code n'est pas équilibré
            print("Le code HTML n'est pas équilibré.")
        # Afficher à nouveau le menu interactif
        menu_interactif()
    
    elif choix_interactif == "2":
        while True:
        # Demander à l'utilisateur d'entrer le chemin du fichier HTML à analyser
            fichier_html = input("\nEntrez le chemin du fichier HTML : ")
            try:
                # Appeler la fonction compter_balises avec le chemin du fichier entré
                resultats = compter_balises(fichier_html)
                # Afficher les résultats sous forme de dictionnaire
                print("Occurrences des balises dans le fichier :", resultats)
                # Si tout s'est bien passé, sortir de la boucle
                break
            except FileNotFoundError:
                print(f"Le fichier '{fichier_html}' n'existe pas. Veuillez réessayer.")
            except Exception as e:
                print(f"Une erreur s'est produite : {e}. Veuillez réessayer.")

        menu_interactif()
    
    elif choix_interactif == "3":
        # Afficher un message de remerciement
        print("Merci d'avoir utilisé ce programme. Au revoir !\n")
        # Afficher à nouveau le menu principal
        #menu_principal()
        
    else:
        # Afficher un message d'erreur si l'option choisie n'est pas valide
        print("Option invalide, veuillez réessayer.\n")
        # Afficher à nouveau le menu interactif
        menu_interactif()

        
menu_principal()