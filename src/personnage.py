import random
import json
from metier import Metier

class Personnage:
    def __init__(self, nom: str, metier, pv_max=100):
        self.nom = nom
        self.metier = metier  # instance de Metier
        self.pv_max = pv_max
        self.pv = pv_max
        self.inventaire = []
        self.xp = 0
        self.niveau = 1
        self.stats = self._calculer_stats()

    def _calculer_stats(self):
        # Combine les bonus métier avec des stats de base
        base_stats = {
            "force": 10,
            "defense": 5,
            "critique": 5,
            "vitesse": 5
        }
        bonus = self.metier.bonus
        for cle, val in bonus.items():
            base_stats[cle] = base_stats.get(cle, 0) + val
        return base_stats

    def attaquer(self, cible):
        base_degats = self.stats.get("force", 5)
        critique = self.stats.get("critique", 0)
        total_degats = base_degats
        if random.randint(1, 100) <= critique:
            total_degats *= 2
            print(f"💥 {self.nom} fait un coup critique !")
        print(f"{self.nom} attaque {cible.nom} pour {total_degats} dégâts.")
        cible.subir_degats(total_degats)

    def subir_degats(self, degats):
        reduction = self.stats.get("defense", 0)
        degats_finals = max(0, degats - reduction)
        self.pv = max(0, self.pv - degats_finals)
        print(f"{self.nom} subit {degats_finals} dégâts, PV restants : {self.pv}")

    def est_vivant(self):
        return self.pv > 0

    def gagner_xp(self, montant):
        self.metier.gagner_xp(montant)
        # Synchroniser niveau avec métier
        self.niveau = self.metier.niveau
        print(f"{self.nom} gagne {montant} XP, niveau {self.niveau}")

    def sauvegarder(self, chemin_fichier):
        data = {
            "nom": self.nom,
            "metier": {
                "nom": self.metier.nom,
                "domaine": self.metier.domaine,
                "niveau": self.metier.niveau,
                "xp": self.metier.xp,
                "xp_max": self.metier.xp_max,
                "bonus_base": self.metier.bonus_base
            },
            "pv_max": self.pv_max,
            "pv": self.pv,
            "inventaire": self.inventaire
        }
        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"{self.nom} sauvegardé dans {chemin_fichier}")

    @classmethod
    def charger(cls, chemin_fichier):
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
        metier_data = data["metier"]
        metier = Metier(
            metier_data["nom"],
            metier_data["domaine"],
            metier_data["bonus_base"]
        )
        # Restaurer niveau et xp
        metier.niveau = metier_data["niveau"]
        metier.xp = metier_data["xp"]
        metier.xp_max = metier_data["xp_max"]

        personnage = cls(data["nom"], metier, pv_max=data["pv_max"])
        personnage.pv = data["pv"]
        personnage.inventaire = data["inventaire"]
        personnage.stats = personnage._calculer_stats()
        return personnage

    def __str__(self):
        return (f"{self.nom} (Niv {self.niveau}, Métier : {self.metier.nom}) - "
                f"PV: {self.pv}/{self.pv_max}, Stats: {self.stats}")