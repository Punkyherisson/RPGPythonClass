from src.personnage import Personnage

def test_attaque_basique():
    hero = Personnage("Kael", "Guerrier")
    gobelin = Personnage("Gobelin", "Monstre")
    vie_initiale = gobelin.vie
    hero.attaquer(gobelin)
    assert gobelin.vie < vie_initiale

def test_gain_xp_et_niveau():
    h = Personnage("Kael", "Guerrier")
    niveau_initial = h.niveau
    h.gagner_xp(150)
    assert h.niveau > niveau_initial

def test_personnage_meurt():
    h = Personnage("Kael", "Guerrier")
    h.vie = 5
    h.subir_degats(10)
    assert h.est_vivant() == False

def test_defense_reduit_degats():
    h = Personnage("Kael", "Guerrier")
    h.defense = 5
    h.vie = 100
    h.subir_degats(10)
    assert h.vie >= 90