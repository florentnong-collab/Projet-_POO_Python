"""
Module equipe
--------------
Equipe contient une liste de Joueur et un Entraineur : c'est la relation
d'AGRÉGATION du projet (les joueurs et l'entraîneur existent indépendamment
de l'équipe ; l'équipe ne fait que les rassembler, ils peuvent changer
d'équipe ou exister sans elle).
"""

from typing import List, Optional

from joueur import Joueur
from entraineur import Entraineur


class Equipe:
    """Une équipe de la NBA (ex: Chicago Bulls)."""

    def __init__(self, nom: str, ville: str, entraineur: Optional[Entraineur] = None):
        self.nom = nom
        self.ville = ville
        self.entraineur = entraineur          # agrégation : un Entraineur existant est rattaché
        self.joueurs: List[Joueur] = []        # agrégation : liste de Joueur existants
        self.victoires = 0
        self.defaites = 0

    def ajouter_joueur(self, joueur: Joueur):
        if joueur not in self.joueurs:
            self.joueurs.append(joueur)

    def retirer_joueur(self, joueur: Joueur):
        if joueur in self.joueurs:
            self.joueurs.remove(joueur)

    def definir_entraineur(self, entraineur: Entraineur):
        self.entraineur = entraineur

    def enregistrer_victoire(self):
        self.victoires += 1

    def enregistrer_defaite(self):
        self.defaites += 1

    def bilan(self) -> str:
        return f"{self.victoires}V - {self.defaites}D"

    def meilleur_marqueur(self) -> Optional[Joueur]:
        if not self.joueurs:
            return None
        return max(self.joueurs, key=lambda j: j.statistique.moyenne_points)

    def __str__(self) -> str:
        coach = self.entraineur.nom_complet if self.entraineur else "Aucun"
        return (f"{self.nom} ({self.ville}) - {self.bilan()} - "
                f"{len(self.joueurs)} joueurs - Coach: {coach}")
