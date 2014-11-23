# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 18:49:32 2014

@author: georgin
"""
import csv
from math import sqrt
from tkinter import *
import matplotlib.pyplot as plt 

fname = "Moyenne.csv"
file = open(fname, "r")
 
try:
    reader = csv.reader(file)

    liste = [row for row in reader]   
    
finally:
    #
    # Fermeture du fichier source
    #
    file.close()

def modif_liste(liste):
    """Recuperation d'un maximum de int dans un tableau """
    nombre_erreur = 0
    for i in range(len(liste)):
        for k in range(len(liste[i])):
            try:
                liste[i][k] = int(liste[i][k])
            except TypeError or ValueError or SyntaxError:
                nombre_erreur += 1
    return liste

def moyenne(lis):
    """Fait la moyenne de la liste"""
    lis = modif_liste(lis)
    somme_de_int = 0
    element_str = 0
    for element in lis:
        if type(element) == int:
            somme_de_int += element
        else:
            element_str += 1
    print(somme_de_int,element_str)
    try:
        a = somme_de_int/(len(lis)-element_str) #notre moyenne
    except ZeroDivisionError:
        print("La liste n'est pas valide")
    return a
        
        

def ecart_type(liste1):
    """Fait la moyenne de la liste"""
    liste1 = modif_lis(liste1)
    x_bar= moyenne(liste1)
    element_str = 0
    s = 0
    for element in liste1:
        if type(element) == type:
             s += (element - x_bar)**2
        else:
             element_str += 1
    try:
        ecart = s/(len(liste1)-element_str)
    except ZeroDivisionError:
        print("Erreur détecter")
    return ecart
             
    
#######################Programme Principale####################################   
Fenetre = Tk()

Fenetre.title('Moyenne')
Fenetre.geometry('300x100+400+400')

moyenne_label = Label(Fenetre, text="Votre moyenne de {} est de {}".format(liste[1][0],moyenne(liste[1])))
moyenne_label.pack()
moyenne_label = Label(Fenetre, text="Votre moyenne est de {}")
moyenne_label.pack()
ecart_type_label = Label(Fenetre, text="L'ecart type est de {}")
ecart_type_label.pack()
Buttom_quitter = Button(Fenetre, text="Quitter", command=Fenetre.destroy)
Buttom_quitter.pack()


Fenetre.mainloop()
