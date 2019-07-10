class dictionnaireOrdonne:
    def __init__(self, base = {}, **donnees):
        self._clefs = []
        self._valeurs = []
        if type(base) not in (dict, dictionnaireOrdonne):
            raise TypeError("le type attendu est dict on dictionnaireOrdonne")
        for clef in base:
            self[clef] = base[clef]

        for clef in donnees:
            self[clef] = donnees[clef]
