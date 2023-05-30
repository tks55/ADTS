import pandas as pd
import indicators

stock = input("What stock would you like to analyze: ")
date = input("When would you like to begin (YYYY-MM-DD): ")

#dataset used for plotting
data = pd.DataFrame()
data = data.ta.ticker(stock, start = date)
#print(dataTab)

print(indicators.getRSI(data))
print(indicators.getMACD(data))
print(indicators.getZSCORE(data))


