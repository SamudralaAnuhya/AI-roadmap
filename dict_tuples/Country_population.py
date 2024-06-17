# # area = (1/2)*base*height
# shape = (input("Enter a shape: "))
# base = int(input("Enter a base: "))
# height = int(input("Enter a height: "))
#
# if shape == 'rectangle':
#     area = base * height
# else:
#     area = 1 / 2 * (base * height)
# print("The area: ", area)


# # Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# # *
# # **
# # ***
#
#
# def print_pattern(number):
#     for i in range(1,number+1):
#         s = ''
#         for j in range(1, i):
#             s = s + '*'
#         print(s)
#
# number = int(input('Enter a number: '))
# x = print_pattern(number)


#
# We have following information on countries and their population (population is in crores),
#
# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
population = {'china' :	143 , 'india':136,'usa': 32, 'pakistan':21}
def print2():
    for country, value in population.items():
        print(f"{country}==>{value}")

def add2():
    country = input("Enter country name: ")
    country = country.lower()
    if country in population:
        print("country already exists")
        return

    value = input("enter population of the country :")
    population[country] = value
    print2()

def remove():
    country = input("enter country to be removed")
    country = country.lower()
    if country in population:
        del population[country]
        print2()
    else:
        print("country does not exist: ")

def query2():
    country = input("enter the country name to be queried  : ")
    country = country.lower()
    if country in population:
       print(f"{country}==>{population[country]}")
    else:
        print("country does not")

def main():
    checkbox = input("enter the operation to perform : ")
    if checkbox == "print" :
        print2()
    elif checkbox == "add" :
        add2()
    elif checkbox == "remove" :
        remove()
    elif checkbox == "query" :
        query2()

if __name__ == "__main__":
    main()














