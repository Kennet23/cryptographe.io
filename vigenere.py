import string

def chiffrement_vigenere(text, motcle):
    text = text.upper()
    motcle = motcle.upper()
    alphabet = string.ascii_uppercase
    tableau_chiffrement = str.maketrans(alphabet, alphabet[len(motcle):] + alphabet[:len(motcle)])
    texte_chiffre = text.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_vigenere(texte_chiffre, motcle):
    texte_chiffre = texte_chiffre.upper()
    motcle = motcle.upper()
    alphabet = string.ascii_uppercase
    tableau_dechiffrement = str.maketrans(alphabet[len(motcle):] + alphabet[:len(motcle)], alphabet)
    text = texte_chiffre.translate(tableau_dechiffrement)
    return text


def cryptage():
    print('1 - Chiffrement Vigénère')
    print('2 - Déchiffrement Vigénère')
    choice = int(input('Faites votre choix : '))
    
    if choice == 1:
        texte = input("Veuillez saisir le texte à crypter : ")
        key = input("Veuillez saisir la clé de cryptage : ")
        texte_chiffrer = chiffrement_vigenere(texte, key)
        print("Texte chiffré :",texte_chiffrer)
    elif choice == 2:
        texte = input("Veuillez saisir le texte crypté : ")
        cle = input("Veuillez saisir la clé de décryptage : ")
        texte_dechiffrer = dechiffrement_vigenere(texte, cle)
        print("Texte déchiffré :" ,texte_dechiffrer)
    else:
        print('Veuillez faire un choix entre 1 et 2')

cryptage()