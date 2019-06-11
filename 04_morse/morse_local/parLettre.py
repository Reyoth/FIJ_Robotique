# coding: utf-8
import ledArduino
import dicoMatrice2D
import comMorse

print("tape un code morse")
code = input()
reponse = comMorse.decode(code)
ledArduino.envoiCaractere(reponse)