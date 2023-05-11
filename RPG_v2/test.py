import tkinter as tk

class HealthBar:
    def __init__(self, master, max_value):
        self.max_value = max_value
        self.current_value = max_value
        self.canvas = tk.Canvas(master, width=200, height=20)
        self.canvas.pack()
        self.health_bar = self.canvas.create_rectangle(0, 0, 200, 20, fill="#5ff40f")

    def decrement(self, value):
        if self.current_value - value < 0:
            self.current_value = 0
        else:
            self.current_value -= value
        self.update()

    def update(self):
        health_percentage = self.current_value / self.max_value
        new_width = health_percentage * 200
        self.canvas.coords(self.health_bar, (0, 0, new_width, 20))

root = tk.Tk()
health_bar = HealthBar(root, 100)
button = tk.Button(root, text="Take Damage", command=lambda: health_bar.decrement(10))
button.pack()
root.mainloop()


# from tkinter import *
# import tkinter as tk

# class HealthBar:
#     def __init__(self, master, max_value):
#         self.max_value = max_value
#         self.current_value = max_value
#         self.canvas = tk.Canvas(master, width=200, height=20)
#         self.canvas.pack()
#         self.health_bar = self.canvas.create_rectangle(0, 0, 200, 20, fill="green")

#     def decrement(self, value):
#         if self.current_value - value < 0:
#             self.current_value = 0
#         else:
#             self.current_value -= value
#         self.update()

#     def update(self):
#         health_percentage = self.current_value / self.max_value
#         new_width = health_percentage * 200
#         self.canvas.coords(self.health_bar, (0, 0, new_width, 20))

# class Personnage(object):
#     def __init__(self, pointsDeVie, nom, force):
#         self.pointsDeVie = pointsDeVie
#         self.nom = nom
#         self.force = int(force)

#     def perdVie(self, nbPointsDeViePerdus):
#         if nbPointsDeViePerdus >= self.pointsDeVie:
#             print (f"{self.nom} a perdu {nbPointsDeViePerdus} point(s) de vie et subit un coup mortel. {self.nom} est mort !")
#             fenêtreResultat.insert(END,f"{self.nom} a perdu {nbPointsDeViePerdus} point(s) de vie et subit un coup mortel. {self.nom} est mort !\n")
#             fenêtreResultat.see(END)
#             if (self.nom == "Goku"):
#                 health_bar1.decrement(nbPointsDeViePerdus)
#             else:
#                 health_bar2.decrement(nbPointsDeViePerdus)
#             self.pointsDeVie = 0
#         else:
#             self.pointsDeVie = self.pointsDeVie - nbPointsDeViePerdus
#             print (f"{self.nom} a perdu ", nbPointsDeViePerdus, "point(s) de vie. Ses points de vie sont maintenant de", self.pointsDeVie)
#             fenêtreResultat.insert(END,f"{self.nom} a perdu {nbPointsDeViePerdus} point(s) de vie. Ses points de vie sont maintenant de {self.pointsDeVie}\n")
#             fenêtreResultat.see(END)
#             if (self.nom == "Goku"):
#                 health_bar1.decrement(nbPointsDeViePerdus)
#             else:
#                 health_bar2.decrement(nbPointsDeViePerdus)

#     def attaque (self, autrePersonnage):        
#         if self.pointsDeVie > 0 and autrePersonnage.pointsDeVie > 0:
#             print(f"{self.nom} attaque {autrePersonnage.nom} !")
#             fenêtreResultat.insert(END,f"{self.nom} attaque {autrePersonnage.nom} !\n")
#             fenêtreResultat.see(END)
#             self.pointsDeDégâts = int(0.6*self.force)
#             autrePersonnage.perdVie(self.pointsDeDégâts),"."
#         else:
#             if self.pointsDeVie <=0:
#                print (f"{self.nom} est mort, il ne peut attaquer ni être attaqué.")
#                fenêtreResultat.insert(END,f"{self.nom} est mort, il ne peut attaquer ni être attaqué.\n")
#                fenêtreResultat.see(END)
#             if autrePersonnage.pointsDeVie <=0:
#                print(f"{autrePersonnage.nom} est mort, il ne peut attaquer ni être attaqué.")
#                fenêtreResultat.insert(END,f"{autrePersonnage.nom} est mort, il ne peut attaquer ni être attaqué.\n")
#                fenêtreResultat.see(END)

# def AttaqueJ1():
#     Goku.attaque(Vegeta)

# def AttaqueJ2():
#     Vegeta.attaque(Goku)

# Goku = Personnage(1000,"Goku",40)
# Vegeta = Personnage(1000,"Vegeta",40)

# Mafenetre = Tk()
# Mafenetre.geometry("800x700")

# fenêtre1 = Frame(Mafenetre, width = 250, height = 350, borderwidth=3, relief = "groove")
# fenêtre1.pack(side = LEFT, padx = 100)
# fenêtre1.propagate(False)

# fenêtre2 = Frame(Mafenetre, width = 250, height = 350, borderwidth=3, relief = "groove")
# fenêtre2.pack(side = RIGHT, padx = 100)
# fenêtre2.propagate(False)

# fenêtreResultat = Text(Mafenetre, width = 49, height = 5)
# fenêtreResultat.pack()
# fenêtreResultat.place(x=102,y=550)

# ButtonAttaquerJ1 = Button(fenêtre1,text="Attaquer",width=6,height=2)
# ButtonAttaquerJ1.pack(side=LEFT,padx=10)
# ButtonAttaquerJ1.config(command=AttaqueJ1)

# ButtonAttaquerJ2 = Button(fenêtre2,text="Attaquer",width=6,height=2)
# ButtonAttaquerJ2.pack(side=RIGHT,padx=10)
# ButtonAttaquerJ2.config(command=AttaqueJ2)

# health_bar1 = HealthBar(fenêtre1, Goku.pointsDeVie)
# health_bar2 = HealthBar(fenêtre2,Vegeta.pointsDeVie)

# Mafenetre.mainloop()


