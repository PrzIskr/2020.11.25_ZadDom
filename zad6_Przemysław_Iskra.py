#Przemysław Iskra
#nr almumu: 145863
#grupa: L6
# zadanie 6

import copy
di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
#di_copied = di.copy() # kopiowanie plytkie tworzy refrencje do oryginalu w kopii
di_copied = copy.deepcopy(di)

print(di)
print(di_copied)

di['four'][0] = 'cztery'

print(di)
print(di_copied)