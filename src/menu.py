from src.metier import Metier
from src.utils import charger_metiers

def choisir_metier():
    metiers = charger_metiers()
    print("Choisissez un métier :")
    for i, m in enumerate(metiers):
        print(f"{i+1}. {m['nom']} - {m['description']}")

    choix = int(input("Numéro du métier : ")) - 1
    metier_choisi = metiers[choix]
    return Metier(metier_choisi["nom"], metier_choisi["description"])