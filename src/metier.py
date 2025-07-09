class Metier:
    def __init__(self, nom, type_metier, effet_passif=None):
        self.nom = nom
        self.type_metier = type_metier  # "combat", "recolte", "artisanat", "special"
        self.effet_passif = effet_passif or {}

    def appliquer_effets(self, personnage):
        for stat, bonus in self.effet_passif.items():
            personnage.stats[stat] = personnage.stats.get(stat, 0) + bonus

    def __str__(self):
        return f"{self.nom} ({self.type_metier})"
    
metiers = [

    # 🔪 Métiers de Combat
    Metier("Guerrier", "combat", {"force": 5, "defense": 3}),
    Metier("Barbare", "combat", {"force": 7, "vitesse": -1}),
    Metier("Archer", "combat", {"agilite": 5, "critique": 5}),
    Metier("Druide", "combat", {"mana": 10, "regeneration": 2}),
    Metier("Mage", "combat", {"intelligence": 7, "mana": 10}),
    Metier("Prêtre", "combat", {"soin": 5, "mana": 5}),
    Metier("Paladin", "combat", {"defense": 6, "soin": 3}),
    Metier("Mercenaire", "combat", {"force": 4, "or": 10}),

    # 🪓 Métiers de Récolte
    Metier("Mineur", "recolte", {"endurance": 5, "chance": 2}),
    Metier("Bûcheron", "recolte", {"force": 3, "vitesse": 1}),
    Metier("Agriculteur", "recolte", {"regeneration": 2, "chance": 3}),

    # 🛠 Métiers d'Artisanat
    Metier("Forgeron", "artisanat", {"force": 2, "durabilité": 5}),
    Metier("Menuisier", "artisanat", {"vitesse": 2, "chance": 2}),
    Metier("Couturier", "artisanat", {"agilite": 2, "defense": 2}),
    Metier("Alchimiste", "artisanat", {"potions": 5, "mana": 5}),

    # 🎭 Métiers Spéciaux
    Metier("Barde", "special", {"charisme": 5, "chance": 3}),
    Metier("Voleur", "special", {"vitesse": 5, "discretion": 5}),
    Metier("Assassin", "special", {"critique": 10, "discretion": 5}),

]