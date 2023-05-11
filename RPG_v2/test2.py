# import tkinter as tk

# class Personnage:
#     def __init__(self, pointsDeVie):
#         self.pointsDeVie = pointsDeVie
        
#         # Création de la fenêtre principale
#         self.fenetre = tk.Tk()
        
#         # Création du Canvas pour la barre de vie
#         self.canvas = tk.Canvas(self.fenetre, width=200, height=20)
#         self.canvas.pack()
        
#         # Création de la barre de vie proportionnelle au nombre de points de vie
#         self.barreDeVie = self.canvas.create_rectangle(0, 0, 200*self.pointsDeVie/100, 20, fill='green')
        
#         # Création du bouton d'attaque
#         self.boutonAttaque = tk.Button(self.fenetre, text='Attaquer', command=self.attaque)
#         self.boutonAttaque.pack()
        
#         # Affichage de la fenêtre principale
#         self.fenetre.mainloop()
    
#     def attaque(self):
#         self.perdrePointsDeVie(20)
    
#     def perdrePointsDeVie(self, points):
#         self.pointsDeVie -= points
        
#         # Décrémentation de la barre de vie proportionnelle au nombre de points de vie
#         self.canvas.coords(self.barreDeVie, 0, 0, 200*self.pointsDeVie/100, 20)
        
#         # Changement de couleur de la barre de vie si elle est en dessous de 50%
#         if self.pointsDeVie < 50:
#             self.canvas.itemconfig(self.barreDeVie, fill='orange')
#         # Changement de couleur de la barre de vie si elle est en dessous de 25%
#         if self.pointsDeVie < 25:
#             self.canvas.itemconfig(self.barreDeVie, fill='red')

# # Création d'un objet Personnage avec 100 points de vie
# Goku = Personnage(100)


# import tkinter as tk
# from tkinter import ttk

# def update_health_bar(health_points, progressbar):
#     progressbar["value"] = health_points

# def attack(health_points, progressbar, attack_button):
#     # Simuler une attaque qui retire 10 points de vie
#     health_points -= 10
#     if health_points <= 0:
#         health_points = 0
#         attack_button["state"] = "disabled"
#     update_health_bar(health_points, progressbar)

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Barre de vie")
#     root.geometry("400x100")

#     # Initialisation de la barre de progression
#     progressbar = ttk.Progressbar(root, orient="horizontal", mode="determinate", maximum=100, length=300)
#     progressbar.pack(pady=20)

#     # Bouton pour tester la fonctionnalité de la barre de vie
#     attack_button = tk.Button(root, text="Attaquer", command=lambda: attack(health_points, progressbar, attack_button))
#     attack_button.pack(pady=10)

#     # Initialisation des points de vie
#     health_points = 100
#     update_health_bar(health_points, progressbar)

#     root.mainloop()
    
 
     

import tkinter as tk
from tkinter import ttk

def update_health_bar(health_points, progressbar):
    progressbar["value"] = health_points

def attack(progressbar, attack_button):
    global health_points # declare health_points comme une variable globale
    # Simuler une attaque qui retire 10 points de vie
    health_points -= 10
    if health_points <= 0:
        health_points = 0
        attack_button["state"] = "disabled"
    update_health_bar(health_points, progressbar)
    

root = tk.Tk()
root.title("Barre de vie")
root.geometry("400x100")

# Initialisation de la barre de progression
progressbar = ttk.Progressbar(root, orient="horizontal", mode="determinate", maximum=100, length=300)
progressbar.pack(pady=20)

# Bouton pour tester la fonctionnalité de la barre de vie
attack_button = tk.Button(root, text="Attaquer", command=lambda: attack(progressbar, attack_button))
attack_button.pack(pady=10)

# Initialisation des points de vie
health_points = 100
update_health_bar(health_points, progressbar)


root.mainloop()