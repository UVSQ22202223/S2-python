import tkinter as tk
import random

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin") # ajoute un titre
def cercle():
    x=random.randint(0,400)
    y=random.randint(0,500)
    canvas.create_oval(x,y,x+50,y+50)

canvas = tk.Canvas(racine,bg="red", height=500, width=500)
canvas.grid(column=1, row=1,columnspan=3,rowspan=3)

couleur = tk.Button(racine, text='choisir une couleur', command=None)
couleur.grid(column=2, row=0)

cercle = tk.Button(racine, text='Cercle', command=cercle())
cercle.grid(column=0, row=1)

carre = tk.Button(racine, text='Carré', command=None)
carre.grid(column=0, row=2)

croix = tk.Button(racine, text='Croix', command=None)
croix.grid(column=0, row=3)


racine.mainloop() # Lancement de la boucle principal