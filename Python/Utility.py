#Nous allons commencer nos problèmes de défi avancé en calculant quelle liste de deux entrées a la plus grande somme.
# Nous allons itérer à travers chacune des listes et calculer les sommes, puis nous allons comparer les deux et retourner
# celle qui a la plus grande somme.
# Voici les étapes dont nous avons besoin :

 """Définir la fonction pour accepter deux paramètres d'entrée : lst1 et lst2.
    Créer deux variables pour enregistrer les deux sommes
    Bouclez dans la première liste et additionnez tous les nombres.
    Parcourir en boucle la deuxième liste et additionner tous les nombres.
    Comparez la première et la seconde somme et renvoyez la liste dont la somme est la plus élevée."""


def larger_sum(lst1, lst2):
 sum1 = 0
 sum2 = 0
 for number in lst1:
  sum1 += number
 for number in lst2:
  sum2 += number
 if sum1 >= sum2:
  return lst1
 else:
  return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

# Nous construisons un appareil capable de mesurer le niveau de puissance de nos capacités de codage et, selon l'appareil,
# il sera impossible que nos niveaux de puissance soient supérieurs à 9000. Pour cette raison,
# lorsque nous itérons à travers une liste de valeurs de puissance, nous comptons chacun des nombres jusqu'à ce que
# notre somme atteigne une valeur supérieure à 9000. Une fois que cela se produit, nous devons arrêter d'ajouter les nombres
# et retourner la valeur où nous nous sommes arrêtés. Pour ce faire, nous devons suivre les étapes suivantes :

 """Définir la fonction pour qu'elle accepte une liste de nombres.
    Créer une variable pour garder la trace de notre somme
    Parcourir chaque élément de notre liste de nombres.
    Dans la boucle, ajoutez le nombre actuel à notre somme.
    Toujours dans la boucle, vérifiez si la somme est supérieure à 9000. Si c'est le cas, terminez la boucle
    Retournez la valeur de la somme à la fin de la boucle."""


def over_nine_thousand(lst):
 sum = 0
 for number in lst:
  sum += number
  if sum > 9000:
   break
  else:
   return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

#Voici un problème de codage plus traditionnel pour vous. Cette fonction sera utilisée pour trouver le nombre maximum
# dans une liste de nombres. Ceci peut être accompli en utilisant la fonction max() de Python, mais pour relever le défi,
# nous allons implémenter manuellement cette fonction. Voici ce que nous devons faire :

 """Définir la fonction pour accepter une liste de nombres appelée nums.
    Définir notre valeur maximale par défaut comme étant le premier élément de la liste.
    Parcourir en boucle chaque nombre de la liste de nombres.
    Dans la boucle, si nous trouvons un nombre supérieur à notre maximum de départ, nous remplaçons le maximum par ce 
    que nous avons trouvé.
    Retourner le nombre maximum."""


def max_num(nums):
 maximum = nums[0]
 for number in nums:
  if number > maximum:
   maximum = number
 return maximum

print(max_num([50, -10, 0, 75, 20]))

#Dans ce défi, nous devons trouver les indices dans deux listes de taille égale où les chiffres correspondent.
# Nous allons itérer à travers les deux listes en même temps et comparer les valeurs, si les nombres sont égaux, alors
# nous enregistrons l'indice.
# Voici les étapes dont nous avons besoin pour accomplir cette tâche :

 """Définir notre fonction pour accepter deux listes de nombres.
    Créer une nouvelle liste pour stocker les indices correspondants
    Bouclez sur chaque indice jusqu'à la fin de l'une ou l'autre de nos listes.
    Dans la boucle, vérifiez si notre première liste à l'indice actuel est égale à la seconde liste à l'indice actuel. 
    Si c'est le cas, ajoutez l'indice où ils correspondent.
    Retourner notre liste d'indices"""

def same_values(lst1, lst2):
 new_list = []
 for index in range(len(lst1)):
  if lst1[index] == lst2[index]:
   new_list.append(index)
 return new_list

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

#Dans cette solution, nous avons utilisé une boucle qui itère en utilisant l'intervalle de la longueur de notre liste.
# Cela génère les indices que nous devons parcourir par itération. Notez que nous supposons que les listes sont de
# taille égale. Nous accédons ensuite à l'élément à l'index courant de chaque liste en utilisant lst1[index] et
# lst2[index]. S'ils sont égaux, nous ajoutons l'indice à la nouvelle liste. Enfin, nous retournons les résultats.

#Pour le dernier défi, nous allons tester deux listes pour voir si la deuxième liste est l'inverse de la première.
# Il y a plusieurs façons d'aborder cette question, mais nous allons essayer une méthode qui itère à travers chacune
# des valeurs dans une direction pour la première liste et les compare aux valeurs partant de l'autre direction dans la
# deuxième liste. Voici ce que vous devez faire :

 """Définir une fonction qui a deux paramètres d'entrée pour nos listes.
    Effectuez une boucle sur chaque indice de l'une des listes, du début à la fin.
    Dans la boucle, comparez l'élément de la première liste à l'indice actuel avec l'élément du dernier indice de la 
    deuxième liste moins l'indice actuel. S'il y a un désaccord, alors les listes ne sont pas inversées et nous pouvons 
    retourner False.
    Si la boucle se termine avec succès, alors nous savons que les listes sont inversées et nous pouvons retourner True."""

def reversed_list(lst1, lst2):
 for index in range(len(lst1)):
  if lst1[index] != lst2[len(lst2) - 1 - index]:
   return False
 return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


"""Dans ce code, nous itérons à travers chacun des indices pour la longueur totale de l'une ou l'autre des listes (puisque nous supposons que les longueurs sont égales) et 
nous effectuons une comparaison sur chacun des éléments. Nous récupérons l'élément à l'index courant de notre première liste avec lst1[index] et nous le testons par rapport 
au dernier index de la seconde liste moins l'index courant len(lst2) - 1 - index.

Ces calculs sont un peu compliqués - il est utile de prendre un exemple concret. Si l'on nous donne une liste de 5 éléments, les indices valides sont de 0 à 4, 
ce qui signifie que le dernier indice de la deuxième liste est len(lst2) - 1, soit 5 - 1 = 4. Maintenant, pour obtenir l'inverse de la position à laquelle 
nous sommes dans la première liste, nous soustrayons l'indice auquel nous sommes à la fin de la deuxième liste. Donc, au premier passage, nous allons comparer 
l'élément à la position 0 à l'élément à la position 5 - 1 - 0 = 4. Au passage suivant, nous comparerons l'élément en position 1 à l'élément en position 5 - 1 - 1 = 3, et ainsi de suite.

Si l'un des deux éléments n'est pas égal, nous savons que la deuxième liste n'est pas l'inverse de la première et nous retournons False. 
Si nous sommes arrivés à la fin sans erreur, nous pouvons renvoyer True puisque la deuxième liste est l'inverse de la première. 
Vous pouvez également essayer de simplifier ce code en utilisant la fonction python reversed() ou d'autres méthodes que 
vous apprendrez plus tard, comme le "slicing"."""







