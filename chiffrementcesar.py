import string

def chiffrement_cesare(texte, motcle):
    texte = texte.upper()
    alphabet = string.ascii_uppercase
    motcle = int(motcle)
    tableau_chiffrement = str.maketrans(alphabet, alphabet[motcle:] + alphabet[:motcle])
    texte_chiffre = texte.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_cesare(texte_chiffre, motcle):
    texte_chiffre = texte_chiffre.upper()
    alphabet = string.ascii_uppercase
    motcle = int(motcle)
    tableau_dechiffrement = str.maketrans(alphabet[motcle:] + alphabet[:motcle], alphabet)
    texte = texte_chiffre.translate(tableau_dechiffrement)
    return texte

def cryptage():
    print('1 - Chiffrement Césare')
    print('2 - Déchiffrement Césare')
    choice = int(input('Faites votre choix : '))
    
    if choice == 1:
        text = input("Veuillez saisir le texte à crypter : ")
        key = input("Veuillez saisir la clé de cryptage : ")
        texte_chiffrer = chiffrement_cesare(text, key)
        print("Texte chiffré :",texte_chiffrer)
    elif choice == 2:
        texte = input("Veuillez saisir le texte crypté : ")
        cle = input("Veuillez saisir la clé de décryptage : ")
        texte_dechiffrer = dechiffrement_cesare(texte, cle)
        print("Texte déchiffré :",texte_dechiffrer)
    else:
        print('Veuillez faire un choix entre 1 et 2')

cryptage()