import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.arme import Arme  



def test_creation_arme():
    epee = Arme("Épée en fer", degats=10)
    assert epee.nom == "Épée en fer"
    assert epee.degats == 10
    assert epee.type_arme == "tranchant"
    assert epee.rarete == "commune"

def test_description():
    arc = Arme("Arc elfique", 15, type_arme="perforant", rarete="rare")
    desc = arc.description()
    assert "Arc elfique" in desc
    assert "Dégâts : 15" in desc
    assert "rare" in desc

def test_amelioration():
    hache = Arme("Hache naine", 12)
    hache.ameliorer(3)
    assert hache.degats == 15