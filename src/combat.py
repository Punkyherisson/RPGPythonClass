import random

class Combat:
    def __init__(self, groupe_1, groupe_2):
        self.groupe_1 = groupe_1
        self.groupe_2 = groupe_2

    def un_tour(self):
        # Groupe 1 attaque
        for attaquant in self.groupe_1.vivants():
            cibles = self.groupe_2.vivants()
            if not cibles:
                return
            cible = random.choice(cibles)
            attaquant.attaquer(cible)

        # Groupe 2 attaque
        for attaquant in self.groupe_2.vivants():
            cibles = self.groupe_1.vivants()
            if not cibles:
                return
            cible = random.choice(cibles)
            attaquant.attaquer(cible)

    def est_termine(self):
        return not self.groupe_1.est_vivant() or not self.groupe_2.est_vivant()

    def gagnant(self):
        if self.groupe_1.est_vivant() and not self.groupe_2.est_vivant():
            return self.groupe_1.nom
        elif self.groupe_2.est_vivant() and not self.groupe_1.est_vivant():
            return self.groupe_2.nom
        return None