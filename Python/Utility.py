#Nous allons commencer nos problèmes de défi avancé en calculant quelle liste de deux entrées a la plus grande somme. Nous allons itérer à travers chacune des listes et calculer les sommes, puis nous allons comparer les deux et retourner celle qui a la plus grande somme. Voici les étapes dont nous avons besoin :

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

# Nous construisons un appareil capable de mesurer le niveau de puissance de nos capacités de codage et, selon l'appareil, il sera impossible que nos niveaux de puissance soient supérieurs à 9000. Pour cette raison, lorsque nous itérons à travers une liste de valeurs de puissance, nous comptons chacun des nombres jusqu'à ce que notre somme atteigne une valeur supérieure à 9000. Une fois que cela se produit, nous devons arrêter d'ajouter les nombres et retourner la valeur où nous nous sommes arrêtés. Pour ce faire, nous devons suivre les étapes suivantes :

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

#Voici un problème de codage plus traditionnel pour vous. Cette fonction sera utilisée pour trouver le nombre maximum dans une liste de nombres. Ceci peut être accompli en utilisant la fonction max() de Python, mais pour relever le défi, nous allons implémenter manuellement cette fonction. Voici ce que nous devons faire :

 """Définir la fonction pour accepter une liste de nombres appelée nums.
    Définir notre valeur maximale par défaut comme étant le premier élément de la liste.
    Parcourir en boucle chaque nombre de la liste de nombres.
    Dans la boucle, si nous trouvons un nombre supérieur à notre maximum de départ, nous remplaçons le maximum par ce que nous avons trouvé.
    Retourner le nombre maximum."""


def max_num(nums):
 maximum = nums[0]
 for number in nums:
  if number > maximum:
   maximum = number
 return maximum

print(max_num([50, -10, 0, 75, 20]))





