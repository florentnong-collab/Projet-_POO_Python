"""
Module statistique
-------------------
Statistique est un objet créé et détruit avec le Joueur auquel il appartient :
c'est la relation de COMPOSITION du projet (sans le joueur, ses statistiques
n'ont aucune raison d'exister).
"""


class Statistique:
    """Statistiques cumulées d'un joueur match après match."""

    def __init__(self):
        self.matchs_joues = 0
        self.total_points = 0
        self.total_passes = 0
        self.total_rebonds = 0
        self.total_minutes = 0.0

    def ajouter_match(self, points: int, passes: int, rebonds: int, minutes: float):
        """Enregistre les statistiques d'un match supplémentaire."""
        self.matchs_joues += 1
        self.total_points += points
        self.total_passes += passes
        self.total_rebonds += rebonds
        self.total_minutes += minutes

    def _moyenne(self, total) -> float:
        return round(total / self.matchs_joues, 1) if self.matchs_joues else 0.0

    @property
    def moyenne_points(self) -> float:
        return self._moyenne(self.total_points)

    @property
    def moyenne_passes(self) -> float:
        return self._moyenne(self.total_passes)

    @property
    def moyenne_rebonds(self) -> float:
        return self._moyenne(self.total_rebonds)

    @property
    def moyenne_minutes(self) -> float:
        return self._moyenne(self.total_minutes)

    def __str__(self) -> str:
        return (f"{self.matchs_joues} matchs | "
                f"{self.moyenne_points} pts, {self.moyenne_passes} pd, "
                f"{self.moyenne_rebonds} rbd (moyennes/match)")
