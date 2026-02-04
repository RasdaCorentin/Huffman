import sys
from huffman import Huffman

def lancer_test():
    """
    Récupérer l'argument, compresser les données et sauvegarder le résultat sur disque.
    """
    # 1. Lire l'argument passé au script (Exemple : python test.py "STRUCTURE")
    if len(sys.argv) < 2:
        print("Erreur : Aucun argument fourni.")
        return
    
    texte_entree = sys.argv[1]
    
    # 2. Utiliser la logique de Huffman
    logiciel = Huffman()
    flux_binaire = logiciel.compresser(texte_entree)
    
    # 3. Sauvegarder dans un fichier (Logique externe au moteur de compression)
    nom_fichier = "resultat_compression.txt"
    try:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(flux_binaire)
        print(f"Succès : Le texte '{texte_entree}' a été compressé dans '{nom_fichier}'.")
    except IOError as e:
        print(f"Erreur lors de la sauvegarde : {e}")

if __name__ == "__main__":
    lancer_test()