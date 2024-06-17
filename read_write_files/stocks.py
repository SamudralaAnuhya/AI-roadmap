# contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# pe ratio = price / earnings per share
# price to book ratio = price / book value
# Your input format (stocks.csv) is,
#
# Company Name	Price	Earnings Per Share	Book Value
# Reliance	1467	66	653
# Tata Steel	391	89	572
# Output.csv should look like this,
#
# Company Name	PE Ratio	PB Ratio
# Reliance	22.23	2.25
# Tata Steel	4.39	0.68

with open("/Users/anuhyasamudrala/Documents/python_exercise/stocks.csv" ,"r")  as f, open("/Users/anuhyasamudrala/Documents/python_exercise/stocks_out.csv" ,"w") as out:
    out.write("Company name , PE Ration , PB Ration \n")
    next(f)
    for line in f :
        stock_values = line.split(",")
        company_name = stock_values[0]
        stock_price = float(stock_values[1])
        per_share = float(stock_values[2])
        Book_value = float(stock_values[3])
        pe_ration = round((stock_price / per_share),2)
        pb_ration = round((stock_price / Book_value),2)
        print(pe_ration,pb_ration)
        out.write(f"{company_name},{pe_ration} , {pb_ration} \n")


