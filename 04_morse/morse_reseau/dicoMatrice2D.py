# coding: utf-8

dico2D={  "a":[[0,1,1,1,0],
               [1,0,0,0,1],
               [1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1]],
          "b":[[1,1,1,1,0],
               [1,0,0,0,1],
               [1,1,1,1,0],
               [1,0,0,0,1],
               [1,1,1,1,0]],
          "c":[[0,1,1,1,0],
               [1,0,0,0,1],
               [1,0,0,0,0],
               [1,0,0,0,1],
               [0,1,1,1,0]],
          "d":[[1,1,1,1,0],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,0]],
          "e":[[1,1,1,1,1],
               [1,0,0,0,0],
               [1,1,1,1,1],
               [1,0,0,0,0],
               [1,1,1,1,1]],
          "f":[[1,1,1,1,1],
               [1,0,0,0,0],
               [1,1,1,1,0],
               [1,0,0,0,0],
               [1,0,0,0,0]],
          "g":[[0,1,1,1,1],
               [1,0,0,0,0],
               [1,0,0,1,1],
               [1,0,0,0,1],
               [0,1,1,1,0]],
          "h":[[1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1]],
          "i":[[0,1,1,1,0],
               [0,0,1,0,0],
               [0,0,1,0,0],
               [0,0,1,0,0],
               [0,1,1,1,0]],
          "j":[[1,1,1,1,1],
               [0,0,1,0,0],
               [0,0,1,0,0],
               [1,0,1,0,0],
               [1,1,1,0,0]],
          "k":[[1,0,0,0,1],
               [1,0,0,1,0],
               [1,1,1,0,0],
               [1,0,0,1,0],
               [1,0,0,0,1]],
          "l":[[1,0,0,0,0],
               [1,0,0,0,0],
               [1,0,0,0,0],
               [1,0,0,0,0],
               [1,1,1,1,1]],
          "m":[[1,0,0,0,1],
               [1,1,0,1,1],
               [1,0,1,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1]],
          "n":[[1,0,0,0,1],
               [1,1,0,0,1],
               [1,0,1,0,1],
               [1,0,0,1,1],
               [1,0,0,0,1]],
          "o":[[0,1,1,1,0],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [0,1,1,1,0]],
          "p":[[1,1,1,1,0],
               [1,0,0,0,1],
               [1,1,1,1,0],
               [1,0,0,0,0],
               [1,0,0,0,0]],
          "q":[[0,1,1,1,0],
               [1,0,0,0,1],
               [1,0,1,0,1],
               [1,0,0,1,0],
               [0,1,1,0,1]],
          "r":[[1,1,1,1,0],
               [1,0,0,0,1],
               [1,1,1,1,0],
               [1,0,0,1,0],
               [1,0,0,0,1]],
          "s":[[0,1,1,1,1],
               [1,0,0,0,0],
               [0,1,1,1,0],
               [0,0,0,0,1],
               [1,1,1,1,0]],
          "t":[[1,1,1,1,1],
               [0,0,1,0,0],
               [0,0,1,0,0],
               [0,0,1,0,0],
               [0,0,1,0,0]],
          "u":[[1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [0,1,1,1,0]],
          "v":[[1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,0,0,1],
               [0,1,0,1,0],
               [0,0,1,0,0]],
          "w":[[1,0,0,0,1],
               [1,0,0,0,1],
               [1,0,1,0,1],
               [1,0,1,0,1],
               [0,1,0,1,0]],
          "x":[[1,0,0,0,1],
               [0,1,0,1,0],
               [0,0,1,0,0],
               [0,1,0,1,0],
               [1,0,0,0,1]],
          "y":[[1,0,0,0,1],
               [0,1,0,1,0],
               [0,0,1,0,0],
               [0,0,1,0,0],
               [0,0,1,0,0]],
          "z":[[1,1,1,1,1],
               [0,0,0,1,0],
               [0,0,1,0,0],
               [0,1,0,0,0],
               [1,1,1,1,1]]}

def testMatrice2D(lettre="a"):
     i=0
     while i<5:
          ligne =""
          for led in dico2D[lettre][i]:
               ligne += str(led)
          ligne = ligne.replace("1","[*]")
          print(ligne.replace("0","[ ]"))
          i +=1

""" testMatrice2D() """