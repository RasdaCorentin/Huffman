class Noeud:
    """
    Un nœud de l’arbre de Huffman.

    Attributs :
    - symbole : caractère (None si nœud interne)
    - freq    : fréquence cumulée
    - gauche  : fils gauche
    - droit   : fils droit
    - parent  : nœud parent (optionnel mais pratique)
    """

    def __init__(self, freq, symbole=None):
        self.freq = freq
        self.symbole = symbole
        self.gauche = None
        self.droit = None
        self.parent = None

def text2freq(text):
    """
    1. Parcourir le texte
    2. Compter le nombre d’apparitions de chaque symbole
    3. Créer une liste de tuples :
       - (symbole, fréquence)
    4. Retourner cette liste
    """

def freq2noeud(liste):
    """
    Construit l’arbre de Huffman.

    1. Transformer chaque (symbole, fréquence) en nœud feuille
    2. Tant qu’il reste plus d’un nœud :
       2.1 Sélectionner les deux nœuds de plus faible fréquence
       2.2 Créer un nouveau nœud parent avec :
           - freq = somme des deux fréquences
           - symbole = None
       2.3 Assigner les deux nœuds comme fils gauche et droit
       2.4 Mettre à jour leurs parents
       2.5 Retirer les deux nœuds de la liste
       2.6 Insérer le nœud parent dans la liste
    3. Retourner le dernier nœud : la racine de l’arbre
    """
def arbre2table(noeud, prefix="", table=None):
    """
    Construit la table de codage Huffman.

    1. Parcourir récursivement l’arbre
    2. À chaque descente :
       - gauche  → ajouter '0'
       - droite  → ajouter '1'
    3. Quand on atteint une feuille :
       - associer symbole → prefix
    4. Retourner la table
    """

def huffcode(table, text):
    """
    Encode un texte avec une table de Huffman.

    1. Pour chaque symbole dans le texte :
    2. Récupérer son code binaire dans la table
    3. Concaténer les bits
    4. Retourner la chaîne binaire finale
    """

