# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take
# from a user using input() function
odd_number =[]
max_number = input("Enter the the maximum number to find list of odd numbers : ")
for i in range(int(max_number)):
    if i%2 ==1:
        odd_number.append(i)
print(odd_number)



