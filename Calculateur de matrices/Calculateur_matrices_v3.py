

from tkinter import *
from fonctionsMatrice import*



##################################################


def get_matrice(mat):
    matrice = []
    idx = 0

    for i in mat.get("1.0", END).splitlines():
        if i != '':
            matrice.append([])
            for j in i.split(","):
                if j.lstrip("-").isnumeric():
                    matrice[idx].append((int(j)))
            idx += 1
    return matrice


def get_texte(texteCombat):
    chat = []
    idx = 0
    for i in texteCombat.get("1.0", END).splitlines():
        chat.append([])
    return chat


def insertResultat(field, resultat):
    field.insert(END, resultat)


def resultat_addition():
    mat_1 = get_matrice(saisieMatrice1)
    mat_2 = get_matrice(saisieMatrice2)
    insertResultat(fenêtreResultat, additionMatrice(mat_1, mat_2))


def resultat_multiplication():
    mat_1 = get_matrice(saisieMatrice1)
    mat_2 = get_matrice(saisieMatrice2)
    insertResultat(fenêtreResultat, multiplicationMatrice(mat_1, mat_2))


def resultat_transposition():
    mat_1 = get_matrice(saisieMatrice1)
    mat_2 = get_matrice(saisieMatrice2)
    insertResultat(fenêtreResultat, transpositionMatrice(mat_1))


def resultat_déterminant():
    mat_1 = get_matrice(saisieMatrice1)
    mat_2 = get_matrice(saisieMatrice2)
    insertResultat(fenêtreResultat, determinantMatrice(mat_1))


def resultat_inversion():
    mat_1 = get_matrice(saisieMatrice1)
    mat_2 = get_matrice(saisieMatrice2)
    insertResultat(fenêtreResultat, InversionMatricede2(mat_1, mat_2))


##################################################



            ############# Création de la fenêtre principale (main window)

Mafenetre =  Tk ()   # On crée un objet tk
Mafenetre.geometry("1000x700")
Mafenetre.title('Calculateur de matrices')
Mafenetre.config(bg = "#ebdef0")
Mafenetre.resizable(False, False)



            ############ Création de trois fenêtres dans la fenêtre principale

fenêtre1 = Frame(Mafenetre, bg= "#0eecc0", width = 2000, height = 140, borderwidth=3, relief = "groove")
fenêtre1.pack(side=TOP, pady= 40)
fenêtre1.propagate(False)

fenêtre2 = Frame(Mafenetre, bg= "#0eecc0", width = 2000, height = 140, borderwidth=3, relief = "groove")
fenêtre2.pack(side=TOP, pady= 40)
fenêtre2.propagate(False)


fenêtre3 = Frame(Mafenetre, bg= "#0eecc0", width = 2000, height = 140, borderwidth=3, relief = "groove")
fenêtre3.pack(side=TOP, pady= 40)
fenêtre3.propagate(False)




            ########### Création des champs de saisies des matrices et de leurs labels dans la première fenêtre

saisieMatrice1 = Text(fenêtre1,width=10, height=5, font=("Helvetica", 16), borderwidth = 3, relief = "sunken")
saisieMatrice1.pack()
saisieMatrice1.place(x = 250, y = 3)
saisieMatrice1.propagate(False)

labelMatrice1 = Label(fenêtre1, text = "Matrice 1 : ", font = 10)
labelMatrice1.pack()
labelMatrice1.place(x = 80, y = 50)

#################################

saisieMatrice2 = Text(fenêtre1,width=10, height=5, font=("Helvetica", 16), borderwidth = 3, relief = "sunken")
saisieMatrice2.pack()
saisieMatrice2.place(x = 650, y = 3)
saisieMatrice2.propagate(False)

labelMatrice2 = Label(fenêtre1, text = "Matrice 2 : ", font = 10)
labelMatrice2.pack()
labelMatrice2.place(x = 480, y = 50)


# font = taille de la police d'écriture



            ########### Création des bouttons dans la 2ème fenêtre

addition = Button(fenêtre2, text="Addition", width =10, height = 2, bg =("#FFA533"), borderwidth=5, relief = "raised",
                    activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command=resultat_addition)
addition.pack(side = LEFT, padx = 40)


multiplication = Button(fenêtre2, text="Multiplication", width =10, height = 2, bg =("#FFA533"), borderwidth=5, relief = "raised",
                    activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command = resultat_multiplication)
multiplication.pack(side = LEFT, padx = 40)


transposition = Button(fenêtre2, text="Transposition", width =10, height = 2, bg =("#FFA533"), borderwidth=5, relief = "raised",
                    activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command = resultat_transposition)
transposition.pack(side = LEFT, padx = 40)


determinant = Button(fenêtre2, text="Déterminant", width =10, height = 2, bg =("#FFA533"), borderwidth=5, relief = "raised",
                    activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command = resultat_déterminant)
determinant.pack(side = LEFT, padx = 40)


inversion = Button(fenêtre2, text="Inversion", width =10, height = 2, bg =("#FFA533"), borderwidth=5, relief = "raised",
                    activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command = resultat_inversion)
inversion.pack(side = LEFT, padx = 40)


adjointe = Button(fenêtre2, text="Adjointe", width =10, height = 2, bg =("#FFA533"), borderwidth=5, relief = "raised",
                    activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff")
adjointe.pack(side = LEFT, padx = 40)


    # bg = backgroung
    # borderwidth = épaisseur des bordures
    # relief = pour donner le type de relief souhaité à un objet
    # activebackground = couleur de fond du bouton lorsque qu'il est pressé
    # activeforeground = couleur de texte du bouton lorque qu'il est pressé
    # foreground = couleur du texte du bouton



            ########### Fenêtre et label resultat dans la 3ème fenêtre


labelResultat = Label(fenêtre3, text = "Résultat : ", bg='white', font = 12)
labelResultat.pack()
labelResultat.place(x = 200, y = 60)


fenêtreResultat = Text(fenêtre3, width = 10, height = 5, bg='white', font=("Helvetica", 16), borderwidth = 2, relief = "solid")
fenêtreResultat.pack(side=LEFT, padx = 10)
fenêtreResultat.place(x = 450, y = 4)


Texte = StringVar()


    # on lance la boucle principale
Mafenetre.mainloop() # Elle permet de maintenir la fenêtre car la fenêtre continue de tourner
