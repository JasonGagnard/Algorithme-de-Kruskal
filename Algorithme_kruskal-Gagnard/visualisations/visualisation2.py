from graphviz import Graph
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation2 import Kruskal_N2
def visualiser_kruskal(arcs, Arbre_minimum, nombre_sommets):
    # Créer un graphe non dirigé
    dot = Graph(comment='Graphe de Kruskal')
    
    # Ajouter tous les sommets
    for i in range(nombre_sommets):
        dot.node(str(i))
    
    # Ajouter tous les arcs
    for arc in arcs:
        start, end, weight = arc
        if (start, end, weight) in Arbre_minimum or (end, start, weight) in Arbre_minimum:
            # Arc dans l'arbre couvrant minimum
            dot.edge(str(start), str(end), label=str(weight), color='red', penwidth='2')
        else:
            # Arc non inclus dans l'arbre couvrant minimum
            dot.edge(str(start), str(end), label=str(weight), style='dashed')
    
    # Générer et sauvegarder le graphe
    dot.render('kruskal_graph', view=True, format='png')

if __name__ == '__main__':
    # Liste des arcs (début, fin, longueur)
    arcs = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]

    nombre_sommets = 7

    Arbre_minimum = Kruskal_N2(arcs, nombre_sommets)
    print("Arbre couvrant minimum:", Arbre_minimum)

    visualiser_kruskal(arcs, Arbre_minimum, nombre_sommets)