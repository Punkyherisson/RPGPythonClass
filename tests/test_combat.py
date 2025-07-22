from groupe import Groupe
from monstre import Monstre
from combat import Combat

def test_combat_initialisation():
    g1 = Groupe("Héros")
    g2 = Groupe("Monstres")
    combat = Combat(g1, g2)
    assert combat.groupe_1.nom == "Héros"
    assert combat.groupe_2.nom == "Monstres"

def test_un_tour_de_combat():
    m1 = Monstre("Guerrier", 1, 20, 5, 2)
    m2 = Monstre("Gobelin", 1, 15, 3, 1)
    g1 = Groupe("Héros", [m1])
    g2 = Groupe("Ennemis", [m2])

    combat = Combat(g1, g2)
    combat.un_tour()

    # Au moins un personnage doit avoir perdu des PV
    assert m1.pv < 20 or m2.pv < 15

def test_combat_termine_et_gagnant():
    m1 = Monstre("Héros", 1, 20, 5, 2)
    m2 = Monstre("Gobelin", 1, 1, 0, 0)  # Faible défense/attaque pour mourir vite
    g1 = Groupe("Héros", [m1])
    g2 = Groupe("Ennemis", [m2])
    combat = Combat(g1, g2)

    while not combat.est_termine():
        combat.un_tour()

    assert combat.gagnant() == "Héros"
