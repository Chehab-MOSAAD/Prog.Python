# Importer le module sys pour gérer les erreurs
import sys

# Implémentation de la structure de données « Pile »
class Pile:
    # Initialiser la pile avec une liste vide
    def __init__(self):
        self.liste = []
    
    # Empiler un élément à la fin de la liste
    def empiler(self, element):
        self.liste.append(element)
    
    # Dépiler un élément en le retirant de la fin de la liste
    def depiler(self):
        # Si la pile est vide, lever une exception
        if self.est_vide():
          raise IndexError("La pile est vide")
        # Sinon, renvoyer le dernier élément de la liste et le supprimer
        else:
          return self.liste.pop()
    
    # Renvoyer l'élément au sommet de la pile sans le dépiler
    def sommet(self):
        # Si la pile est vide, lever une exception
        if self.est_vide():
            raise IndexError("La pile est vide")
        # Sinon, renvoyer le dernier élément de la liste et le supprimer
        else:
            return self.liste[-1]
      
    # Vérifier si la pile est vide
    def est_vide(self):
        # Renvoyer True si la liste est vide, False sinon
        return len(self.liste) == 0

# Écriture d'une fonction qui convertit un nombre décimal en sa représentation binaire en utilisant une pile
def decimal_binaire(decimal):
    if decimal ==0:
        return "0"
    # Créer une pile vide
    pile = Pile()
    
    # Tant que le nombre décimal n'est pas nul :
    while decimal > 0:
        # Calculer le reste de la division par 2
        reste = decimal % 2
        # Empiler le reste dans la pile
        pile.empiler(reste)
        # Diviser le nombre décimal par 2
        decimal = decimal // 2
        
    # Initialiser une chaîne vide pour stocker le résultat
    binaire = ""
    
    # Tant que la pile n'est pas vide :
    while not pile.est_vide():
        # Dépiler un élément de la pile et le concaténer à la chaîne
        binaire = binaire + str(pile.depiler())
        
    # Renvoyer la chaîne binaire
    return binaire


# Écriture un programme qui permet de tester la fonction précédente
# Définir le menu principal
def menu_principal():
    # Afficher les options du menu
    print("1) Faire un test rapide et exécuter le code que j'ai écrit pour tester vos fonctions.")
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
    # Tester la classe Pile avec quelques opérations
    print("Nous testons la classe Pile :\n")
    # Créer une pile vide
    pile = Pile()
    
    # Vérifier que la pile est vide
    assert pile.est_vide(), "La pile devrait être vide"
    print("La pile est vide :",pile.est_vide()) 
    
    # Empiler quelques éléments
    pile.empiler(1)
    print("Élément '1' empilé")
    pile.empiler(2)
    print("Élément '2' empilé")
    pile.empiler(3)
    print("Élément '3' empilé")
    
    # Vérifier que la pile n'est pas vide
    assert not pile.est_vide(), "La pile ne devrait pas être vide"
    print("La pile est vide :",pile.est_vide()) 
    
    # Vérifier que le sommet de la pile est 3
    assert pile.sommet() == 3, "Le sommet de la pile devrait être 3"
    print("Le sommet de la pile est :",pile.sommet())
    
     # Dépiler un élément et vérifier qu'il est 3
    depile_1 = pile.depiler()
    assert depile_1 == 3, "L'élément dépilé devrait être 3"
    print("Élément dépilé :", depile_1)

    # Dépiler un élément et vérifier qu'il est 2
    depile_2 = pile.depiler()
    assert depile_2 == 2, "L'élément dépilé devrait être 2"
    print("Élément dépilé :", depile_2)

    # Dépiler un élément et vérifier qu'il est 1
    depile_3 = pile.depiler()
    assert depile_3 == 1, "L'élément dépilé devrait être 1"
    print("Élément dépilé :", depile_3)

    # Vérifier que la pile est vide
    assert pile.est_vide(), "La pile devrait être vide"
    print("La pile est vide :",pile.est_vide())  

    # Essayer de dépiler un élément et vérifier qu'une exception est levée
    try:
        pile.depiler()
        assert False, "Une exception devrait être levée"
    except IndexError as e:
        assert str(e) == "La pile est vide", "Le message d'erreur devrait être 'La pile est vide'"
    
    # Afficher un message de succès
    print("\nLa classe Pile a été testée avec succès.\n")
    
    # Tester la fonction decimal_binaire avec quelques nombres décimaux
    print("Nous testons la fonction decimal_binaire :\n")
    # Le résultat attendu pour 0 est "0"
    resultat = decimal_binaire(0)
    assert resultat == "0", "Le résultat est incorrect"
    print("Le résultat pour 0 est :", resultat)
    
    # Le résultat attendu pour 1 est "1"
    resultat = decimal_binaire(1)
    assert resultat == "1", "Le résultat est incorrect"
    print("Le résultat pour 1 est :", resultat)

    # Le résultat attendu pour 2 est "10"
    resultat = decimal_binaire(2)
    assert resultat == "10", "Le résultat est incorrect"
    print("Le résultat pour 2 est :", resultat)
    
    # Le résultat attendu pour 10 est "1010"
    resultat = decimal_binaire(10)
    assert resultat == "1010", "Le résultat est incorrect"
    print("Le résultat pour 10 est :", resultat)
    
    # Le résultat attendu pour 42 est "101010"
    resultat = decimal_binaire(42)
    assert resultat == "101010", "Le résultat est incorrect"
    print("Le résultat pour 42 est :", resultat)
    
    # Afficher un message de succès
    print("La fonction decimal_binaire a été testée avec succès.\n")
    
    # Afficher à nouveau le menu principal
    menu_principal()

# Créer une pile vide
pile = Pile()

# Définir le menu interactif
def menu_interactif():
    global pile  #Déclaration de la pile en tant que variable globale
    
    # Afficher les options du menu
    print("\n1) Créer une pile vide")
    print("2) Empiler un élément dans la pile")
    print("3) Dépiler un élément de la pile")
    print("4) Afficher le sommet de la pile")
    print("5) Vérifier si la pile est vide")
    print("6) Convertir un nombre décimal en binaire")
    print("7) Revenir au menu principal")
    
    # Demander à l'utilisateur de choisir une option
    choix = input("Entrez le numéro de l'option que vous souhaitez choisir : \n")
    
    # Si l'utilisateur choisit l'option 1
    if choix == "1":
        # Créer une pile vide
        pile = Pile()
        # Afficher un message de confirmation
        print("Vous avez créé une pile vide.\n")
        
        # Afficher à nouveau le menu interactif
        menu_interactif()
    
    # Sinon, si l'utilisateur choisit l'option 2
    elif choix == "2":
        # Demander à l'utilisateur d'entrer un élément à empiler
        element = input("Entrez l'élément à empiler : ")
        # Empiler l'élément dans la pile
        pile.empiler(element)
        # Afficher un message de confirmation
        print("Vous avez empilé l'élément", element, "dans la pile.\n")
        
        # Afficher à nouveau le menu interactif
        menu_interactif()
    
    # Sinon, si l'utilisateur choisit l'option 3
    elif choix == "3":
        # Essayer de dépiler un élément de la pile
        try:
            # Dépiler un élément de la pile
            element = pile.depiler()
            # Afficher un message de confirmation
            print("Vous avez dépilé l'élément", element, "de la pile.\n")
        # Si une exception est levée
        except IndexError as e:
            # Afficher le message d'erreur
            print(e)
        
        # Afficher à nouveau le menu interactif
        menu_interactif()
    
    # Sinon, si l'utilisateur choisit l'option 4
    elif choix == "4":
        # Essayer d'afficher le sommet de la pile
        try:
            # Afficher le sommet de la pile
            print("Le sommet de la pile est", pile.sommet(), "\n")
        # Si une exception est levée
        except IndexError as e:
            # Afficher le message d'erreur
            print(e)
        
        # Afficher à nouveau le menu interactif
        menu_interactif()
    
    # Sinon, si l'utilisateur choisit l'option 5
    elif choix == "5":
        # Vérifier si la pile est vide
        vide = pile.est_vide()
        # Si la pile est vide
        if vide:
            # Afficher un message de confirmation
            print("La pile est vide.\n")
        # Sinon
        else:
            # Afficher un message de confirmation
            print("La pile n'est pas vide.\n")
        
        # Afficher à nouveau le menu interactif
        menu_interactif()
    
    # Sinon, si l'utilisateur choisit l'option 6
    elif choix == "6":
        # Demander à l'utilisateur de saisir un nombre décimal
        while True:
            decimal = input("Entrez un nombre décimal : ")
            # Essayer de convertir le nombre décimal en un entier
            try:
                decimal = int(decimal)
                break  # Sortir de la boucle si la conversion est réussie
            # Si une erreur se produit, afficher un message d'erreur et redemander le nombre
            except ValueError:
                print("Vous devez entrer un nombre décimal valide.")
        
        # Si le nombre décimal est nul, renvoyer 0
        if decimal == 0:
            print("Le nombre binaire correspondant est 0.")
        # Sinon, appeler la fonction decimal_binaire et afficher le résultat
        else:
            binaire = decimal_binaire(decimal)
            # Afficher le résultat
            print("Le nombre ", decimal," en binaire est ", binaire, "\n")
        
        # Afficher à nouveau le menu interactif
        menu_interactif()
    
    # Sinon, si l'utilisateur choisit l'option 7
    elif choix == "7":
        # Afficher un message de remerciement
        print("Merci d'avoir utilisé ce programme. Au revoir !\n")
        # Afficher à nouveau le menu principal
        menu_principal()
    
    # Sinon, si l'utilisateur choisit une option invalide
    else:
        # Afficher un message d'erreur
        print("Option invalide, veuillez réessayer.\n")
        # Afficher à nouveau le menu interactif
        menu_interactif()

menu_principal()