# Liste des mots du pendu
liste_mots = [
    "armoire",
    "boucle",
    "buisson",
    "bureau",
    "chaise",
    "carton",
    "couteau",
    "fichier",
    "garage",
    "glace",
    "journal",
    "kiwi",
    "lampe",
    "liste",
    "montagne",
    "remise",
    "sandale",
    "taxi",
    "vampire",
    "volant",
]

chances = {  8:["____ ",
                "|/",
                "|",
                "|",
                "|",
                "|____"],
             7:["____ ",
                "|/ |",
                "|",
                "|",
                "|",
                "|____"],
             6:["____ ",
                "|/",
                "|",
                "|",
                "|",
                "|____"],
             5:["____ ",
                "|/",
                "|",
                "|",
                "|",
                "|____"],
             4:["____ ",
                "|/",
                "|",
                "|",
                "|",
                "|____"],
             3:["____ ",
                "|/",
                "|",
                "|",
                "|",
                "|____"],
             2:["____ ",
                "|/",
                "|",
                "|",
                "|",
                "|____"],
             1:["____ ",
                "|/",
                "|",
                "|",
                "|",
                "|____"],
             0:["____ ",
                "|/ | ",
                "| \\o/",
                "|  | ",
                "| / \\",
                "|____"]
}


def pendu(chance=0):
    for ligne in chances[chance]:
        print(ligne)

def masque(mot_a_trouver,lettres_trouvees):
    mot_masque = ""
    for lettre in mot_a_trouver:

        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"

    return mot_masque