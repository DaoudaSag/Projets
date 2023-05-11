# import tkinter as tk

# # Initialisation des joueurs et du tour actuel
# joueur1 = True
# joueur2 = False

# # Fonction appelée lorsqu'un bouton est cliqué
# def bouton_clique():
#     global joueur1, joueur2
    
#     # Si c'est le tour du joueur 1, désactiver les boutons du joueur 2
#     if joueur1:
#         bouton_joueur2_1.config(state='disabled')
#         bouton_joueur2_2.config(state='disabled')
#         bouton_joueur2_3.config(state='disabled')
        
#         # Effectuer les actions correspondant au clic du joueur 1 ici
        
#         # Changer de tour
#         joueur1 = False
#         joueur2 = True
        
#     # Si c'est le tour du joueur 2, désactiver les boutons du joueur 1
#     elif joueur2:
#         bouton_joueur2_1.config(state='normal')
#         bouton_joueur2_2.config(state='normal')
#         bouton_joueur2_3.config(state='normal')
        
#         bouton_joueur1_1.config(state='disabled')
#         bouton_joueur1_2.config(state='disabled')
#         bouton_joueur1_3.config(state='disabled')
        
#         # Effectuer les actions correspondant au clic du joueur 2 ici
        
#         # Changer de tour
#         joueur1 = True
#         joueur2 = False
        
#         # Réactiver les boutons pour le joueur suivant
#         bouton_joueur1_1.config(state='normal')
#         bouton_joueur1_2.config(state='normal')
#         bouton_joueur1_3.config(state='normal')
        
#         bouton_joueur2_1.config(state='disabled')
#         bouton_joueur2_2.config(state='disabled')
#         bouton_joueur2_3.config(state='disabled')

# # Création de la fenêtre et des boutons
# fenetre = tk.Tk()

# bouton_joueur1_1 = tk.Button(fenetre, text="Joueur 1 Bouton 1", command=bouton_clique)
# bouton_joueur1_1.grid(row=0, column=0)

# bouton_joueur1_2 = tk.Button(fenetre, text="Joueur 1 Bouton 2", command=bouton_clique)
# bouton_joueur1_2.grid(row=0, column=1)

# bouton_joueur1_3 = tk.Button(fenetre, text="Joueur 1 Bouton 3", command=bouton_clique)
# bouton_joueur1_3.grid(row=0, column=2)

# bouton_joueur2_1 = tk.Button(fenetre, text="Joueur 2 Bouton 1", command=bouton_clique)
# bouton_joueur2_1.grid(row=1, column=0)

# bouton_joueur2_2 = tk.Button(fenetre, text="Joueur 2 Bouton 2", command=bouton_clique)
# bouton_joueur2_2.grid(row=1, column=1)

# bouton_joueur2_3 = tk.Button(fenetre, text="Joueur 2 Bouton 3", command=bouton_clique)
# bouton_joueur2_3.grid(row=1, column=2)

# # Désactiver les boutons du joueur 2 au début de la partie
# bouton_joueur2_1.config(state='disabled')
# bouton_joueur2_2.config(state='disabled')
# bouton_joueur2_3.config(state='disabled')

# fenetre.mainloop()


import tkinter as tk

# Initialisation des joueurs et du tour actuel
joueur1 = True
joueur2 = False
joueur3 = False
joueur4 = False


# Fonction appelée lorsqu'un bouton est cliqué
def bouton_clique():
    global joueur1, joueur2, joueur3, joueur4
    
        
    # Si c'est le tour du joueur 1
    if joueur1:

        for bouton in (bouton_J1):
            bouton.config(state='disabled', background= '#c9c9c9') 
        
        for bouton in bouton_J2:
            bouton.config(state='normal', background= '#3df308')
            
        for bouton in bouton_J3:
            bouton.config(state='disabled', background= '#c9c9c9') 
            
        for bouton in bouton_J4:
            bouton.config(state='disabled', background= '#c9c9c9') 

        
        # Effectuer les actions correspondant au clic du joueur 1 ici

        # Changer de tour
        joueur1 = False
        joueur2 = True
        joueur3 = False
        joueur4 = False
        
    # Si c'est le tour du joueur 2
    elif joueur2:

        for bouton in bouton_J1:
            bouton.config(state='disabled', background= '#c9c9c9') 
        
        for bouton in bouton_J2:
            bouton.config(state='disabled', background= '#c9c9c9')
            
        for bouton in bouton_J3:
            bouton.config(state='normal', background= '#3df308') 
            
        for bouton in bouton_J4:
            bouton.config(state='disabled', background= '#c9c9c9') 

        
        # Effectuer les actions correspondant au clic du joueur 2 ici
        
        # Changer de tour
        joueur1 = False
        joueur2 = False
        joueur3 = True
        joueur4 = False
        
    
    elif joueur3:

        for bouton in bouton_J1:
            bouton.config(state='disabled', background= '#c9c9c9') 
        
        for bouton in bouton_J2:
            bouton.config(state='disabled', background= '#c9c9c9')
            
        for bouton in bouton_J3:
            bouton.config(state='disabled', background= '#c9c9c9')
            
        for bouton in bouton_J4:
            bouton.config(state='normal', background= '#3df308')
            
            
        # Changer de tour
        joueur1 = False
        joueur2 = False
        joueur3 = False
        joueur4 = True
        
    
    elif joueur4:

        for bouton in bouton_J1:
            bouton.config(state='normal', background= '#3df308')
        
        for bouton in bouton_J2:
            bouton.config(state='disabled', background= '#c9c9c9')
            
        for bouton in bouton_J3:
            bouton.config(state='disabled', background= '#c9c9c9')
            
        for bouton in bouton_J4:
            bouton.config(state='disabled', background= '#c9c9c9')
        
        
        # Changer de tour
        joueur1 = True
        joueur2 = False
        joueur3 = False
        joueur4 = False
            
    
# Création de la fenêtre et des boutons
fenetre = tk.Tk()

bouton_joueur1_1 = tk.Button(fenetre, text="Joueur 1 Bouton 1", command=bouton_clique)
bouton_joueur1_1.grid(row=0, column=0)

bouton_joueur1_2 = tk.Button(fenetre, text="Joueur 1 Bouton 2", command=bouton_clique)
bouton_joueur1_2.grid(row=0, column=1)

bouton_joueur1_3 = tk.Button(fenetre, text="Joueur 1 Bouton 3", command=bouton_clique)
bouton_joueur1_3.grid(row=0, column=2)

bouton_joueur2_1 = tk.Button(fenetre, text="Joueur 2 Bouton 1", command=bouton_clique)
bouton_joueur2_1.grid(row=1, column=0)

bouton_joueur2_2 = tk.Button(fenetre, text="Joueur 2 Bouton 2", command=bouton_clique)
bouton_joueur2_2.grid(row=1, column=1)

bouton_joueur2_3 = tk.Button(fenetre, text="Joueur 2 Bouton 3", command=bouton_clique)
bouton_joueur2_3.grid(row=1, column=2)

bouton_joueur3_1 = tk.Button(fenetre, text="Joueur 3 Bouton 1", command=bouton_clique)
bouton_joueur3_1.grid(row=2, column=0)

bouton_joueur3_2 = tk.Button(fenetre, text="Joueur 3 Bouton 2", command=bouton_clique)
bouton_joueur3_2.grid(row=2, column=1)

bouton_joueur3_3 = tk.Button(fenetre, text="Joueur 3 Bouton 3", command=bouton_clique)
bouton_joueur3_3.grid(row=2, column=2)

bouton_joueur4_1 = tk.Button(fenetre, text="Joueur 4 Bouton 1", command=bouton_clique)
bouton_joueur4_1.grid(row=3, column=0)

bouton_joueur4_2 = tk.Button(fenetre, text="Joueur 4 Bouton 2", command=bouton_clique)
bouton_joueur4_2.grid(row=3, column=1)

bouton_joueur4_3 = tk.Button(fenetre, text="Joueur 4 Bouton 3", command=bouton_clique)
bouton_joueur4_3.grid(row=3, column=2)


bouton_J1 = [bouton_joueur1_1, bouton_joueur1_2, bouton_joueur1_3]
bouton_J2 = [bouton_joueur2_1, bouton_joueur2_2, bouton_joueur2_3]
bouton_J3 = [bouton_joueur3_1, bouton_joueur3_2, bouton_joueur3_3]
bouton_J4 = [bouton_joueur4_1, bouton_joueur4_2, bouton_joueur4_3]

# # Désactiver les boutons du joueur 2 au début de la partie
bouton_joueur2_1.config(state='disabled')
bouton_joueur2_2.config(state='disabled')
bouton_joueur2_3.config(state='disabled')

bouton_joueur3_1.config(state='disabled')
bouton_joueur3_2.config(state='disabled')
bouton_joueur3_3.config(state='disabled')

bouton_joueur4_1.config(state='disabled')
bouton_joueur4_2.config(state='disabled')
bouton_joueur4_3.config(state='disabled')


fenetre.mainloop()

