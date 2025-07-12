import pytest
from monstre2 import Monstre

def test_creation_monstre():
    m = Monstre("Loup", 2, 30, 8, 5, loot=["fourrure"], cri="Awooo", type_monstre="bête")
    assert m.nom == "Loup"
    assert m.niveau == 2
    assert m.pv == 30
    assert m.attaque == 8
    assert m.defense == 5
    assert m.loot == ["fourrure"]
    assert m.type_monstre == "bête"
    assert m.cri == "Awooo"

def test_est_vivant_et_subir_degats():
    m = Monstre("Orc", 1, 20, 5, 3)
    assert m.est_vivant()
    degats = m.subir_degats(10)
    assert degats == 7
    assert m.pv == 13
    m.subir_degats(100)
    assert not m.est_vivant()
    assert m.pv == 0

def test_resistances_et_faiblesses():
    m = Monstre("Slime", 1, 15, 3, 2, resistances={"feu": 2}, faiblesses={"glace": 2})
    degats_feu = m.subir_degats(10, type_attaque="feu")    # 10 - (2+2) = 6
    degats_glace = m.subir_degats(10, type_attaque="glace")  # 10 - (2-2) = 10 - 0 = 10
    assert degats_feu == 6
    assert degats_glace == 10

def test_attaque():
    monstre = Monstre("Gobelin", 1, 10, 4, 1)
    cible = Monstre("Héros", 1, 20, 5, 3)
    degats = monstre.attaquer(cible)
    assert degats == max(0, 4 - 3)
    assert cible.pv == 20 - degats

def test_loot():
    m = Monstre("Dragon", 10, 100, 25, 20, loot=["écaille", "or", "potion"])
    assert m.drop_loot() in m.loot

def test_cri(monkeypatch):
    m = Monstre("Corbeau", 1, 5, 1, 1, cri="Croaa!")
    output = []
    monkeypatch.setattr("builtins.print", lambda msg: output.append(msg))
    m.crier()
    assert "Croaa!" in output[0]

def test_comportement():
    m1 = Monstre("Troll", 5, 100, 15, 10, comportement="agressif")
    m2 = Monstre("Rat", 1, 5, 2, 1, comportement="fuyant")
    m3 = Monstre("Serpent", 2, 10, 3, 2, comportement="aléatoire")
    assert m1.comportement_ia() == "attaque"
    assert m2.comportement_ia() == "fuit"
    assert m3.comportement_ia() in ["attaque", "défend", "fuit"]

def test_str():
    m = Monstre("Liche", 7, 80, 18, 12, type_monstre="mort-vivant")
    s = str(m)
    assert "Liche" in s
    assert "niveau 7" in s
    assert "mort-vivant" in s
    assert "PV: 80/80" in s