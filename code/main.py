"""
Programme principal
--------------------
Logiciel d'analyse de données NBA.

Démontre l'utilisation des classes Personne, Joueur, Entraineur, Statistique,
Equipe, Match et Ligue :
- création d'équipes et de joueurs
- ajout d'un joueur à une équipe
- saisie de statistiques de match pour un joueur
- programmation et résultat de matchs
- affichage du classement de la ligue
"""

from datetime import date

from entraineur import Entraineur
from joueur import Joueur
from equipe import Equipe
from match import Match
from ligue import Ligue


def creer_donnees_demo() -> Ligue:
    ligue = Ligue("NBA")

    # --- Entraîneurs ---
    coach_bulls = Entraineur("Donovan", "Billy", "USA", date(1968, 4, 30), annees_experience=10)
    coach_celtics = Entraineur("Mazzulla", "Joe", "USA", date(1988, 3, 4), annees_experience=3)

    # --- Équipes ---
    bulls = Equipe("Bulls", "Chicago", coach_bulls)
    celtics = Equipe("Celtics", "Boston", coach_celtics)
    ligue.ajouter_equipe(bulls)
    ligue.ajouter_equipe(celtics)

    # --- Joueurs ---
    j1 = Joueur("LaVine", "Zach", "USA", date(1995, 3, 10), "Arriere", 8, date(2014, 6, 1))
    j2 = Joueur("Vucevic", "Nikola", "Monténégro", date(1990, 10, 24), "Pivot", 9, date(2011, 6, 1))
    j3 = Joueur("Tatum", "Jayson", "USA", date(1998, 3, 3), "Ailier", 0, date(2017, 6, 1))
    j4 = Joueur("Brown", "Jaylen", "USA", date(1996, 10, 24), "Arriere", 7, date(2016, 6, 1))

    bulls.ajouter_joueur(j1)
    bulls.ajouter_joueur(j2)
    celtics.ajouter_joueur(j3)
    celtics.ajouter_joueur(j4)

    # --- Statistiques de quelques matchs (points, passes, rebonds, minutes) ---
    j1.ajouter_performance(points=27, passes=4, rebonds=5, minutes=34.5)
    j1.ajouter_performance(points=19, passes=6, rebonds=3, minutes=31.0)
    j2.ajouter_performance(points=18, passes=3, rebonds=11, minutes=30.2)
    j3.ajouter_performance(points=30, passes=5, rebonds=8, minutes=36.0)
    j3.ajouter_performance(points=24, passes=7, rebonds=6, minutes=35.1)
    j4.ajouter_performance(points=22, passes=4, rebonds=5, minutes=33.4)

    # --- Un match programmé puis joué ---
    match1 = Match(bulls, celtics, date(2026, 1, 15))
    ligue.programmer_match(match1)
    match1.enregistrer_resultat(score_domicile=101, score_exterieur=108)

    match2 = Match(celtics, bulls, date(2026, 2, 2))
    ligue.programmer_match(match2)
    match2.enregistrer_resultat(score_domicile=115, score_exterieur=110)

    return ligue


def afficher_details_equipe(equipe: Equipe):
    print(f"\n--- {equipe.nom} ---")
    print(equipe)
    print("Joueurs :")
    for joueur in equipe.joueurs:
        print(f"  - {joueur}")
    meilleur = equipe.meilleur_marqueur()
    if meilleur:
        print(f"Meilleur marqueur : {meilleur.nom_complet} "
              f"({meilleur.statistique.moyenne_points} pts/match)")


def menu():
    ligue = creer_donnees_demo()

    actions = {
        "1": ("Afficher toutes les équipes", lambda: [afficher_details_equipe(e) for e in ligue.equipes]),
        "2": ("Afficher le classement de la ligue", ligue.afficher_classement),
        "3": ("Afficher l'historique des matchs", lambda: [print(m) for m in ligue.matchs]),
        "4": ("Ajouter un nouveau joueur à une équipe", lambda: ajouter_nouveau_joueur(ligue)),
        "0": ("Quitter", None),
    }

    while True:
        print("\n===== Logiciel d'analyse de données NBA =====")
        for cle, (libelle, _) in actions.items():
            print(f"{cle}. {libelle}")
        choix = input("Votre choix : ").strip()

        if choix == "0":
            print("Au revoir !")
            break
        if choix in actions:
            actions[choix][1]()
        else:
            print("Choix invalide.")


def ajouter_nouveau_joueur(ligue: Ligue):
    nom_equipe = input("Nom de l'équipe : ").strip()
    equipe = ligue.trouver_equipe(nom_equipe)
    if not equipe:
        print("Équipe introuvable.")
        return
    nom = input("Nom du joueur : ").strip()
    prenom = input("Prénom du joueur : ").strip()
    poste = input(f"Poste ({', '.join(Joueur.POSTES_VALIDES)}) : ").strip()
    try:
        numero = int(input("Numéro de maillot : ").strip())
        annee_naissance = int(input("Année de naissance : ").strip())
        annee_debut = int(input("Année de début en NBA : ").strip())
        nouveau_joueur = Joueur(nom, prenom, "N/A", date(annee_naissance, 1, 1),
                                 poste, numero, date(annee_debut, 1, 1))
        equipe.ajouter_joueur(nouveau_joueur)
        print(f"{nouveau_joueur.nom_complet} a été ajouté à {equipe.nom} !")
    except ValueError as erreur:
        print(f"Erreur de saisie : {erreur}")


if __name__ == "__main__":
    # Démo automatique non-interactive pour illustrer le fonctionnement,
    # puis menu interactif optionnel.
    ligue_demo = creer_donnees_demo()
    for equipe in ligue_demo.equipes:
        afficher_details_equipe(equipe)
    ligue_demo.afficher_classement()
    print("\nHistorique des matchs :")
    for m in ligue_demo.matchs:
        print(m)

    print("\n(Lancez le menu interactif ci-dessous, Ctrl+C pour quitter à tout moment)")
    try:
        menu()
    except KeyboardInterrupt:
        print("\nAu revoir !")
