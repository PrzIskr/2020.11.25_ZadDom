#Przemysław Iskra
#nr almumu: 145863
#grupa: L6
# zadanie 5b

list_len = 5
list2_len = 4
#i = 0
#j = 0

from random import randint

rand_list = [[randint(1, 10) for element in range (list2_len)] for list2 in range (list_len)]

print(rand_list)