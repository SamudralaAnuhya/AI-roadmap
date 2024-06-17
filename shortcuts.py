# list
a = [1,2,3,4,5,6,7,8,9,10]
even =[]
for i in a :
    if i % 2 == 0:
        even.append(i)
print(even)

# we can write like this too(in the brackets first i is like to store value format)
even_number =[i  for i in a if i % 2 == 0]
print(even_number)
square_number =[i*i for i in a ]
print(square_number)

# set ( remove duplicates and wrote output)
b  =[1,2,3,4,5,6,7,8,9,10 , 3, 4,5 ,6]
print(b)
c  ={1,2,3,4,5,6,7,8,9,10 , 3, 4,5 }   ##set {}..this braces remove dup
print(c)
even_number =[i for i in b if i % 2 == 0]
print(even_number)
even_number ={i for i in b if i % 2 == 0}  ##removed duplicates
print(even_number ,)

#dictcomprehension  (zip command used to add 2 lists)
list1 = ["anu" , "vimala" ,"deepika" ,"Triveni" ]
list2 = ["vivek" , "sjvs" ,"hari", "srinivasarao" ]
couples = zip(list1,list2)
for i in couples :
    print(i)

d = {a:b for a, b in zip(list1,list2) }
print(d)






