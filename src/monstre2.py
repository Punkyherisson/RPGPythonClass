import random

class Monstre:
    def __init__(
        self, nom: str, niveau: int, pv: int, attaque: int, defense: int,
        loot: list = None, type_monstre: str = "bête", resistances: dict = None,
        faiblesses: dict = None, cri: str = "", comportement: str = "agressif"
    ):
        self.nom = nom
        self.niveau = niveau
        self.pv_max = pv
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.loot = loot if loot else []
        self.type_monstre = type_monstre
        self.resistances = resistances if resistances else {}
        self.faiblesses = faiblesses if faiblesses else {}
        self.cri = cri
        self.comportement = comportement  # "agressif", "défensif", "fuyant", "aléatoire"

    def est_vivant(self):
        return self.pv > 0

    def subir_degats(self, degats: int, type_attaque: str = None):
        reduction = self.defense
        if type_attaque:
            if type_attaque in self.resistances:
                reduction += self.resistances[type_attaque]
            if type_attaque in self.faiblesses:
                reduction -= self.faiblesses[type_attaque]
        degats_finals = max(0, degats - reduction)
        self.pv = max(0, self.pv - degats_finals)
        return degats_finals

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} !")
        return cible.subir_degats(self.attaque)

    def drop_loot(self):
        return random.choice(self.loot) if self.loot else None

    def crier(self):
        if self.cri:
            print(f"{self.nom} crie : {self.cri}")
        else:
            print(f"{self.nom} pousse un cri bestial !")

    def comportement_ia(self):
        actions = {
            "agressif": "attaque",
            "défensif": "défend",
            "fuyant": "fuit",
            "aléatoire": random.choice(["attaque", "défend", "fuit"])
        }
        return actions.get(self.comportement, "attaque")

    def __str__(self):
        return (f"{self.nom} (niveau {self.niveau}, type {self.type_monstre}) "
                f"PV: {self.pv}/{self.pv_max}, Attaque: {self.attaque}, Défense: {self.defense}")