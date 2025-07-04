import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from monstre import Monstre
from personnage import Personnage

def test_monstre_attaque_personnage():
    gobelin = Monstre("Gobelin", niveau=1)
    hero = Personnage("Kael", "Guerrier")
    hero.defense = 0  # Ajoute cette ligne
    vie_initiale = hero.vie
    gobelin.attaquer(hero)
    assert hero.vie < vie_initiale

def test_monstre_subit_degats():
    gobelin = Monstre("Gobelin")
    vie_avant = gobelin.vie
    gobelin.subir_degats(10)
    assert gobelin.vie < vie_avant