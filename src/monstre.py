class Monstre:
    def __init__(self, nom, niveau=1, vie=30, force=5, defense=2):
        self.nom = nom
        self.niveau = niveau
        self.vie = vie
        self.force = force
        self.defense = defense

    def est_vivant(self):
        return self.vie > 0

    def attaquer(self, cible):
        if not self.est_vivant():
            print(f"{self.nom} est KO et ne peut pas attaquer.")
            return

        degats = max(0, self.force - cible.defense)
        cible.vie -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")

    def subir_degats(self, degats):
        reduction = self.defense
        degats_finals = max(0, degats - reduction)
        self.vie -= degats_finals
        print(f"{self.nom} subit {degats_finals} dégâts. Vie restante : {self.vie}")