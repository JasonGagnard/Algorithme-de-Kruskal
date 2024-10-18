from implementations.implementation1 import Kruskal
from visualisations.visualisation import visualiser_kruskal
from implementations.implementation2 import Kruskal_N2
from visualisations.visualisation2 import visualiser_kruskal as visualiser_kruskal2
import timeit
import time
from memory_profiler import memory_usage

def afficher_menu():
    print("Menu :")
    print("1 - Kruskal en O(n)")
    print("2 - Graphique de Kruskal en O(n)")
    print("3 - Kruskal en O(N^2)")
    print("4 - Graphique de Kruskal en O(N^2)")
    print("5 - Quitter")

def main():
    arcs = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]
    nombre_sommets = 7

    while True:
        afficher_menu()
        choix = input("Veuillez choisir une option (1-5) : ")

        if choix == '1':
            temps_kruskal = timeit.timeit(lambda: Kruskal(arcs, nombre_sommets), number=1000)
            memoire_kruskal = max(memory_usage((Kruskal, (arcs, nombre_sommets))))
            arbre_minimum = Kruskal(arcs, nombre_sommets)
            print("Arbre couvrant minimum:", arbre_minimum)
            print("Temps moyen de Kruskal en O(n) sur 1000 répétitions : {:.8f} secondes".format(temps_kruskal / 100000))
            print("Mémoire maximale utilisée par Kruskal : {:.2f} MiB".format(memoire_kruskal))
        
        elif choix == '2':
            arbre_minimum = Kruskal(arcs, nombre_sommets)
            # Measure max memory usage for visualiser_kruskal
            memoire_visualisation_kruskal = max(memory_usage((visualiser_kruskal, (arcs, arbre_minimum, nombre_sommets))))
            debut = time.time()
            fin = time.time()
            visualiser_kruskal(arcs, arbre_minimum, nombre_sommets)
            
            print("Temps d'exécution de visualiser_kruskal : {:.8f} secondes".format(fin - debut))
            print("Mémoire maximale utilisée par visualiser_kruskal : {:.2f} MiB".format(memoire_visualisation_kruskal))

        elif choix == '3':
            # Measure time and memory usage of Kruskal_N2
            temps_kruskal_n2 = timeit.timeit(lambda: Kruskal_N2(arcs, nombre_sommets), number=100000)
            memoire_kruskal_n2 = max(memory_usage((Kruskal_N2, (arcs, nombre_sommets))))
            arbre_minimum = Kruskal_N2(arcs, nombre_sommets)
            print("Arbre couvrant minimum (O(N^2)):", arbre_minimum)
            print("Temps moyen de Kruskal en O(N^2) sur 1000 répétitions : {:.8f} secondes".format(temps_kruskal_n2 / 100000))
            print("Mémoire maximale utilisée par Kruskal_N2 : {:.2f} MiB".format(memoire_kruskal_n2))

        elif choix == '4':
            arbre_minimum = Kruskal_N2(arcs, nombre_sommets)
            # Measure max memory usage for visualiser_kruskal2
            memoire_visualisation_kruskal2 = max(memory_usage((visualiser_kruskal2, (arcs, arbre_minimum, nombre_sommets))))
            debut = time.time()
            fin = time.time()
            visualiser_kruskal2(arcs, arbre_minimum, nombre_sommets)
            print("Temps d'exécution de visualiser_kruskal : {:.8f} secondes".format(fin - debut))
            print("Mémoire maximale utilisée par visualiser_kruskal2 : {:.2f} MiB".format(memoire_visualisation_kruskal2))

        elif choix == '5':
            print("Quitter le programme.")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
