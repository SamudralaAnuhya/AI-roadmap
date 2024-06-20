# Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.
# Example :
#
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
binary_dict = dict(zip( integer , binary))
print(binary_dict)

# Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
# a + i = 0

integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1*i for i in integer]
print(additive_inverse)

# Create a set which only contains unique sqaures from a given a integer list.
integer = [1, -1, 2, -2, 3, -3]
# sq_set = {1, 4, 9}

square_number = { i*i for i in integer }
print(square_number)