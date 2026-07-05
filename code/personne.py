"""
Module personne
----------------
Définit la classe de base Personne, dont héritent Joueur et Entraineur.
"""

from datetime import date


class Personne:
    """
    Classe mère représentant une personne physique (nom, prénom, nationalité...).
    Joueur et Entraineur en héritent : c'est la relation d'HÉRITAGE du projet.
    """

    def __init__(self, nom: str, prenom: str, nationalite: str, date_naissance: date):
        self.nom = nom
        self.prenom = prenom
        self.nationalite = nationalite
        self.date_naissance = date_naissance

    @property
    def nom_complet(self) -> str:
        return f"{self.prenom} {self.nom}"

    def age(self) -> int:
        aujourd_hui = date.today()
        age = aujourd_hui.year - self.date_naissance.year
        if (aujourd_hui.month, aujourd_hui.day) < (self.date_naissance.month, self.date_naissance.day):
            age -= 1
        return age

    def __str__(self) -> str:
        return f"{self.nom_complet} ({self.nationalite}, {self.age()} ans)"
