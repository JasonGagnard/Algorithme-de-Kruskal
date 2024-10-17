from implementations.implementation1 import Kruskal
from visualisations.visualisation import visualiser_kruskal
from implementations.implementation2 import Kruskal_N2
from visualisations.visualisation2 import visualiser_kruskal

def afficher_menu():
    print("Menu :")
    print("1 - Kruskal en O(n)")
    print("2 - Graphique de Kruskal en O(n)")
    print("3 - Kruskal en O(N^2)")
    print("4 - Graphique de Kruskal en O(N^2)")
    print("5 - Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Veuillez choisir une option (1-5) : ")

        if choix == '1':
            Kruskal
        elif choix == '2':
            visualiser_kruskal()
        elif choix == '3':
            Kruskal_N2()
        elif choix == '4':
            visualiser_kruskal()
        elif choix == '5':
            print("Quitter le programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
