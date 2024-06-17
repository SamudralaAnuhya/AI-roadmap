#find the total expense of each lists

anu_exp =[1,2,3,4,5,6,7,8,9]
vivek_exp =[5,6,7,8,9,10,11,12]
# total = 0
# for i in anu_exp:
#     total = total + i
# print(total)

def total_expense(exp):
    """
    write comments in this
    """
    total = 0
    for i in exp:
        total = total + i
    return total

x = total_expense(anu_exp)
y = total_expense(vivek_exp)
print(x , y)



def sum(a,b= []):
    total = a+b
    return total
a = sum(anu_exp)
print(a)
