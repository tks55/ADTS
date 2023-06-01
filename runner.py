import pandas as pd
import indicators
import standardize
import formula
import derivatives
import variability

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
r2Val = variability.getR2(data)
residDev = variability.getSTDResidual(data)

#interpretation 
#if a value of within the range of +/-1.8 stock is fairly neutral
#if a value of above (or below) +/- 1.8, moderately overbought/oversold, respectively (moving out of the 50% range of data)
#if a value of above (or below) +/- 4.1, strongly overbought/oversold, respectively (moving out of the 80% range of data)
#if a value of above (or below) +/-8, extremely overbought/oversold, respectively (moving out of the 95% range of data)

calculatedVal = formula.calculate(data)

print("OVERALL VALUE: " + str(calculatedVal) + "\n" )
print("COMPONENT VALUES: ")
print("RSI VALUE: " + str(rsiVal))
print("MACD VALUE: " + str(macdVal))
print("ADX VALUE: " + str(adxVal))
print("ADX DIFF: " + str(adxDVal))
print("ZSCORE: " + str(zscore) + "\n")

#higher values = more risk
print("RISK ANALYSIS: ")
print("R^2 VALUE: " + str(r2Val))

#residual deviation still needs to be tested
#print("RESIDUAL DEVIATION: " + str(residDev))
print("KURTOSIS: " + str(kurtosis)  + "\n")

#derivative analysis--moving averages
print("RATE OF CHANGE ANALYSIS: ")
print("MOVING AVERAGES: " + maDeriv)






