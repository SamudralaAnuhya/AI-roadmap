# create any set anf try to use frozenset(setname)
# Find the elements in a given set that are not in another set

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

difference = set1 - set2
print(difference)
difference1 = set1.difference(set2)
print(difference1)