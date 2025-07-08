import pytest
from src.sorts import Sort  # selon le nom de ton fichier

class CibleMock:
    def __init__(self, vie):
        self.vie = vie

    def subir_degats(self, degats):
        self.vie -= degats

def test_sort_offensif_inflige_degats():
    cible = CibleMock(vie=100)
    boule_feu = Sort("Boule de Feu", degats=30, cout_mana=10, type_sort="offensif")
    boule_feu.lancer(cible)
    assert cible.vie == 70

def test_sort_defensif_soigne():
    cible = CibleMock(vie=50)
    soin = Sort("Soin", degats=-20, cout_mana=5, type_sort="defensif")
    soin.lancer(cible)
    assert cible.vie == 70
    