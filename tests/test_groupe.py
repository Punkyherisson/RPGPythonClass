import pytest
from groupe import Groupe
from monstre import Monstre

def test_creation_groupe():
    g = Groupe("Monstres")
    assert g.nom == "Monstres"
    assert len(g) == 0

def test_ajout_membres():
    g = Groupe("Horde")
    m1 = Monstre("Gobelin", 1, 10, 2, 1)
    m2 = Monstre("Orc", 2, 20, 4, 2)
    g.ajouter(m1)
    g.ajouter(m2)
    assert len(g) == 2
    assert m1 in g.membres
    assert m2 in g.membres

def test_retrait_membre():
    g = Groupe("Meute")
    m = Monstre("Loup", 1, 15, 3, 1)
    g.ajouter(m)
    g.retirer(m)
    assert len(g) == 0

def test_vivants_et_est_vivant():
    g = Groupe("Bête")
    m1 = Monstre("Sanglier", 1, 0, 3, 1)  # mort
    m2 = Monstre("Loup", 1, 10, 4, 2)     # vivant
    g.ajouter(m1)
    g.ajouter(m2)
    vivants = g.vivants()
    assert len(vivants) == 1
    assert m2 in vivants
    assert g.est_vivant() is True

def test_str_groupe():
    g = Groupe("Gobelins")
    m = Monstre("Gobelin", 1, 10, 2, 1)
    g.ajouter(m)
    assert "Gobelin" in str(g)