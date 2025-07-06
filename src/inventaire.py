class Inventaire:
    def __init__(self):
        self.objets = []

    def ajouter_objet(self, objet):
        self.objets.append(objet)

    def retirer_objet(self, objet):
        if objet in self.objets:
            self.objets.remove(objet)
            return True
        return False

    def contient(self, objet):
        return objet in self.objets

    def afficher(self):
        if not self.objets:
            return "Inventaire vide."
        return "\n".join([str(objet) for objet in self.objets])