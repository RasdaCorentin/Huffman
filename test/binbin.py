import sys
import os
from huffman import Huffman

def principal():
    """
    Lire un fichier, compresser son contenu et traduire le résultat en binaire réel.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 test/binbin.py <chemin_du_fichier>")
        return

    # 1. Ouvrir le fichier au lieu de passer le contenu en argument
    chemin = sys.argv[1]
    if not os.path.exists(chemin):
        print(f"Erreur : Le fichier {chemin} n'existe pas.")
        return

    with open(chemin, "r", encoding="utf-8") as f:
        contenu_source = f.read()

    moteur = Huffman()
    
    # 2. Obtenir la chaîne de '0' et '1'
    flux_string = moteur.compresser(contenu_source)
    
    # 3. Traduire en binaire réel (Groupement par 8 bits)
    padding = 8 - (len(flux_string) % 8)
    if padding != 8:
        flux_string += "0" * padding

    donnees_binaires = bytearray()
    for i in range(0, len(flux_string), 8):
        huit_bits = flux_string[i:i+8]
        donnees_binaires.append(int(huit_bits, 2))

    # 4. Sauvegarder en mode binaire
    with open("test/resultat_reel.bin", "wb") as f_out:
        f_out.write(donnees_binaires)
    
    print(f"Succès ! Taille finale : {len(donnees_binaires)} octets.")

if __name__ == "__main__":
    principal()