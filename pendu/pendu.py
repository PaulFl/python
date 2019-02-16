import fonctions
import donnees


nom_joueur = fonctions.nom_joueur()
mot = fonctions.choisir_mot()
mot_joueur = "_" * len(mot)
scores = fonctions.recuperer_scores()

essais_restants = donnees.nombre_essais
mot_found = False

while not mot_found and essais_restants > 0:
    lettre_jouee = fonctions.choix_lettre()
    if fonctions.lettre_est_dans_mot(lettre_jouee, mot):
        mot_joueur = fonctions.completer_mot(mot, mot_joueur, lettre_jouee)
        print("La lettre était dans le mot: ")
        print(mot_joueur)
    else:
        essais_restants -= 1
        print("La lettre n'est pas dans le mot")
    if mot_joueur == mot:
        mot_found = True

if mot_found:
    try:
        score_joueur = scores[nom_joueur.upper()]
    except KeyError:
        score_joueur = 0
    score_joueur += essais_restants
    scores[nom_joueur.upper()] = score_joueur
    fonctions.stocker_scores(scores)
    print("Bravo, votre scores est maintennant: {}".format(score_joueur))
else:
    print("Dommage, le mot était '{}'".format(mot))
