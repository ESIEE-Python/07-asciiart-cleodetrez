#### Imports et définition des variables globales
"""
Aucun module n'est nécéssaire à la fonction
"""
#### Fonctions secondaires
def artcode_i(s) :
    """retourne la liste de tuples encodant une chaîne
    de caractères passée en argument selon un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    c = [s[0]]
    n = [1]
    for i in range(1,len(s)) :
        if s[i - 1] == s[i] :
            n[-1] = n[-1] + 1
        else :
            c.append(s[i])
            n.append(1)
    return list(zip(c,n))

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de
    caractères passée en argument selon un algorithme récursif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # cas de base
    if s == "" :
        return []
    # recherche nombre de caractères identiques au premier
    # appel récursif
    k = 1
    for c in s[1:] :
        #print(s, c, k)
        if c == s[0] :
            k = k + 1
        else :
            break
    return [(s[0], k)] + artcode_r(s[k:])
#### Fonction principale

def main():
    """
    test si les fonctions marchent
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__" :
    main()
