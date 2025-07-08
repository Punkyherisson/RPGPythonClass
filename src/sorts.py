class Sort:
    def __init__(self, nom: str, degats: int, cout_mana: int, type_sort: str = "offensif"):
        self.nom = nom
        self.degats = degats
        self.cout_mana = cout_mana
        self.type_sort = type_sort  # 'offensif' ou 'defensif'

    def lancer(self, cible):
        """Applique le sort à la cible si c’est un sort offensif"""
        if self.type_sort == "offensif":
            cible.subir_degats(self.degats)
        elif self.type_sort == "defensif":
            cible.vie += abs(self.degats)  # Soins

    def __str__(self):
        return f"{self.nom} ({self.type_sort} - Mana: {self.cout_mana})"