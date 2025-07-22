class Groupe:
    def __init__(self, nom, membres=None):
        self.nom = nom
        self.membres = membres if membres else []

    def ajouter(self, personnage):
        self.membres.append(personnage)

    def retirer(self, personnage):
        if personnage in self.membres:
            self.membres.remove(personnage)

    def vivants(self):
        return [p for p in self.membres if hasattr(p, 'est_vivant') and p.est_vivant()]

    def est_vivant(self):
        return any(p.est_vivant() for p in self.membres if hasattr(p, 'est_vivant'))

    def __len__(self):
        return len(self.membres)

    def __str__(self):
        return f"Groupe {self.nom} : {[str(p) for p in self.membres]}"