import random
from src.monstre import Monstre
from metier import Metier      # Ta classe Metier existante
from personnage import Personnage  # La nouvelle classe Personnage

def test_combat():
    # Création métiers
    guerrier = Metier("Guerrier", "combat", {"force": 5, "defense": 3})
    mage = Metier("Mage", "combat", {"intelligence": 7, "mana": 10})

    # Création personnages
    hero = Personnage("Arthur", guerrier)
    ennemi = Monstre("Gobelin", niveau=1, pv=50, attaque=8, defense=2)

    print(hero)
    print(ennemi)

    # Combat basique
    while hero.est_vivant() and ennemi.est_vivant():
        hero.attaquer(ennemi)
        if ennemi.est_vivant():
            ennemi.attaquer(hero)
        print()

    if hero.est_vivant():
        print(f"{hero.nom} a vaincu {ennemi.nom} !")
        hero.gagner_xp(50)
    else:
        print(f"{hero.nom} a été vaincu...")

def test_sauvegarde():
    guerrier = Metier("Guerrier", "combat", {"force": 5, "defense": 3})
    hero = Personnage("Lancelot", guerrier)
    hero.inventaire.append("Potion de soin")
    hero.sauvegarder("lancelot.json")

    hero_charge = Personnage.charger("lancelot.json")
    print(hero_charge)

if __name__ == "__main__":
    random.seed(42)  # Pour tests reproductibles
    test_combat()
    print("\n--- Test sauvegarde/chargement ---\n")
    test_sauvegarde()
