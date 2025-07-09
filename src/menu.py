import json

def charger_metiers(fichier="data/metiers.json"):
    with open(fichier, encoding="utf-8") as f:
        data = json.load(f)
    return data