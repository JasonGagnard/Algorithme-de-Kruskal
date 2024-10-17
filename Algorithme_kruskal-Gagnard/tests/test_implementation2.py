import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation2 import Kruskal_N2

def test_kruskal_N2_basic_case():
    """
    Test de base pour la fonction Kruskal_N2 en O(N^2).
    """
    arcs = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]
    nombre_sommets = 7
    expected_result = [(0, 3, 5), (3, 5, 6), (2, 4, 5), (0, 1, 7), (1, 4, 7), (4, 6, 9)]

    result = Kruskal_N2(arcs, nombre_sommets)
    assert sorted(result) == sorted(expected_result), f"Expected {expected_result}, but got {result}"


def test_kruskal_N2_empty():
    """
    Test pour Kruskal_N2 avec un graphe vide.
    """
    arcs = []
    nombre_sommets = 0
    expected_result = []
    
    result = Kruskal_N2(arcs, nombre_sommets)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_kruskal_N2_large_input():
    """
    Test de performance pour Kruskal_N2 en O(N^2) sur une entrée plus grande.
    """
    arcs = [(i, i + 1, i + 2) for i in range(100)]
    nombre_sommets = 101
    
    result = Kruskal_N2(arcs, nombre_sommets)
    assert len(result) == nombre_sommets - 1, "Le nombre d'arêtes dans l'arbre couvrant est incorrect."
