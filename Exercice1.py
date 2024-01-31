# Importer le module sys pour gérer les erreurs
import sys

def intersection_2_listes(L1, L2):
    # Initialiser d'une liste vide pour stocker le résultat et de deux indices i et j à 0
    resultat = []
    i = 0
    j = 0
    
    # Tant que i et j sont inférieurs aux longueurs de L1 et L2 respectivement :
    while i < len(L1) and j < len(L2):
        # Si L1[i] est égal à L2[j] :
        if L1[i] == L2[j]:
          # Ajouter L1[i] au résultat
          resultat.append(L1[i])
          # Incrémenter i et j
          i += 1
          j += 1
        # Sinon, si L1[i] est inférieur à L2[j] :
        elif L1[i] < L2[j]:
          # Incrémenter i
          i += 1
        # Sinon :
        else:
          # Incrémenter j
          j += 1
          
    # Renvoyer le résultat
    return resultat

def intersection(L):
    # Si L est vide, renvoyer une liste vide
    if not L:
        return []
    
    # Sinon, initialiser le résultat avec la première liste de L
    else:
        resultat = L[0]
        # Pour chaque liste de L à partir de la deuxième :
        for liste in L[1:]:
            # Calculer l'intersection entre le résultat et la liste courante en utilisant la fonction intersection_2_listes
            inter = intersection_2_listes(resultat, liste)
            # Affecter le résultat de l'intersection à la variable résultat
            resultat = inter
            
        # Renvoyer le résultat
        return resultat


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
    # Définir quelques listes de test
    L1 = [1, 2, 3, 4, 5]
    L2 = [3, 4, 5, 6, 7]
    L3 = [5, 6, 7, 8, 9]
    L4 = [1, 3, 5, 7, 9]
    L  = [L1, L2, L3, L4]
    
    # Afficher les listes de test
    print("\nLes listes de test sont :")
    for liste in L:
        print(liste)
    
    # Calculer et afficher l'intersection des listes de test
    inter = intersection(L)
    print("L'intersection des listes de test est :")
    print(inter)
    # Afficher un message de succès
    print("Le code a été exécuté avec succès !\n")
    
    # Afficher à nouveau le menu principal
    menu_principal()

# Définir la fonction menu_interactif()
def menu_interactif():
    # Demander à l'utilisateur de saisir le nombre de listes qu'il souhaite comparer
    while True:
        n = input("\nEntrez le nombre de listes que vous souhaitez comparer : ")
        try:
            n = int(n)
            break  # Si la conversion est réussie, sortir de la boucle
        except ValueError:
            print("Vous devez entrer un seul nombre entier. Veuillez réessayer.")

            
    # Initialiser une liste vide pour stocker les listes de l'utilisateur
    L = []
    
    # Pour chaque liste que l'utilisateur souhaite comparer
    for i in range(n):
        # Demander à l'utilisateur de saisir les éléments de la liste séparés par des espaces
        while True:
            try:
                liste = input(f"Entrez les éléments de la liste {i+1} séparés par des espaces : ")
                liste = [int(x) for x in liste.split()]
                break  # Si la conversion est réussie, sortir de la boucle
            except ValueError:
                print("Les éléments de la liste doivent être des chiffres. Veuillez réessayer.")

        # Trier la liste et l'ajouter la liste à la liste L
        liste.sort()
        L.append(liste)
    
    # Calculer et afficher l'intersection des listes de l'utilisateur
    inter = intersection(L)
    print("L'intersection des listes que vous avez saisies est :", inter, "\n")
    
    # Afficher à nouveau le menu principal
    menu_principal()

menu_principal()