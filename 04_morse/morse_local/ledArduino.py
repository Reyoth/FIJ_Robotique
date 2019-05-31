import i2cComm
import dicoMatrice2D
import time


def envoiCaractere(lettre):
    matrice = dicoMatrice2D.dico2D[lettre]
    for ligne in matrice:
        for led in ligne:
            i2cComm.writeNumber(led)


def envoiPhrase(phrase):
    for lettre in phrase:
        matrice = dicoMatrice2D.dico2D[lettre]
        for ligne in matrice:
            for led in ligne:
                i2cComm.writeNumber(led)
        time.sleep(1)

