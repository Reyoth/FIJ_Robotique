# Jeu du pendu
import random # on utilisera la fonction choice qui permet de choisir un element d'une liste
import libExo2

continuer_partie = 'o'

# on verifie a chaque tour si la personne veut continuer
while continuer_partie != 'n':

    # on prend un mots de la liste de maniere aleatoire
    mot_a_trouver = random.choice(libExo2.liste_mots)
    # on initialise nos variables
    lettres_trouvees= []
    mot_trouve = libExo2.masque(mot_a_trouver,lettres_trouvees)
    nb_chances = 8

    # on verifie a chaque tour si on a toujours pas trouve le nnombre
    # et si on a pas depasse le nombre de chance
    while mot_a_trouver != mot_trouve and nb_chances > 0 :
        libExo2.pendu(nb_chances)
        print("Mot à trouver", mot_trouve, "(encore", nb_chances, "chances)")

        lettre = input("Tapez une lettre: ")

        if lettre in lettres_trouvees: # La lettre a deja ete choisie
            print("Vous avez déjà choisi cette lettre.")
        elif lettre in mot_a_trouver: # La lettre est dans le mot a trouver
            lettres_trouvees.append(lettre)
            print("Bien joué.")
        else:
            nb_chances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot...")

        mot_trouve = libExo2.masque(mot_a_trouver,lettres_trouvees)


    # A-t-on trouve le mot ou nos chances sont-elles epuisees ?

    if mot_a_trouver == mot_trouve :
        print("Félicitations ! Vous avez trouvé le mot", mot_a_trouver)
    else:
        libExo2.pendu(nb_chances)
        print("PENDU !!! Vous avez perdu.")

    continuer_partie = input("Souhaitez-vous continuer la partie (o/n) ?")