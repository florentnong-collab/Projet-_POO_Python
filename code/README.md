# 🏀 Logiciel d'analyse de données NBA

Projet réalisé dans le cadre du cours de Programmation Orientée Objet (POO)/Python/Master 1 IFOAD — Dr Delwende D. A. Sawadogo.

## DescriptionS

Logiciel permettant à un manager d'équipe NBA de gérer et d'analyser les données de son
équipe : liste des équipes et des joueurs, résultats des matchs, informations et
statistiques d'un joueur, ajout de nouveaux joueurs, classement de la ligue.

## Structure du projet

```
code/
├── main.py          # Programme principal (démo + menu interactif)
├── personne.py       # Classe Personne (classe mère)
├── joueur.py          # Classe Joueur (hérite de Personne)
├── entraineur.py      # Classe Entraineur (hérite de Personne)
├── statistique.py     # Classe Statistique (composée dans Joueur)
├── equipe.py           # Classe Equipe (agrège Joueur et Entraineur)
├── match.py             # Classe Match (associe deux Equipe)
└── ligue.py               # Classe Ligue (agrège Equipe et Match)
```

## Modèle objet

| Classe | Rôle |
|---|---|
| `Personne` | Classe mère : nom, prénom, nationalité, date de naissance |
| `Joueur` | Hérite de `Personne` ; possède une `Statistique` (composition) |
| `Entraineur` | Hérite de `Personne` |
| `Statistique` | Statistiques cumulées d'un joueur (points, passes, rebonds, minutes) |
| `Equipe` | Agrège une liste de `Joueur` et un `Entraineur` |
| `Match` | Associe deux `Equipe` existantes (association) |
| `Ligue` | Agrège les `Equipe` et les `Match` de la compétition |

- **Héritage** : `Joueur` et `Entraineur` héritent de `Personne`.
- **Association** : `Match` référence deux `Equipe` sans les posséder.
- **Agrégation** : `Equipe` rassemble des `Joueur` (et un `Entraineur`) qui peuvent
  exister indépendamment d'elle ; `Ligue` rassemble des `Equipe`.
- **Composition** : chaque `Joueur` crée et possède sa propre `Statistique`, qui n'a
  pas de sens en dehors de lui.

## Lancer le projet

```bash
cd code
python3 main.py
```

Le programme affiche d'abord une démonstration automatique (équipes, joueurs,
statistiques, matchs, classement), puis propose un menu interactif pour explorer
les données ou ajouter un nouveau joueur.

## Auteurs

- Florent Nonguierma
- Aboubacary Sawadogo