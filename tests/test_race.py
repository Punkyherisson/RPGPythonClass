# tests/test_race.py
from race import Race

def test_creation_race():
    race = Race("Elfe", {"intelligence": +2, "force": -1})
    assert race.nom == "Elfe"
    assert race.get_modificateur("intelligence") == 2
    assert race.get_modificateur("force") == -1
    assert race.get_modificateur("charisme") == 0

def test_str_race():
    race = Race("Nain", {"constitution": +2, "charisme": -1})
    assert str(race) == "Nain (constitution: +2, charisme: -1)"