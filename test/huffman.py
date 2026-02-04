from collections import Counter


class Noeud:
    """
    Représenter une unité structurelle (nœud interne ou feuille) de l'arbre de Huffman.
    
    Cette classe permet de stocker les informations statistiques et les liens hiérarchiques 
    nécessaires à la navigation bit à bit durant le codage et le décodage.

    Attributs :
    - symbole (char)    : Le caractère stocké dans la feuille (vaut None pour un nœud interne).
    - frequence (int)   : Le poids statistique (nombre d'occurrences ou cumul des enfants).
    - gauche (Noeud)    : Référence vers l'enfant associé au bit '0'.
    - droit (Noeud)     : Référence vers l'enfant associé au bit '1'.
    - parent (Noeud)    : Référence vers le nœud supérieur (facilite la remontée de l'arbre).
    """

    def __init__(self, frequence, symbole=None):
        """
        Initialiser un nouveau nœud avec sa fréquence et son éventuel symbole.
        """
        self.frequence = frequence
        self.symbole = symbole
        self.gauche = None
        self.droit = None
        self.parent = None

    def est_feuille(self):
        """
        Vérifier si le nœud actuel est une terminaison sans enfant (feuille).
        """
        return self.gauche is None and self.droit is None


class ArbreHuffman:
    """
    Gérer la structure logique et la génération de la table de codage.
    
    L'arbre est construit à partir d'une liste de fréquences pour minimiser la longueur 
    moyenne du code binaire.

    Attributs :
    - racine (Noeud) : Le point d'entrée supérieur de l'arbre construit.
    """

    def __init__(self):
        """
        Initialiser un arbre prêt à être construit.
        """
        self.racine = None

    def construire(self, frequences):
        """
        Assembler la structure de l'arbre en fusionnant les nœuds selon l'algorithme de Huffman.
        
        Args:
            frequences (list): Liste de tuples (symbole, fréquence).
        """
        # frequences: liste de tuples (symbole, frequence)
        if not frequences:
            self.racine = None
            return

        # Créer une feuille pour chaque symbole
        noeuds = [Noeud(freq, symbole) for symbole, freq in frequences]

        # Construire l'arbre en fusionnant les deux noeuds de plus faible fréquence
        while len(noeuds) > 1:
            noeuds.sort(key=lambda n: n.frequence)
            gauche = noeuds.pop(0)
            droit = noeuds.pop(0)
            parent = Noeud(gauche.frequence + droit.frequence)
            parent.gauche = gauche
            parent.droit = droit
            gauche.parent = parent
            droit.parent = parent
            noeuds.append(parent)

        self.racine = noeuds[0]

    def generer_table(self):
        """
        Produire un dictionnaire associant chaque symbole à son chemin binaire ('0'/'1').
        """
        table = {}
        if self.racine is None:
            return table

        def _parcourir(noeud, prefix):
            if noeud.est_feuille():
                # Cas d'un seul symbole dans l'arbre -> attribuer '0' si prefix vide
                table[noeud.symbole] = prefix if prefix != "" else "0"
                return
            if noeud.gauche is not None:
                _parcourir(noeud.gauche, prefix + "0")
            if noeud.droit is not None:
                _parcourir(noeud.droit, prefix + "1")

        _parcourir(self.racine, "")
        return table


class Huffman:
    """
    Orchestrer les processus de compression et de décompression de données.
    
    Cette classe sert d'interface principale pour transformer un message textuel 
    en un flux binaire optimisé et inversement.

    Exemple d'utilisation :
        >>> huff = Huffman()
        >>> msg = "BABA"
        >>> code = huff.compresser(msg) # Retourne "1010"
        >>> # Pour décompresser, on utilise l'arbre généré lors de la compression
        >>> texte = huff.decompresser("1010", mon_arbre) # Retourne "BABA"

    Attributs :
    - source (Donnees) : Référence vers les données d'entrée ou de sortie.
    """

    def _calculer_frequences(self, texte):
        """
        Comptabiliser les occurrences de chaque caractère dans le message source.
        """
        compte = Counter(texte)
        # Retourner une liste de (symbole, frequence)
        # Trie par fréquence ascendante pour déterminisme
        return list(sorted(compte.items(), key=lambda x: x[1]))

    def compresser(self, message):
        """
        Exécuter le cycle complet de compression d'un message texte.
        """
        # Étapes : Calculer fréquences -> Construire Arbre -> Générer Table -> Encoder.
        if message == "":
            self.arbre = ArbreHuffman()
            self.arbre.racine = None
            self.table = {}
            return ""

        freq_list = self._calculer_frequences(message)
        arbre = ArbreHuffman()
        arbre.construire(freq_list)
        table = arbre.generer_table()

        # Encoder le message
        try:
            encoded = "".join(table[ch] for ch in message)
        except KeyError as e:
            raise ValueError(f"Caractère inconnu lors de l'encodage: {e}")

        # Sauvegarder l'arbre et la table pour usage ultérieur
        self.arbre = arbre
        self.table = table
        return encoded

    def decompresser(self, flux, arbre):
        """
        Parcourir l'arbre bit par bit pour reconstituer le message original.
        
        Args:
            flux (str)          : La chaîne de bits à décoder.
            arbre (ArbreHuffman) : L'arbre de référence utilisé pour le codage.
        """
        resultat = []
        noeud_courant = arbre.racine
        
        for bit in flux:
            if bit == '0':
                noeud_courant = noeud_courant.gauche
            else:
                noeud_courant = noeud_courant.droit
            
            if noeud_courant.est_feuille():
                resultat.append(noeud_courant.symbole)
                noeud_courant = arbre.racine
                
        return "".join(resultat)