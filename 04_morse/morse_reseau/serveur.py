# coding: utf-8 
import network
import comMorse
import ledArduino


ADDRESS=""
PORT=1111

sock=network.newServerSocket()
sock.bind((ADDRESS,PORT))


def communication(thread):
    
    message = thread.clientsocket.recv(4096)
    message = message.decode("utf-8")

    print("message de %s %s" % (thread.ip, thread.port, ))
    print(">>", message)
    message= comMorse.decodeMorse(message)
    print(">>", message)
    
    #eledArduino.nvoiCaractere(message[0])
    ledArduino.envoiPhrase(message)
    
    thread.clientsocket.send("serveur : j'ai bien recu le message".encode())
    
    if message=="exit":
        return False
    else:
        return True



continuer = True
while continuer:

    sock.listen(10)
    print( "En ecoute...")

    thread = network.newThread(sock.accept())
    thread.start()

    continuer=communication(thread)


    