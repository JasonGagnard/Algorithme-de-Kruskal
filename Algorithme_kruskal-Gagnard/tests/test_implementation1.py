# test_implementation1.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation1 import Kruskal


def test_kruskal_basic_case():
    """
    Test de base pour la fonction Kruskal en O(N).
    """
    arcs = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]
    nombre_sommets = 7
    expected_result = [(0, 3, 5), (3, 5, 6), (2, 4, 5), (0, 1, 7), (1, 4, 7), (4, 6, 9)]

    result = Kruskal(arcs, nombre_sommets)
    assert sorted(result) == sorted(expected_result), f"Expected {expected_result}, but got {result}"



def test_kruskal_empty():
    """
    Test pour Kruskal avec un graphe vide.
    """
    arcs = []
    nombre_sommets = 0
    expected_result = []
    
    result = Kruskal(arcs, nombre_sommets)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_kruskal_large_input():
    """
    Test de performance de Kruskal en O(N) sur une entrée plus grande.
    """
    arcs = [(i, i + 1, i + 2) for i in range(1000)]
    nombre_sommets = 1001
    
    result = Kruskal(arcs, nombre_sommets)
    assert len(result) == nombre_sommets - 1, "Le nombre d'arêtes dans l'arbre couvrant est incorrect."
