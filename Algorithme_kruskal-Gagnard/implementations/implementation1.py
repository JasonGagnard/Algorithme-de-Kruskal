from graphviz import Graph
import timeit

class EnsembleDisjoint:
    """
    cette classe sert à gérer les ensembles disjoints. Deux éléments sont considérés dans le même ensemble quand ils ont le même parent.
    """
    def __init__(self, N):
        self.parent = {}
        for i in range(N):
            self.parent[i] = i
#Fonction qui permet de retrouver le parent le plus lointain
    def getparent(self, k):
        if self.parent[k] == k:
            return k
        return self.getparent(self.parent[k])
# Union de deux ensembles jusque là disjoints
    def Union(self, a, b):
        x = self.getparent(a)
        y = self.getparent(b)
        self.parent[x] = y

def Kruskal(arcs, nombre_sommets):
    """
    Construction de l'arbre couvrant minimum à l'aide de l'algorithme de kruskal : le nombre de sommets, et les arretes (début,fin,longueur)
    """
    Arbre_minimum = []
    ed = EnsembleDisjoint(nombre_sommets)
    arcs_tries = sorted(arcs, key=lambda x: x[2])

    for arc in arcs_tries:
        src, dest, weight = arc
        x = ed.getparent(src)
        y = ed.getparent(dest)

        if x != y:
            Arbre_minimum.append((src, dest, weight))
            ed.Union(x, y)

        if len(Arbre_minimum) == nombre_sommets - 1:
            break

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

    nombre_repetitions = 1000
    temps_moyen = timeit.timeit(lambda: Kruskal(arcs, nombre_sommets), number=nombre_repetitions) / nombre_repetitions

    Arbre_minimum = Kruskal(arcs, nombre_sommets)
    print("Arbre couvrant minimum:", Arbre_minimum)
    print("Temps d'exécution moyen de l'algorithme de Kruskal sur {} répétitions : {:.8f} secondes".format(nombre_repetitions, temps_moyen))

    