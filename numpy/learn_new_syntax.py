import numpy as np
# a = np.array([[1,2] , [3,4] ,[5,6]] , dtype = np.float64)
# print(a.ndim)
# print(a.shape)
# print(a.itemsize)
# print(a)
# a = np.array([[1,2] , [3,4] ,[5,6]] , dtype = complex)
# print(a)
#
# x = np.zeros((3,4), dtype = np.float64)
# print(x)
#
# y = np.linspace(1,5,5) #divide the values for start and end based on last value spacing
# print(y)
#
# a = np.array([[1,2],[4,5],[8,9]])
# print(a.shape)
# y = a.reshape(6,1) #helps to change the dimension of array list
# print(y)
# print(a.ravel()) #helps to make any 2d list to 1d list
#
# print(a.min())
# print(a.max())
# print(a.mean())
# print(a.sum()) #sum all teh elements
# print(a.sum(axis = 0)) #it will sum all the position of elements in the list(x , y)
# print(a.sum(axis = 1)) #if we axis  1 it will add individual list in 2d list
# print(np.sqrt(a)) #can do squareroot of each other
#
# a = np.array([[1,2] , [6,8] ,[5,9]])
# b = np.array([[3,4],[5,6],[99,11]])
# print(a+b, a/b, a*b) #can sum directly /multiply directly

#Slicing

a = np.array([[1,2] , [6,8] ,[5,9]])
# print(a[-2])
# print(a[0:2,1])
# for x in a:
#     print(x)
for y in a.flat:
    print(y)
for y in a.flatten():
    print(y)

b = np.arange(6).reshape(3,2)
c = np.arange(6,12).reshape(3,2)

print(b)
d=np.vstack((b,c))
print(d)
e = np.hstack((b,c))
print(e)
print(np.hsplit(b,2))

#nditer






