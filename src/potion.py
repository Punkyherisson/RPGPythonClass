class Potion:
    def __init__(self, nom, effet, puissance):
        self.nom = nom
        self.effet = effet  # "vie" ou "mana"
        self.puissance = puissance

    def utiliser(self, cible):
        if self.effet == "vie":
            cible.vie += self.puissance
        elif self.effet == "mana":
            if hasattr(cible, "mana"):
                cible.mana += self.puissance
        else:
            raise ValueError("Effet inconnu")