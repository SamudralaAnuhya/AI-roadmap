#ask user to enter number , program should odd or even

# num = input("Enter a number: ")
# if int(num)% 2 == 0 :
#     print("The number is even")
# else :
#     print("The number is odd")

# enter dish name program should give which cuisine
dish = input("Enter a dish ")
indian_cuisine = ["mushrooms","panner","chapathi" ,"rice"]
american_cuisine = ["bread","pasta","beef"]
chinese_cuisine = ["noodles","friedrice" ]
if dish in indian_cuisine :
    print("The", dish ,"is  indian ")
elif dish in american_cuisine :
    print("The", dish, "is american")
elif dish in chinese_cuisine :
    print("The", dish, "is chinese")
else: print("based on little knowledge i have i dont know which cuisine  is" , dish)


#
# wallet_loc = "chair"
# loc = ["sofa", "chair" , "kitchen", "bed", "table", "tv"]
# visited_location = ''
# for i in range(len(loc)):
#     visited_location = str(visited_location)  + ' '+str(loc[i])
#     if loc[i] == wallet_loc:
#         print(loc[i])
#         break
# else : print("Not found")
# print(visited_location)
#


# # print square of number from 1 to 5 except even
# for i in range (1,6):
#     if i%2 != 0:
#         print(i*i)
#
# for i in range (1,6):
#     if i%2 == 0:
#         continue
#     print(i*i)
#


# print numbers 1 to 5 using while
i=0
while i <= 5:
    print(i)
    i = i + 1

