import donnees
import random as rd
import pickle


def choisir_mot():
    mot = donnees.mots[rd.randrange(len(donnees.mots))]
    return mot


def nom_joueur():
    return input("Quel est ton nom ? ")


def recuperer_scores():
    with open("scores", "rb") as fichier_scores:
        scores_pickler = pickle.Unpickler(fichier_scores)
        try:
            scores = scores_pickler.load()
        except EOFError:
            scores = {}
        return scores


def stocker_scores(scores):
    with open("scores", "wb") as fichier_scores:
        scores_pickler = pickle.Pickler(fichier_scores)
        scores_pickler.dump(scores)


def choix_lettre():
    lettre = ""
    while len(lettre) != 1:
        lettre = input("Choisir une lettre: ")
    return lettre


def lettre_est_dans_mot(lettre, mot: str):
    return mot.find(lettre) != -1


def completer_mot(mot: str, mot_joueur: str, lettre):
    mot_joueur_local = list(mot_joueur)
    for i in range(len(mot)):
        if mot[i] == lettre:
            mot_joueur_local[i] = lettre
    return ''.join(mot_joueur_local)

