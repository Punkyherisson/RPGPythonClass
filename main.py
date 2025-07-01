from src.personnage import Personnage

def main():
    hero = Personnage("Kael", "Guerrier")
    gobelin = Personnage("Gobelin", "Monstre")

    print(f"{hero.nom} attaque {gobelin.nom}")
    hero.attaquer(gobelin)
    print(f"PV de {gobelin.nom} après l'attaque : {gobelin.vie}")

if __name__ == "__main__":
    main()