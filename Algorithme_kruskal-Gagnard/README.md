# Algorithme de Kruskal

## Description

L'algorithme de Kruskal est un algorithme de recherche d'arbre couvrant minimal (ACM) pour un graphe non orienté pondéré. Il est utilisé pour trouver l'arbre couvrant de poids minimal, c'est-à-dire un sous-ensemble des arêtes du graphe qui relie tous les sommets sans former de cycle et dont la somme des poids est minimale.

## Fonctionnement

L'algorithme de Kruskal suit une approche par "greedy" (glouton) pour construire l'arbre couvrant minimal. Il fonctionne de la manière suivante :

1. **Tri des arêtes** : Toutes les arêtes du graphe sont triées par poids croissant.
2. **Sélection des arêtes** : On sélectionne les arêtes, une par une, en commençant par la plus légère, et on les ajoute à l'arbre couvrant si elles ne forment pas de cycle avec les arêtes déjà sélectionnées.
3. **Arrêt** : Le processus continue jusqu'à ce que toutes les arêtes de l'arbre couvrant minimal aient été sélectionnées.

### Détails de l'algorithme :

- On utilise une structure de données appelée *Union-Find* ou *Disjoint Set* pour garder une trace des composants connectés afin d'éviter la formation de cycles.
- Le coût temporel de l'algorithme est principalement déterminé par le tri des arêtes, soit \(O(E \log E)\), où \(E\) est le nombre d'arêtes.

## Utilisation

### Entrée

L'algorithme prend en entrée :
- Un graphe non orienté pondéré \(G = (V, E)\), où \(V\) est l'ensemble des sommets et \(E\) est l'ensemble des arêtes, chaque arête ayant un poids.

### Sortie

La sortie de l'algorithme est un sous-ensemble d'arêtes qui forment l'arbre couvrant minimal.

### Pseudocode

```plaintext
Objectif de l'algorithme : 
L'algorithme de Kruskal vise à trouver l'arbre couvrant le poids minimum dans le graphe . Cela signifie qu'on cherche à connecter tous les sommets du graphe avec un coût total minimal.

Initialisation :
On commence avec un graphe G(V, E), où V est l'ensemble des sommets et E l'ensemble des arêtes.
Chaque arête a un poids associé.

Tri des arêtes :
On trie toutes les arêtes du graphe par ordre croissant de poids.
Structure de données clé : Ensembles disjoints
On utilise une structure d'ensembles disjoints pour détecter efficacement les cycles.
Initialement, chaque sommet est dans son propre ensemble.

Processus principal :
Pour chaque arête (u, v) dans la liste triée des arêtes :
a. On vérifie si u et v appartiennent à des ensembles disjoints.
b. Si oui, on ajoute cette arête à notre solution et on fusionne les ensembles de u et v.
c. Si non, on ignore cette arête car elle formerait un cycle.
Critère d'arrêt :
L'algorithme s'arrête quand on a ajouté (n-1) arêtes, où n est le nombre de sommets. À ce stade, on a un arbre couvrant.

Complexité :
Le tri des arêtes prend O(N log N) temps.
Les opérations sur les ensembles disjoints prennent presque O(1) temps amorti.
La complexité totale est donc O(N log N).


Propriété importante :
L'algorithme de Kruskal est un algorithme glouton. Il fait le meilleur choix local à chaque étape pour atteindre une solution globalement optimale.
Visualisation (optionnelle) :
Pour mieux comprendre le résultat, on peut représenter graphiquement la solution, en mettant en évidence les arêtes sélectionnées pour l'arbre couvrant minimum.
```
### Installation

Pour utiliser ce projet, vous pouvez cloner ce dépôt :

```bash
  git clone https://github.com/JasonGagnard/Algorithme-de-Kruskal
cd Algorithme-de-Kruskal
```
## Exécution
Vous pouvez exécuter le script en Python de la manière suivante :

```bash
  python main.py
```
    