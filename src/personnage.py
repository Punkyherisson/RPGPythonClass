import random
import json
from metier import Metier
from race import Race

class Personnage:
    def __init__(self, nom: str, metier, pv_max=100, race: Race = None):
        self.nom = nom
        self.metier = metier  # instance de Metier
        self.race = race
        self.pv_max = pv_max + (race.get_modificateur("pv_max") if race else 0)
        self.pv = self.pv_max
        self.inventaire = []
        self.xp = 0
        self.niveau = 1
        self.stats = self._calculer_stats()

    def _calculer_stats(self):
        # Stats de base métier
        base_stats = {
            "force": 10,
            "defense": 5,
            "critique": 5,
            "vitesse": 5
        }
        # Ajouter bonus métier
        bonus = self.metier.bonus
        for cle, val in bonus.items():
            base_stats[cle] = base_stats.get(cle, 0) + val

        # Ajouter modificateurs race
        if self.race:
            for cle, val in self.race.modificateurs.items():
                if cle != "pv_max":  # pv_max déjà ajouté à l'init
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
            "inventaire": self.inventaire,
            "race": {
                "nom": self.race.nom if self.race else None,
                "modificateurs": self.race.modificateurs if self.race else {}
            }
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
        metier.niveau = metier_data["niveau"]
        metier.xp = metier_data["xp"]
        metier.xp_max = metier_data["xp_max"]

        race_data = data.get("race")
        race = None
        if race_data and race_data["nom"]:
            race = Race(race_data["nom"], race_data["modificateurs"])

        personnage = cls(data["nom"], metier, pv_max=data["pv_max"], race=race)
        personnage.pv = data["pv"]
        personnage.inventaire = data["inventaire"]
        personnage.stats = personnage._calculer_stats()
        return personnage

    def __str__(self):
        race_str = f" ({self.race.nom})" if self.race else ""
        return (f"{self.nom}{race_str} (Niv {self.niveau}, Métier : {self.metier.nom}) - "
                f"PV: {self.pv}/{self.pv_max}, Stats: {self.stats}")