# 🧙 RPGPythonClass

Bienvenue dans **RPGPythonClass**, un projet Python orienté objet pour simuler un RPG (jeu de rôle) classique inspiré de *Wizardry II* et *Bard's Tale*.

## 🎯 Objectifs

- Créer un backend Python pour un RPG textuel
- Simuler des combats entre héros et monstres
- Gérer des objets : armes, potions, inventaire
- Relier plus tard à une interface graphique HTML/JavaScript

## 📦 Structure du projet

```
RPGPythonClass/
│
├── src/                      # Code source principal
│   ├── personnage.py         # Classe Personnage
│   ├── monstre.py            # Classe Monstre
│   ├── arme.py               # Classe Arme
│   ├── potion.py             # Classe Potion
│   ├── inventaire.py         # Classe Inventaire
│
├── tests/                    # Tests unitaires Pytest
│   ├── test_personnage.py
│   ├── test_monstre.py
│   ├── test_arme.py
│   ├── test_potion.py
│   ├── test_inventaire.py
│
├── README.md                 # Ce fichier
└── requirements.txt          # (optionnel) Dépendances du projet
```

## 🚀 Démarrer le projet

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/Punkyherisson/RPGPythonClass.git
   cd RPGPythonClass
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé) :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate sous Windows
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer les tests :**

   ```bash
   pytest
   ```

## 🧪 Technologies utilisées

- Python 3.12
- Pytest pour les tests unitaires
- VSCode pour l’édition
- Git/GitHub pour la gestion de versions

## 📌 À venir

- Interface graphique en HTML/JS
- Donjons, équipements, magie
- Système de sauvegarde/chargement JSON
- Intelligence des monstres

---

© 2025 PunkyHérisson – Projet éducatif et passionné 🎮