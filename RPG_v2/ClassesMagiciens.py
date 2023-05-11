from RPG_Final import*


##############################################      Classe mère      ##############################################


class Magicien(Personnage):

    def __init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie):
        """ héritage de la classe Personnage """
        Personnage.__init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence)

        # nouvel attribut
        self.pointsDeMagie = pointsDeMagie


    def faireMagie(self, autrePersonnage):
        if self.pointsDeVie > 0 and autrePersonnage.pointsDeVie > 0:
            if self.pointsDeMagie > 0:
            # à l'avenir peut-être modifier cette ligne en --> if self.pointsDeMagie >= coûtSort :
                self.dégâtsMagie = int(0.6*self.intelligence)
                if self.dégâtsMagie > 0:
                    print(f"{self.nom} lance un sort sur {autrePersonnage.nom} !")
                    autrePersonnage.perdVie(self.dégâtsMagie)
                    #self.attaque(autrePersonnage)
                if self.dégâtsMagie < 0:
                    print(f"{self.nom} lance un sort sur {autrePersonnage.nom} !")
                    autrePersonnage.gagneVie(-self.dégâtsMagie) # ici on inverse le signe pour rendre les dégâts positifs
                # à l'avenir ajouter --> pointsDeMagie = pointsDeMagie - coûtSort



##############################################      Classes filles      ##############################################


class MagHumain(Magicien):
    def __init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie):
        Magicien.__init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie)
        self.race = "Humain"


class MagHobbit(Magicien):
    def __init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie):
        Magicien.__init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie)
        self.race = "Hobbit"


class MagElfe(Magicien):
    def __init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie):
        Magicien.__init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie)
        self.race = "Elfe"


class MagNain(Magicien):
    def __init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie):
        Magicien.__init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie)
        self.race = "Nain"


class MagOrque(Magicien):
    def __init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie):
        Magicien.__init__(self, pointsDeVie, nom, force, endurance, rapidité, intelligence, pointsDeMagie)
        self.race = "Orque"


##############################################      Classes filles      ##############################################


print(dir(Magicien))

Babidi = Magicien(10, "Babidi", 2, 5, 3, 50, 100)


Shin = MagElfe(200, "Shin", 50, 60, 30, -70, 400)
Shin.faireMagie(Babidi)

print(Shin.race)