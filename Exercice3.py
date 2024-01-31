# Définir les constantes pour les caractères minuscules, majuscules, chiffres et spéciaux
MINUSCULES = "abcdefghijklmnopqrstuvwxyz"
MAJUSCULES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHIFFRES = "0123456789"
SPECIAUX = "!@#$%^&*()-_+=[]{};:,.<>/?\\|`~"

# Définir la fonction qui teste la validité du mot de passe
def mot_de_passe_valide(mot_de_passe):
    # Initialiser les variables pour compter le nombre de caractères de chaque catégorie
    nb_minuscules = 0
    nb_majuscules = 0
    nb_chiffres = 0
    nb_speciaux = 0
    
    # Parcourir le mot de passe caractère par caractère
    for caractere in mot_de_passe:
        # Si le caractère est une lettre minuscule, incrémenter le compteur correspondant
        if caractere in MINUSCULES:
            nb_minuscules += 1
        # Si le caractère est une lettre majuscule, incrémenter le compteur correspondant
        elif caractere in MAJUSCULES:
            nb_majuscules += 1
        # Si le caractère est un chiffre, incrémenter le compteur correspondant
        elif caractere in CHIFFRES:
            nb_chiffres += 1
        # Si le caractère est un caractère spécial, incrémenter le compteur correspondant
        elif caractere in SPECIAUX:
            nb_speciaux += 1
        # Sinon, le caractère n'est pas valide, renvoyer False
        else:
            return False
    
    # Vérifier si le mot de passe respecte les conditions de validité
    # Le mot de passe doit avoir au moins 8 caractères
    # Le mot de passe doit avoir au moins un caractère de chaque catégorie
    if len(mot_de_passe) >= 8 and nb_minuscules > 0 and nb_majuscules > 0 and nb_chiffres > 0 and nb_speciaux > 0:
        # Le mot de passe est valide, renvoyer True
        return True
    else:
        # Le mot de passe n'est pas valide, renvoyer False
        return False


# Écriture d'un programme qui permet de tester la fonction précédente
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
    # Définir quelques mots de passe de test
    mdp1 = "azerty"
    mdp2 = "Azerty123"
    mdp3 = "Azerty@123"
    mdp4 = "Azerty@123!"
    
    # Afficher les mots de passe de test
    print("\nLes mots de passe de test sont :")
    print(mdp1)
    print(mdp2)
    print(mdp3)
    print(mdp4)
    
    # Tester la validité des mots de passe de test en utilisant la fonction mot_de_passe_valide
    print("\nLa validité des mots de passe de test est :")
    print(mot_de_passe_valide(mdp1))
    print(mot_de_passe_valide(mdp2))
    print(mot_de_passe_valide(mdp3))
    print(mot_de_passe_valide(mdp4))
    
    # Afficher un message de succès
    print("Le code a été exécuté avec succès !\n")
    
    # Afficher à nouveau le menu principal
    menu_principal()

# Définir la fonction menu_interactif()
def menu_interactif():
    # Demander à l'utilisateur d'entrer un mot de passe
    mot_de_passe = input("\nEntrez un mot de passe : ")
    
    # Tester la validité du mot de passe en utilisant la fonction mot_de_passe_valide
    if mot_de_passe_valide(mot_de_passe):
        # Afficher un message positif si le mot de passe est valide
        print("Votre mot de passe est valide.\n")
    else:
        # Afficher un message négatif si le mot de passe n'est pas valide
        print("Votre mot de passe n'est pas valide.\n")
    
    # Afficher à nouveau le menu principal
    menu_principal()

menu_principal()