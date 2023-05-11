from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from io import StringIO
import sys
# from tkinter.ttk import*
from tkinter import ttk  
from RPG_Final_Copie_v2 import*
import pygame



        
############################################################################################################################################################# MES FONCTIONS
#### Fonction qui gère l'animation des fichiers gif

def animate_gif(filename, canvas):
    frames = []
    try:
        with Image.open(filename) as im:
            for frame in ImageSequence.Iterator(im):
                photo = ImageTk.PhotoImage(frame)
                frames.append(photo)
        idx = 0
        def update():
            nonlocal idx
            canvas.itemconfig(image_item, image=frames[idx])
            idx += 1
            if idx == len(frames):
                idx = 0
            canvas.after(100, update)
        image_item = canvas.create_image(0, 0, anchor=NW, image=frames[0])
        canvas.after(0, update)
    except Exception as e:
        print(f"Error loading {filename}: {e}")


def clear():
    fenêtreResultat.delete('1.0', END)

########################################################################################

def attaque_goku():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    Goku.attaque(Vegeta)
    sys.stdout = old_stdout
    print(mystdout.getvalue())
    fenêtreResultat.insert(END, mystdout.getvalue() + "\n********************************************\n\n")
    mise_a_jour_barre()
    bouton_clique()
    kamehameha_sound.play()
    

def soin_goku():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    Goku.soigne(Goku, 15)
    sys.stdout = old_stdout
    print(mystdout.getvalue())
    fenêtreResultat.insert(END, mystdout.getvalue() + "\n********************************************\n\n")
    mise_a_jour_barre()
    bouton_clique()


def caractéristiques_goku():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    Goku.afficheCaractéristiques()
    sys.stdout = old_stdout
    print(mystdout.getvalue())
    fenêtreResultat.insert(END, mystdout.getvalue() + "\n********************************************\n\n")
    bouton_clique()

########################################################################################

def attaque_vegeta():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    Vegeta.attaque(Goku)
    sys.stdout = old_stdout
    print(mystdout.getvalue())
    fenêtreResultat.insert(END, mystdout.getvalue() + "\n********************************************\n\n")
    mise_a_jour_barre()
    bouton_clique()
    bigbang_sound.play()
    


def soin_vegeta():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    Vegeta.soigne(Vegeta, 15)
    sys.stdout = old_stdout
    print(mystdout.getvalue())
    fenêtreResultat.insert(END, mystdout.getvalue() + "\n********************************************\n\n")
    mise_a_jour_barre()
    bouton_clique()


def caractéristiques_vegeta():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    Vegeta.afficheCaractéristiques()
    sys.stdout = old_stdout
    print(mystdout.getvalue())
    fenêtreResultat.insert(END, mystdout.getvalue() + "\n********************************************\n\n")
    bouton_clique()

############################################################################################################################################################# MES PERSONNAGES

### Création de nos personnages (qui seront nos joueurs)

Goku = Personnage(500, "Goku", 100, 50, 30, 10)
Vegeta = Personnage(500, "Vegeta", 100, 40, 30, 20)
Piccolo = Personnage(500, "Piccolo", 100, 50, 20, 50)



########################################################## Création de la fenêtre principale (main window)

Mafenetre =  Tk ()   # On crée un objet tk
Mafenetre.geometry("800x700")
Mafenetre.title('RPG')
Mafenetre.config(bg = "#d1f2eb")
Mafenetre.resizable(False, False)

############################################################################################################################################ CREATION DES FENETRES POUR NOS JOUEURS


######################################################################################################################## Fenêtre pour notre joueur 1

fenêtre1 = Frame(Mafenetre, bg= "#0eecc0", width = 250, height = 350, borderwidth=3, relief = "groove")
fenêtre1.pack(side = LEFT, padx = 100)
fenêtre1.propagate(False)

imgGoku = Canvas(fenêtre1, width = 150, height = 170)
imgGoku.pack(pady = 30)
animate_gif("Goku.gif", imgGoku)

fenêtre1_1 = Frame(fenêtre1, bg= "#16a085", width = 250, height = 100, borderwidth = 3)
fenêtre1_1.pack(side = BOTTOM)
fenêtre1_1.propagate(False)

label_joueur1 = Label(Mafenetre, text= "Joueur 1", width = 35, height=3, bg= "#18CFBB")
label_joueur1.pack(side = LEFT)
label_joueur1.place(x = 100, y= 60)

# label_pointsDeVieJ1 = LabelFrame(Mafenetre, text="PV", width=30, height=200, bg="#22FC18")
# label_pointsDeVieJ1.pack()
# label_pointsDeVieJ1.place(x = 35, y = 250)




######################################################################################################################## Fenêtre pour notre joueur 2

fenêtre2 = Frame(Mafenetre, bg= "#0eecc0", width = 250, height = 350, borderwidth=3, relief = "groove")
fenêtre2.pack(side = LEFT)
fenêtre2.propagate(False)


imgVegeta = Canvas(fenêtre2, width = 150, height = 170)
imgVegeta.pack(pady = 30)
animate_gif("Vegeta.gif", imgVegeta)

fenêtre2_1 = Frame(fenêtre2, bg= "#16a085", width = 250, height = 100, borderwidth = 3)
fenêtre2_1.pack(side = BOTTOM)
fenêtre2_1.propagate(False)

label_joueur2 = Label(Mafenetre, text= "Joueur 2", width = 35, height=3, bg= "#18CFBB")
label_joueur2.pack()
label_joueur2.place(x = 450, y= 60)

# label_pointsDeVieJ2 = LabelFrame(Mafenetre, text="PV", width=30, height=200, bg="#22FC18")
# label_pointsDeVieJ2.pack()
# label_pointsDeVieJ2.place(x = 735, y = 250)



fenêtreResultat = Text(Mafenetre, width = 49, height = 5, bg='white', font=("Helvetica", 16), borderwidth = 2, relief = "solid")
fenêtreResultat.place(x=102, y = 550)
# fenêtreResultat.config(state=DISABLED)

# scrollbar = Scrollbar(fenêtreResultat)
# scrollbar.config(command=fenêtreResultat.yview)
# scrollbar.place(relx=0.97)
# scrollbar.pack(fill=Y)

# fenêtreResultat.config(scrollbar = Scrollbar(fenêtreResultat))



BoutonClear = Button(Mafenetre, text="Clear", width = 6, height = 2, bg = "#FFA533", borderwidth=5, relief = "raised",
              activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command=clear)
BoutonClear.pack(side = BOTTOM)
BoutonClear.place(x = 720, y = 590)




##########################################################################################################################################################   BOUTONS JOUEURS


############################## BOUTON D'ATTAQUE DU JOUEUR 1 (J1)

ButtonAttaquerJ1 = Button(fenêtre1_1, text="Attaquer", width = 6, height = 2, bg = "#FFA533", borderwidth=5, relief = "raised",
                   activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command=attaque_goku)
ButtonAttaquerJ1.pack(side = LEFT, padx = 10)


############################## BOUTON DE DOIN DU JOUEUR 1 (J1)

ButtonSoignerJ1 = Button(fenêtre1_1, text="Soigner", width =6, height = 2, bg = "#FFA533", borderwidth=5, relief = "raised",
                  activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command=soin_goku)
ButtonSoignerJ1.pack(side = LEFT, padx = 10)



############################## BOUTON DE CARACTERISTIQUE DU JOUEUR 1 (J1)

ButtonCaractéristiquesJ1 = Button(fenêtre1_1, text="Caractéristiques", width =6, height = 2, bg = "#FFA533", borderwidth=5, relief = "raised",
                           activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command=caractéristiques_goku)
ButtonCaractéristiquesJ1.pack(side = LEFT, padx = 10)



############################## BOUTON D'ATTAQUE DU JOUEUR 2 (J2)

ButtonAttaquerJ2 = Button(fenêtre2_1, text="Attaquer", width = 6, height = 2, bg = "#FFA533", borderwidth=5, relief = "raised",
                   activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command=attaque_vegeta)
ButtonAttaquerJ2.pack(side = LEFT, padx = 10)

############################## BOUTON DE DOIN DU JOUEUR 2 (J2)

ButtonSoignerJ2 = Button(fenêtre2_1, text="Soigner", width = 6, height = 2, bg = "#FFA533", borderwidth=5, relief = "raised",
                  activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command=soin_vegeta)
ButtonSoignerJ2.pack(side = LEFT, padx = 10)



############################## BOUTON DE CARACTERISTIQUE DU JOUEUR 2 (J2)

ButtonCaractéristiquesJ2 = Button(fenêtre2_1, text="Caractéristiques", width = 6, height = 2, bg = "#FFA533", borderwidth=5, relief = "raised",
                           activebackground = "#5a66f8", activeforeground = "white", foreground = "#0013ff", command = caractéristiques_vegeta)
ButtonCaractéristiquesJ2.pack(side = LEFT, padx = 10)



style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", background = '#3df308')
style.configure("custom.Horizontal.TProgressbar", thickness=20)


barVieGoku = ttk.Progressbar(Mafenetre, length=250, orient='vertical', maximum = Goku.pointsDeVie, style="custom.Horizontal.TProgressbar")
barVieGoku["value"] = Goku.pointsDeVie
barVieGoku.place(x = 35, y = 250)

label_Pv_Goku = Label(Mafenetre, text="PV", bg = "#d1f2eb", font=1)
label_Pv_Goku.place(x = 30, y = 200)


barVieVegeta = ttk.Progressbar(Mafenetre, length=250, orient='vertical', maximum = Vegeta.pointsDeVie, style="custom.Horizontal.TProgressbar")
barVieVegeta["value"] = Vegeta.pointsDeVie
barVieVegeta.place(x = 735, y = 250)

label_Pv_Vegeta = Label(Mafenetre, text="PV", bg = "#d1f2eb", font=1)
label_Pv_Vegeta.place(x = 730, y = 200)



def mise_a_jour_barre():
    barVieGoku["value"] = Goku.pointsDeVie
    barVieVegeta["value"] = Vegeta.pointsDeVie
    # barVieGohan["value"] = Gohan.pointsDeVie
    # barViePiccolo["value"] = Piccolo.pointsDeVie
    
    

pygame.mixer.init()

kamehameha_sound = pygame.mixer.Sound('D:\Formation_Python\RPG_v2\Goku_kamehameha2.mp3')
bigbang_sound = pygame.mixer.Sound('D:\Formation_Python\RPG_v2\Vegeta_BigBang.mp3')





# Initialisation des joueurs et du tour actuel
joueur1 = True
joueur2 = False

# Fonction appelée lorsqu'un bouton est cliqué
def bouton_clique():
    global joueur1, joueur2
    
    # Si c'est le tour du joueur 1
    if joueur1:
        for bouton in boutons_Joueur1:
            bouton.config(state='disabled', background= '#c9c9c9') 
        
        
        for bouton in boutons_Joueur2:
            bouton.config(state='normal', background= '#3df308')
        
        # Effectuer les actions correspondant au clic du joueur 1 ici

        # Changer de tour
        joueur1 = False
        joueur2 = True
        
    # Si c'est le tour du joueur 2
    elif joueur2:
        # Désactiver les boutons du joueur 2 et activer ceux du joueur 1
        
        for bouton in boutons_Joueur2:
            bouton.config(state='disabled', background='#c9c9c9')
        

        for bouton in boutons_Joueur1:
            bouton.config(state='normal', background='#3df308')
        
        # Effectuer les actions correspondant au clic du joueur 2 ici
        
        # Changer de tour
        joueur1 = True
        joueur2 = False
        
        
boutons_Joueur1 = [ButtonAttaquerJ1, ButtonSoignerJ1, ButtonCaractéristiquesJ1]
boutons_Joueur2 = [ButtonAttaquerJ2, ButtonSoignerJ2, ButtonCaractéristiquesJ2]
# boutons_Joueur3 = [ButtonAttaquerJ3, ButtonSoignerJ3, ButtonCaractéristiquesJ3]
# boutons_Joueur4 = [ButtonAttaquerJ4, ButtonSoignerJ4, ButtonCaractéristiquesJ4]

Mafenetre.mainloop()
