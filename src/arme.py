class Arme:
    def __init__(self, nom, degats, type_arme="tranchant", rarete="commune"):
        self.nom = nom
        self.degats = degats
        self.type_arme = type_arme
        self.rarete = rarete

    def description(self):
        return f"{self.nom} ({self.type_arme}) - Dégâts : {self.degats}, Rareté : {self.rarete}"

    def ameliorer(self, bonus):
        self.degats += bonus
    def __str__(self):
        return f"{self.nom} - Dégâts : {self.degats}, Type : {self.type_arme}, Rareté : {self.rarete}"
    