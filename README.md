# Cryptographie
Ensemble des cryptage classique
Cet code contient l'ensemble des algorithmes utiliser pour chiffrer et dechiffrer des messages
avec le cryptage  de Césare, Vigenere et celui Affine
Language : Python

        CHIFFREMENT DE CESARE


1 - Importation de modules :
import string
Ici, le module string est importé pour utiliser la constante string.ascii_uppercase, qui représente toutes les lettres majuscules de l'alphabet.

2 - Définition des fonctions de chiffrement et de déchiffrement :

    def chiffrement_cesare(texte, motcle):

        a - texte = texte.upper() :
            Convertit le texte en majuscules. Cela assure que le chiffrement est effectué de manière insensible à la casse.
        b - alphabet = string.ascii_uppercase :
            Crée une chaîne contenant toutes les lettres majuscules de l'alphabet.
        c - motcle = int(motcle) :
            Convertit la clé (décalage dans le chiffrement de César) en un entier. Cela est nécessaire car l'entrée utilisateur est traitée comme une chaîne de caractères.
        d - tableau_chiffrement = str.maketrans(alphabet, alphabet[cle:] + alphabet[:cle]) :
            Utilise la fonction str.maketrans pour créer une table de substitution. Elle marque chaque caractère de l'alphabet vers le caractère correspondant après le décalage.
        e - texte_chiffre = texte.translate(tableau_chiffrement) :
            Utilise la méthode translate pour appliquer la substitution à chaque caractère du texte.
        f - return texte_chiffre : 
            Renvoie le texte chiffré.

    def dechiffrement_cesare(texte_chiffre, motcle):
    
        a - texte_chiffre = texte_chiffre.upper() :
            Convertit le texte chiffré en majuscules pour assurer la correspondance avec l'alphabet.
        b - alphabet = string.ascii_uppercase : 
            Initialise l'alphabet.
        c - tableau_dechiffrement = str.maketrans(alphabet[cle:] + alphabet[:cle], alphabet) : 
            Crée une table de substitution pour le déchiffrement.
        d - texte = texte_chiffre.translate(tableau_dechiffrement) : 
            Applique la substitution au texte chiffré pour obtenir le texte déchiffré.
        e - return texte : 
            Renvoie le texte déchiffré.

Ces fonctions prennent un texte et une clé en entrée, puis effectuent le chiffrement ou le déchiffrement de César en utilisant une table de substitution.

3 - Conversion de la clé en entier :
motcle = int(motcle)
Cette ligne de code convertit la clé (qui est une chaîne de caractères obtenue à partir de l'entrée utilisateur) en un entier. Cela est nécessaire car les indices pour le découpage de la chaîne doivent être des entiers.

4 - Logique de l'interface utilisateur :
def cryptage_cesare() :
    # ...
Cette fonction affiche un menu à l'utilisateur avec les options de chiffrement et de déchiffrement. En fonction du choix de l'utilisateur, elle demande le texte et la clé appropriés, puis appelle la fonction de chiffrement ou de déchiffrement.

    a - choice = int(input('Faites votre choix : '))
Cette ligne de code convertit le choix de l'utilisateur en un entier. Cela est nécessaire car input() renvoie une chaîne de caractères, et vous devez comparer le choix avec des entiers dans les instructions conditionnelles.


    b - print('Veuillez faire un choix entre 1 et 2')
Cette ligne affiche un message d'erreur lorsque l'utilisateur entre un choix invalide.

5 - Appel de la fonction principale :
cryptage()
Enfin, cette ligne appelle la fonction principale pour exécuter le programme.



      CHIFFREMENT VIGENERE


1 - Importation de modules :
import string
Ici, le module string est importé pour utiliser la constante string.ascii_uppercase, qui représente toutes les lettres majuscules de l'alphabet.

2 - Définition des fonctions de chiffrement et de déchiffrement :

    def chiffrement_vigenere(text, motcle):

        a - La fonction prend deux paramètres : text (le texte à chiffrer) et motcle (la clé de chiffrement).
        b - Les deux chaînes (text et motcle) sont converties en majuscules pour assurer une correspondance insensible à la casse.
        c - L'alphabet est créé à l'aide de string.ascii_uppercase, qui est la liste des lettres majuscules de l'alphabet anglais.
        d - Une table de chiffrement est créée à l'aide de str.maketrans. Cette table est générée en décalant l'alphabet par la longueur de la clé. Par exemple, si la clé est "KEY", la table sera générée en décalant l'alphabet de "KEY" positions vers la gauche. Cela crée un tableau de substitution pour le chiffrement de Vigenère.
        e - La fonction translate est utilisée pour appliquer la substitution du tableau de chiffrement au texte, produisant ainsi le texte chiffré.

    def dechiffrement_vigenere(texte_chiffre, motcle):

        a - La fonction prend deux paramètres : texte_chiffre (le texte chiffré) et motcle (la clé de déchiffrement).
        b - Les deux chaînes (texte_chiffre et motcle) sont converties en majuscules.
        c - Une table de déchiffrement est créée de manière similaire à la fonction de chiffrement, mais cette fois en décalant l'alphabet dans l'autre sens par la longueur de la clé.
        e - La substitution du tableau de déchiffrement est appliquée au texte chiffré à l'aide de translate, produisant ainsi le texte déchiffré.

3 - Logique de l'interface utilisateur :

def cryptage() :
    # ...
Cette fonction affiche un menu à l'utilisateur avec les options de chiffrement et de déchiffrement. En fonction du choix de l'utilisateur, elle demande le texte et la clé appropriés, puis appelle la fonction de chiffrement ou de déchiffrement.

4 - Appel de la fonction principale :
cryptage()
Enfin, cette ligne appelle la fonction principale pour exécuter le programme.



       CHIFFREMENT AFFINE 

Cet algorithme de chiffrement affine est une technique de chiffrement par substitution qui utilise une fonction mathématique linéaire pour transformer les lettres du texte. La formule de chiffrement affine est généralement exprimée comme suit : E(x)=(ax+b)mod m où  E(x) est la lettre chiffrée, x est la lettre originale, a et b sont les paramètres de la clé, et m est la taille de l'alphabet (dans ce cas, la taille de l'alphabet est 26, car il s'agit d'une substitution sur les lettres majuscules).
Le code fourni comprend deux fonctions : chiffrement_affine qui chiffre le texte et dechiffrement_affine qui le déchiffre.

1 - Importation de modules :
import string
Ici, le module string est importé pour utiliser la constante string.ascii_uppercase, qui représente toutes les lettres majuscules de l'alphabet.

2 - Définition des fonctions de chiffrement et de déchiffrement :

    def chiffrement_affine (texte,a,b):

        a - Paramètres:
            texte: Le texte que vous souhaitez chiffrer.
            a: Le coefficient multiplicatif dans la formule de chiffrement affine.
            b: Le terme constant dans la formule de chiffrement affine.
        b - Traitement du texte:
            Le texte d'entrée est converti en majuscules avec texte.upper().
            L'alpha est défini avec string.ascii_uppercase, qui est la liste des lettres majuscules de l'alphabet anglais.
        c - Table de Chiffrement:
            La table de chiffrement est créée à l'aide de str.maketrans. Elle effectue une substitution en utilisant l'alphabet original et un alphabet modifié. L'alphabet modifié est généré en prenant les caractères après la position a et en les plaçant devant les caractères avant la position a. Cela crée la substitution pour le chiffrement affine.
        d - Chiffrement et retour:
        La fonction translate est utilisée pour appliquer la substitution au texte d'entrée, produisant ainsi le texte chiffré. Ainsi le texte est revoyé

    def chiffrement_affine (texte_chiffre,a,b):

        a - Paramètres:
            texte_chiffre: Le texte chiffré que vous souhaitez déchiffrer.
            a: Le coefficient multiplicatif dans la formule de déchiffrement affine.
            b: Le terme constant dans la formule de déchiffrement affine.
        b - Traitement du Texte Chiffré:
            Le texte chiffré est converti en majuscules avec texte_chiffre.upper().
        c - Table de Déchiffrement:
            La table de déchiffrement est créée de manière similaire à celle du chiffrement, mais cette fois en décalant l'alphabet dans l'autre sens. Elle effectue une substitution utilisant l'alphabet modifié pour déchiffrer le texte.
        d - Déchiffrement et retour:
            La fonction translate est utilisée pour appliquer la substitution au texte chiffré, produisant ainsi le texte déchiffré.
3 - Logique de l'interface utilisateur :
def cryptage_affine() :
    # ...
Cette fonction affiche un menu à l'utilisateur avec les options de chiffrement et de déchiffrement. En fonction du choix de l'utilisateur, elle demande le texte et les clé appropriés, puis appelle la fonction de chiffrement ou de déchiffrement.

4 - Appel de la fonction principale :
cryptage_affine()
Enfin, cette ligne appelle la fonction principale pour exécuter le programme.             
