"""
Module joueur
--------------
Joueur hérite de Personne (héritage) et possède sa propre Statistique
(composition).
"""

from datetime import date

from personne import Personne
from statistique import Statistique


class Joueur(Personne):
    """Un joueur de NBA."""

    POSTES_VALIDES = {"Meneur", "Arriere", "Ailier", "Ailier fort", "Pivot"}

    def __init__(self, nom: str, prenom: str, nationalite: str, date_naissance: date,
                 poste: str, numero_maillot: int, date_debut_nba: date):
        super().__init__(nom, prenom, nationalite, date_naissance)
        if poste not in self.POSTES_VALIDES:
            raise ValueError(f"Poste invalide: {poste}")
        self.poste = poste
        self.numero_maillot = numero_maillot
        self.date_debut_nba = date_debut_nba
        # Composition : la Statistique n'existe que via le Joueur qui la possède
        self.statistique = Statistique()

    def ajouter_performance(self, points: int, passes: int, rebonds: int, minutes: float):
        self.statistique.ajouter_match(points, passes, rebonds, minutes)

    def annees_experience(self) -> int:
        return date.today().year - self.date_debut_nba.year

    def __str__(self) -> str:
        return (f"#{self.numero_maillot} {self.nom_complet} ({self.poste}) - "
                f"{self.annees_experience()} ans d'exp. NBA - {self.statistique}")
