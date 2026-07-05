"""
Module match
-------------
Match relie deux objets Equipe déjà existants : c'est la relation
d'ASSOCIATION du projet (un Match ne "possède" pas les équipes, il se
contente de les référencer ; les équipes existent avant, pendant et après
le match).
"""

from datetime import date

from equipe import Equipe


class Match:
    """Un match opposant deux équipes à une date donnée."""

    def __init__(self, equipe_domicile: Equipe, equipe_exterieur: Equipe, date_match: date):
        self.equipe_domicile = equipe_domicile      # association
        self.equipe_exterieur = equipe_exterieur     # association
        self.date_match = date_match
        self.score_domicile: int = 0
        self.score_exterieur: int = 0
        self.joue: bool = False

    def enregistrer_resultat(self, score_domicile: int, score_exterieur: int):
        self.score_domicile = score_domicile
        self.score_exterieur = score_exterieur
        self.joue = True

        if score_domicile > score_exterieur:
            self.equipe_domicile.enregistrer_victoire()
            self.equipe_exterieur.enregistrer_defaite()
        elif score_exterieur > score_domicile:
            self.equipe_exterieur.enregistrer_victoire()
            self.equipe_domicile.enregistrer_defaite()

    def vainqueur(self):
        if not self.joue or self.score_domicile == self.score_exterieur:
            return None
        return (self.equipe_domicile if self.score_domicile > self.score_exterieur
                else self.equipe_exterieur)

    def __str__(self) -> str:
        if not self.joue:
            return f"{self.date_match} : {self.equipe_domicile.nom} vs {self.equipe_exterieur.nom} (à jouer)"
        return (f"{self.date_match} : {self.equipe_domicile.nom} {self.score_domicile} - "
                f"{self.score_exterieur} {self.equipe_exterieur.nom}")
