"""
Programme Snake version 1

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 

def computeNextFrame(numFrame):
    print(numFrame)
    numFrame = numFrame + 1
    can.delete("all")
    tk.after(100, lambda:compute(NextFrame))
    
can.pack()
computeNextFrame(0)
# On crée un environnement Tkinter
tk = Tk()
   
# On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
# Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
# intégré (ici l'environnement Tkinter)
# Les trois autres paramètres permettent de spécifier la taille et la couleur
# de fond du canevas
can = Canvas(tk, width=500, height=500, bg='black')

# On affiche le canevas
can.pack()

# lancement de la boucle principale qui écoute les évènements (claviers...)
tk.mainloop() # Cet appel doit être la derniere instruction du programme




