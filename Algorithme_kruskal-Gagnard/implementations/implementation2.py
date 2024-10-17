from graphviz import Graph

class EnsembleDisjoint:
    """
    Classe pour gérer les ensembles disjoints. Deux éléments sont dans le même ensemble s'ils ont le même parent.
    """
    def __init__(self, N):
        self.parent = {}
        for i in range(N):
            self.parent[i] = i

    def getparent(self, k):
        if self.parent[k] == k:
            return k
        return self.getparent(self.parent[k])

    def Union(self, a, b):
        x = self.getparent(a)
        y = self.getparent(b)
        self.parent[x] = y

def Kruskal_N2(arcs, nombre_sommets):
    """
    Algorithme de Kruskal avec une complexité O(N^2) pour trouver l'arbre couvrant minimum.
    """
    Arbre_minimum = []
    ed = EnsembleDisjoint(nombre_sommets)
    
    # Parcourir toutes les arêtes et les traiter dans un ordre fixe
    while len(Arbre_minimum) < nombre_sommets - 1:
        # Chercher l'arête minimale non encore traitée
        min_arc = None
        min_weight = float('inf')
        for arc in arcs:
            src, dest, weight = arc
            x = ed.getparent(src)
            y = ed.getparent(dest)

            # Si elle connecte deux composantes différentes et est la plus petite trouvée
            if x != y and weight < min_weight:
                min_weight = weight
                min_arc = arc

        if min_arc:
            src, dest, weight = min_arc
            Arbre_minimum.append((src, dest, weight))
            ed.Union(src, dest)

    return Arbre_minimum

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

    
