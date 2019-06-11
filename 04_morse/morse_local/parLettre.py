# coding: utf-8
import ledArduino
import dicoMatrice2D
import comMorse

print("tape une lettre")
lettre = input()
reponseMorse = comMorse.encode(lettre)
print("le code morse est :",reponseMorse)

reponse = comMorse.decode(reponseMorse)
ledArduino.envoiCaractere(reponse)