"""
Module entraineur
------------------
Entraineur hérite lui aussi de Personne (deuxième branche de l'héritage).
"""

from datetime import date

from personne import Personne


class Entraineur(Personne):
    """Entraîneur principal d'une équipe."""

    def __init__(self, nom: str, prenom: str, nationalite: str, date_naissance: date,
                 annees_experience: int):
        super().__init__(nom, prenom, nationalite, date_naissance)
        self.annees_experience = annees_experience

    def __str__(self) -> str:
        return f"Coach {self.nom_complet} ({self.annees_experience} ans d'expérience)"
