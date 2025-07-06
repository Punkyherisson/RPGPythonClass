import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.inventaire import Inventaire  # ✅
from src.arme import Arme  # ✅


def test_ajouter_objet():
    inv = Inventaire()
    epee = Arme("Épée courte", 5)
    inv.ajouter_objet(epee)
    assert inv.contient(epee)

def test_retirer_objet():
    inv = Inventaire()
    epee = Arme("Épée courte", 5)
    inv.ajouter_objet(epee)
    assert inv.retirer_objet(epee) == True
    assert not inv.contient(epee)

def test_retirer_objet_inexistant():
    inv = Inventaire()
    epee = Arme("Épée courte", 5)
    assert inv.retirer_objet(epee) == False

def test_afficher_inventaire_vide():
    inv = Inventaire()
    assert inv.afficher() == "Inventaire vide."

def test_afficher_contenu():
    inv = Inventaire()
    arc = Arme("Arc long", 8)
    inv.ajouter_objet(arc)
    output = inv.afficher()
    assert "Arc long" in output