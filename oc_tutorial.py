class UnePersonne:
    """classe qui définit une personne"""

    attribut_de_classe = 2

    def __init__(self, nom, prenom, age, adresse):
        """constructeur de la classe"""

        self.prenom  = prenom
        self.nom = nom
        self.age = age
        self._adresse = adresse

    def _get_adresse(self):
        return self._adresse

    def _set_adresse(self, adresse):
        print("en train de déménager")
        self._adresse = adresse

    adresse = property(_get_adresse, _set_adresse)



class Tableau:
    """modélisation d'un tableau"""

    def __init__(self):
        self.contenu = ""

    def ecrire(self, phrase):
        """ajouter une str a la fin du tableau"""
        self.contenu += phrase

    def lire(self):
        """afficher le contenu du tableau"""
        print(self.contenu)

    def effacer(self):
        self.contenu = ""

    def __repr__(self):
        return self.contenu

    def __str__(self):
        return "Contenu: {}".format(self.contenu)
