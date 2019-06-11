# coding: utf-8

codesMorse =[
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
    "-----",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----."
]

lettres=[
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]

#encode
def encode(lettre="a"):
    position = lettres.index(lettre)
    return codesMorse[position]

#decode
def decode(morse=".-"):
    position = codesMorse.index(morse)
    return lettres[position]

#test
""" print("tape une lettre")
lettre = input()
reponse = encode(lettre)
print(reponse)

print("tape un code")
code = input()
print( decode(code) ) """


def encodeTexte(phrase):
    """Fonction prennant une phrase ou un mot et renvoyant son equivalent en morse
    sous forme de chaine de caractere.
    Pour faciliter la lecture, des espaces sont inserer entre les codes.
    Des / sont aussi inserer pour representer les espaces entre les mots"""
    
    reponse=""
    for lettre in phrase:
        if lettre != " " and lettre != "":
            reponse= reponse + encode(lettre)
            reponse= reponse + " "
        else:
            reponse= reponse + "/ "
    return reponse



def decodeMorse(morseBrut):
    """Fonction prennant une phrase ou un mot  en morse et renvoyant son equivalent texte
    sous forme de chaine de caractere."""
    
    reponse=""
    morseBrut = str.split(morseBrut," ")
    for element in morseBrut:
            if element != "/" and element != "":
                reponse= reponse + decode(element)
            elif element == "/":
                reponse= reponse + " "
            else:
                pass
    return reponse