"""
Module ligue
-------------
Ligue rassemble toutes les Equipe et tous les Match : agrégation également,
au niveau supérieur du système.
"""

from typing import List, Optional

from equipe import Equipe
from match import Match


class Ligue:
    """Représente la ligue NBA dans son ensemble : gère équipes et calendrier."""

    def __init__(self, nom: str = "NBA"):
        self.nom = nom
        self.equipes: List[Equipe] = []
        self.matchs: List[Match] = []

    def ajouter_equipe(self, equipe: Equipe):
        if equipe not in self.equipes:
            self.equipes.append(equipe)

    def trouver_equipe(self, nom: str) -> Optional[Equipe]:
        for equipe in self.equipes:
            if equipe.nom.lower() == nom.lower():
                return equipe
        return None

    def programmer_match(self, match: Match):
        self.matchs.append(match)

    def classement(self) -> List[Equipe]:
        return sorted(self.equipes, key=lambda e: e.victoires - e.defaites, reverse=True)

    def afficher_classement(self):
        print(f"\n=== Classement {self.nom} ===")
        for rang, equipe in enumerate(self.classement(), start=1):
            print(f"{rang}. {equipe}")

    def __str__(self) -> str:
        return f"Ligue {self.nom} - {len(self.equipes)} équipes - {len(self.matchs)} matchs"
