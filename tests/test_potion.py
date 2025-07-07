from src.potion import Potion

class CibleFictive:
    def __init__(self):
        self.nom = "Testeur"
        self.vie = 50
        self.mana = 10

def test_potion_vie():
    cible = CibleFictive()
    potion = Potion("Potion de soin", "vie", 20)
    potion.utiliser(cible)
    assert cible.vie == 70

def test_potion_mana():
    cible = CibleFictive()
    potion = Potion("Potion de mana", "mana", 15)
    potion.utiliser(cible)
    assert cible.mana == 25

def test_potion_effet_inconnu():
    cible = CibleFictive()
    potion = Potion("Potion étrange", "chance", 10)
    try:
        potion.utiliser(cible)
        assert False  # ne doit pas atteindre cette ligne
    except ValueError:
        assert True
