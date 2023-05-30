import pandas as pd
import indicators
import standardize
import formula
import derivatives

stock = input("What stock would you like to analyze: ")
date = input("When would you like to begin (YYYY-MM-DD): ")

#dataset used for plotting
data = pd.DataFrame()
data = data.ta.ticker(stock, start = date)

rsiVal = indicators.getRSIVal(data)
macdVal = indicators.getMACDVal(data)
adxVal = indicators.getADXVal(data)
adxDVal = indicators.getADXDiff(data)
zscore = indicators.getZSCORE(data)
kurtosis = indicators.getKURTVal(data)
maDeriv = derivatives.derivInterpret(data)

#if less than 0, oversold, if greater than 0, overbought
calculatedVal = formula.calculate(data)

print("OVERALL VALUE: " + str(calculatedVal) + "\n" )
print("COMPONENT VALUES: ")
print("RSI Value: " + str(rsiVal))
print("MACD Value: " + str(macdVal))
print("ADX Value: " + str(adxVal))
print("ADX Diff: " + str(adxDVal))
print("ZSCORE: " + str(zscore) + "\n")

#higher values = more risk
print("RISK ANALYSIS: ")
print("KURTOSIS: " + str(kurtosis)  + "\n")

#derivative analysis--moving averages
print("Rate of Change Analysis: ")
print("Moving Averages: " + maDeriv)






