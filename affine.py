import string

def chiffrement_affine(texte, a, b):
    texte = texte.upper()
    alpha = string.ascii_uppercase
    tableau_chiffrement = str.maketrans(alpha, ''.join([alpha[(a*i + b) % 26] for i in range(26)]))
    texte_chiffre = texte.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_affine(texte_chiffre, a, b):
    texte_chiffre = texte_chiffre.upper()
    alpha = string.ascii_uppercase
    tableau_dechiffrement = str.maketrans(''.join([alpha[(a*i + b) % 26] for i in range(26)]), alpha)
    texte = texte_chiffre.translate(tableau_dechiffrement)
    return texte

def cryptage_affine():
    choix = input("Voulez-vous chiffrer (A) ou déchiffrer (B) ? ").upper()
    
    if choix == 'A':
        texte = input("Entrez le texte à chiffrer : ")
        a = int(input("Entrez la valeur de a pour la clé : "))
        b = int(input("Entrez la valeur de b pour la clé : "))
        texte_chiffre = chiffrement_affine(texte, a, b)
        print("Texte chiffré :", texte_chiffre)
        
    elif choix == 'B':
        texte_chiffre = input("Entrez le texte à déchiffrer : ")
        a = int(input("Entrez la valeur de a pour la clé : "))
        b = int(input("Entrez la valeur de b pour la clé : "))
        texte_dechiffre = dechiffrement_affine(texte_chiffre, a, b)
        print("Texte déchiffré :", texte_dechiffre)
        
    else:
        print("Choix invalide. Veuillez choisir 'C' pour chiffrer ou 'D' pour déchiffrer.")

# Appel de la fonction d'interaction avec l'utilisateur
cryptage_affine()
