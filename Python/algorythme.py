# Ecrire un algorithme qui demande à l’utilisateur un nombre compris entre 1 et 3 jusqu’à ce que la réponse convienne.

n = int(input())
if n < 1 or n > 3:
 print("Saisie erronée. Recommencez")

# Ecrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse convienne.
# En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! »,
# et inversement, « Plus grand ! » si le nombre est inférieur à 10.

n = int(input())
if n < 10 or n > 20:
    if n < 10:
        print("Plus grand")
    elif n > 20:
        print("Plus Petit")

#  Ecrire un algorithme qui demande un nombre de départ, et qui ensuite affiche les dix nombres
# suivants. Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres
# de 18 à 27.

n = int(input())
print((n + 1), "à", (n + 10))

# Réécrire l'algorithme précédent, en utilisant cette fois l'instruction Pour

n = int(input())
for i in range(n + 1, n + 11):
    print(i)

# Ecrire un algorithme qui demande un nombre de départ, et qui ensuite écrit la table de
# multiplication de ce nombre, présentée comme suit (cas où l'utilisateur entre le nombre 7) :
# Table de 7 :
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70

n = int(input())
for i in range(1, 11):
    x = n * i
    print(x)






