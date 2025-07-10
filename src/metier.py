class Metier:
    def __init__(self, nom: str, domaine: str, bonus_base: dict):
        self.nom = nom                      # "Guerrier", "Mage", etc.
        self.domaine = domaine              # "combat", "magie", etc.
        self.bonus_base = bonus_base if bonus_base is not None else {}        # {"force": 5, "defense": 3}
        self.niveau = 1
        self.xp = 0
        self.xp_max = 100

    def gagner_xp(self, quantite: int):
        self.xp += quantite
        while self.xp >= self.xp_max and self.niveau < 100:
            self.xp -= self.xp_max
            self.niveau += 1
            self.xp_max = int(self.xp_max * 1.2)  # XP nécessaire augmente à chaque niveau

    @property
    def bonus(self):
        # Bonus évolutif : augmente légèrement avec le niveau
        bonus_evolutif = {}
        for attr, val in self.bonus_base.items():
            bonus_evolutif[attr] = val + int(self.niveau / 10)
        return bonus_evolutif

    @classmethod
    def afficher_metiers(cls, liste_metiers):
        print("\n📜 Liste des Métiers Disponibles :\n")
        for m in liste_metiers:
            bonus_str = ', '.join(f"{k}: {v}" for k, v in m.bonus_base.items())
            print(f"🔹 {m.nom} [{m.domaine}] — Bonus de départ : {bonus_str}")    
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