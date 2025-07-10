import pytest
from src.metier import Metier

def test_creation_metier():
    m = Metier("Guerrier", "Spécialiste du combat au corps à corps",{})
    assert m.nom == "Guerrier"
    assert m.niveau == 1
    assert m.xp == 0

def test_gain_xp_et_monte_niveau():
    m = Metier("Mage", "Maître de la magie", {})
    # suite du test...

def test_max_niveau():
    m = Metier("Barde", "Chanteur magique", {})
    # suite du test...

def test_domaine_correct():
    m = Metier("Barbare", "combat", {"force": 7, "vitesse": -1})
    assert m.domaine == "combat"
    assert m.bonus["force"] == 7