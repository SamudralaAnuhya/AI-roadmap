# you are given following list of stocks and their prices in last 3 days,

# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67

# add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

stocks = {'info' : [600,630,620] , 'ril' :[1430,1490,1567] , 'mtl':[234,180,160] }
def print_stocks():
    for key, value in stocks.items():
        print(f"{key}==>{value}==>avg: { round(sum(value)/len(value), 2)}")
def add_stock():
    key = input("Enter Stock name to be added : " )
    value = input("Enter stock price to be added : " )
    value = float(value)
    if key in stocks :
        stocks[key].append(value)
        print_stocks()
    else:
        stocks[key] = [value]
        print_stocks()



def main():
    add_stock()
if __name__ == '__main__':
    main()

