# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# expense_list = [{"January" : 2200 }, {"February" : 2350}, {"March" : 2600}, {"April" :2130} , {"May"  : 2600} ]
# 1. In Feb, how many dollars you spent extra compare to January?
expense_list = [2200,2350,2600,2130,2190]
x = expense_list[1]-expense_list[0]
print(x)

# 2. Find out your total expense in first quarter (first three months) of the year.
total =expense_list[0] + expense_list[1] + expense_list[2]
print(total)

# 3. Find out if you spent exactly 2000 dollars in any month
for price in expense_list:
    if price == 2000:
        x = 1
    else:
        continue;
if x !=1:
    print("no")
else :
    print("yes")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense_list.append(1980)
print(expense_list)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
expense_list[3]-=200
print(expense_list)








