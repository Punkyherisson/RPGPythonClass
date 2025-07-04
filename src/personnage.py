class Personnage:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.vie = 100
        self.niveau = 1
        self.xp = 0
        self.defense = 0

    def attaquer(self, cible):
        degats = 10
        cible.vie -= degats

    def gagner_xp(self, montant):
        self.xp += montant
        if self.xp >= 100:
            self.niveau += 1
            self.xp -= 100

    def est_vivant(self):
        return self.vie > 0
    
    def subir_degats(self, degats):
        reduction = self.defense
        degats_finals = max(0, degats - reduction)
        self.vie -= degats_finals
        print(f"{self.nom} subit {degats_finals} dégâts. Vie restante : {self.vie}")

    

