''' RPG '''

''' 17/02/2023 '''

class Personnage(object):
    # classe mère
    def __init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence):
        self.pointsDeVie = pointsDeVie
        self.nom = nom
        self.force = int(force)
        self.endurance = int(endurance)
        self.rapidité = int(rapidité)
        self.intelligence = int(intelligence)
        self.estMort()

        ''' Méthodes '''

    def estMort(self):
        if self.pointsDeVie > 0:
            self.mort = False
        else:
            self.mort = True


    def afficheEtat(self):
        # ici on rappelle la méthode "estMort"
        self.estMort()
        if self.mort:
            print (f"{self.nom} est mort !")
        else:
            print(f"Il reste {self.pointsDeVie} points de vie à {self.nom}.")


    def afficheCaractéristiques(self):
        print(f"{self.nom} a une force de {self.force}, une endurance de {self.endurance}, une rapidité de {self.rapidité} et une intelligence de {self.intelligence}.")


    def perdVie(self, nbPointsDeViePerdus):
        if nbPointsDeViePerdus >= self.pointsDeVie:
            print (f"{self.nom} a perdu {nbPointsDeViePerdus} point(s) de vie et subit un coup mortel. {self.nom} est mort !")
            self.pointsDeVie = 0
        else:
            self.pointsDeVie = self.pointsDeVie - nbPointsDeViePerdus
            print (f"{self.nom} a perdu ", nbPointsDeViePerdus, "point(s) de vie.\nSes points de vie sont maintenant de", self.pointsDeVie,".")
        #self.afficheEtat()
        
        # self.maj_barre_progression()


    def gagneVie(self, nbPointsVieGagnés):
        if self.pointsDeVie > 0 :
            self.pointsDeVie = self.pointsDeVie + nbPointsVieGagnés
            print(f"{self.nom} a été soigné de {nbPointsVieGagnés} point(s) de vie.\nSes points de vie sont maintenant de {self.pointsDeVie}.")
        else:
            print(f"{self.nom} ne peut pas être soigné car il est mort ce faible.")


    def attaque (self, autrePersonnage):
        if self.pointsDeVie > 0 and autrePersonnage.pointsDeVie > 0:
            print(f"{self.nom} attaque {autrePersonnage.nom} !")
            if not autrePersonnage.esquiveAttaque(self):
                self.pointsDeDégâts = int(0.6*self.force)
                autrePersonnage.perdVie(self.pointsDeDégâts),"."
        else:
            if self.pointsDeVie <=0:
               return (f"{self.nom} est mort, il ne peut attaquer ni être attaqué.")
            if autrePersonnage.pointsDeVie <=0:
               return(f"{autrePersonnage.nom} est mort, il ne peut attaquer ni être attaqué.")
        



    def esquiveAttaque(self, autrePersonnage):
        if self.pointsDeVie > 0 and autrePersonnage.pointsDeVie > 0:
            if int(self.rapidité*1.2) > autrePersonnage.force:
                print (f"La rapidité de {self.nom} ({int(self.rapidité*1.2)}) est supérieur à la force de {autrePersonnage.nom} ({autrePersonnage.force}) !")
                print (f"{self.nom} parvient à esquiver l'attaque!")
                # revoir peut être la rapidité et mettre son calcul dans le print pour pas que sa valeur initiale ne soit impactée
                return True
            else:
                print(f"{self.nom} n'a pu esquiver l'attaque !")
                return False
        else:
            if self.pointsDeVie <=0:
                print(f"{self.nom} ne peut esquiver / être attaquer car il est mort.")
            if autrePersonnage.pointsDeVie <=0:
                print(f"{autrePersonnage.nom} ne peut esquiver / être attaquer car il est mort.")


    def soigne (self, autrePersonnage, pointsDeSoin):
        if self.pointsDeVie > 0 and autrePersonnage.pointsDeVie > 0:
            print(f"{self.nom} a soigné {autrePersonnage.nom}!")
            autrePersonnage.gagneVie(pointsDeSoin),"."
        else:
            if self.pointsDeVie <=0:
                print(f"{self.nom} est mort, il ne peut soigner ni être soigné.")
            if autrePersonnage.pointsDeVie <=0:
                print(f"{autrePersonnage.nom} est mort, il ne peut soigner ni être soigné.")

    def seDéplacer (pointDeDéplacement):
        pass

    
    # def maj_barre_progression(self):
    #     barre_progression = self.pointsDeVie
    #     barre_progression['value'] = self.points_vie


'''

########################################################################## MAIN

# print (dir(Personnage))
# pointsDeVie, nom, force, endurance, rapidité, intelligence

Goku = Personnage(100, "Goku", 100, 20, 322, 10)
print(vars(Goku))

###########################

Broly = Personnage(100, "Broly", 350, 30, 26, 10)

###########################

Broly.attaque(Goku)
# Personnage.attaque(Broly, Goku)   # cette écriture est l'équivalente de celle du dessus

###########################


piccolo = Personnage(100, "Piccolo", 555, 555, 555, 555)
piccolo.attaque(Goku)

'''
