# race.py
class Race:
    def __init__(self, nom, modificateurs):
        self.nom = nom
        self.modificateurs = modificateurs  # dictionnaire: {"force": +2, "intelligence": -1}

    def get_modificateur(self, attribut):
        return self.modificateurs.get(attribut, 0)

    def __str__(self):
        mods = ", ".join(f"{k}: {v:+d}" for k, v in self.modificateurs.items())
        return f"{self.nom} ({mods})"