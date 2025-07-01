class Personnage:
    def __init__(self, nom, classe, niveau=1):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.vie = 100
        self.force = 10
        self.defense = 5
        self.experience = 0

    def attaquer(self, cible):
        degats = max(1, self.force - cible.defense)
        cible.vie -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts!")

    def est_vivant(self):
        return self.vie > 0

    def gagner_xp(self, xp):
        self.experience += xp
        if self.experience >= self.niveau * 100:
            self.niveau += 1
            self.vie += 20
            self.force += 2
            self.defense += 1
            print(f"{self.nom} passe au niveau {self.niveau} !")