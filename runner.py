#ignore futureWarnings--semantic changes from pandas

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#import statements
import pandas as pd
import indicators
import standardize
import formula
import derivatives
import variability
import stockList
import time
from datetime import datetime

#global variables
overallData = pd.DataFrame()

#standard functions to search stocks
def retrieveInfo():
    stock = input("What stock would you like to analyze: ")
    date = input("When would you like to begin (YYYY-MM-DD): ")
    dataTab = pd.DataFrame()
    dataTab = dataTab.ta.ticker(stock, start = date)
    return(dataTab)

def mainOutput(dataTab):

    rsiVal = indicators.getRSIVal(dataTab)
    macdVal = indicators.getMACDVal(dataTab)
    adxVal = indicators.getADXVal(dataTab)
    adxDVal = indicators.getADXDiff(dataTab)
    zscore = indicators.getZSCORE(dataTab)
    kurtosis = indicators.getKURTVal(dataTab)
    maDeriv = derivatives.firstDerivInterpret(dataTab)
    maDoubleDeriv = derivatives.secondDerivInterpret(dataTab)
    r2Val = variability.getR2(dataTab)
    residDev = variability.getSTDResidual(dataTab)
    obvTrend = indicators.analyzeOBVDivergence(dataTab, 7)
    obvSlope = indicators.getOBVSlope(dataTab, 7)
    priceSlope = indicators.getPriceSlope(dataTab, 7)

    #interpretation 
    #if a value of within the range of +/-1.8 stock is fairly neutral
    #if a value of above (or below) +/- 1.8, moderately overbought/oversold, respectively (moving out of the 50% range of data)
    #if a value of above (or below) +/- 4.1, strongly overbought/oversold, respectively (moving out of the 80% range of data)
    #if a value of above (or below) +/-8, extremely overbought/oversold, respectively (moving out of the 95% range of data)

    calculatedVal = formula.calculate(dataTab)

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
    print("MOVING AVERAGES FIRST: " + maDeriv)
    print("MOVING AVERAGES SECOND: " + maDoubleDeriv)
    print("OBV DIVERGENCE: " + obvTrend)
    print("OBV SLOPE: " + str(obvSlope))
    print("PRICE SLOPE: " + str(priceSlope))

#autoRunner functions

def autoRunner(stockNames):
    startTime = time.time()
    inc = 0
    for stock in stockNames:
        dataTab = pd.DataFrame()
        dataTab = dataTab.ta.ticker(stock, start = "2023-01-01")
        getCalculatedValues(dataTab, stock)
        inc = inc + 1
        currentTime = time.time()
        timeDiff = currentTime - startTime
        roundedTimeDiff = round(timeDiff, 2)  
        print(str(inc) + ": " + stock + ": " + str(roundedTimeDiff) + "\n")
    setTicker()
    return(overallData)

def getCalculatedValues(dataTab, stock):
    #if you change anything within calculated values, you must change overall data dataframe as well
    name = stock
    points = 0.0
    calVal = formula.calculate(dataTab)
    rsiVal = indicators.getRSIVal(dataTab)
    macdVal = indicators.getMACDVal(dataTab)
    adxVal = indicators.getADXVal(dataTab)
    adxDVal = indicators.getADXDiff(dataTab)
    zscore = indicators.getZSCORE(dataTab)
    kurtosis = indicators.getKURTVal(dataTab)
    maDeriv = derivatives.firstDerivInterpret(dataTab)
    maDoubleDeriv = derivatives.secondDerivInterpret(dataTab)
    r2Val = variability.getR2(dataTab)
    #residDev = variability.getSTDResidual(dataTab)
    obvTrend = indicators.analyzeOBVDivergence(dataTab, 7)
    obvSlope = indicators.getOBVSlope(dataTab, 7)
    priceSlope = indicators.getPriceSlope(dataTab, 7)
    reccBuy = "NEUTRAL"
    
    #RSI points
    if(rsiVal < 30):
        points = points + 1
    elif(rsiVal < 40):
        points = points + 0.5
    elif(rsiVal <= 60):
        points = points
    elif(rsiVal <= 70): 
        points = points - 0.5
    else:
        points = points - 1
    
    #MACD points
    if(macdVal < 0):
        points = points + 1
    else:
        points = points - 1
        
    #ZSCORE points
    if(zscore < -2):
        points = points + 1
    elif(zscore < -1):
        points = points + 0.5
    elif(zscore <= 1):
        points = points
    elif(zscore <= 2):
        points = points - 0.5
    else:
        points = points - 1
    
    #maDeriv/doubleDeriv points
    if(maDoubleDeriv == "NEGATIVE"):
        points = points - 1
    elif((maDeriv == "POSITIVE")):
        points = points + 1
    else:
        points = points
        
    #OBV points
    if((obvTrend == "CONFIRMING TREND DOWNWARD") or (obvTrend == "OPPOSING TREND DOWNWARD")):
        points = points - 1
    elif((obvTrend == "CONFIRMING TREND UPWARD") or (obvTrend == "OPPOSING TREND UPWARD")):
        points = points + 1
    else:
        points = points
    
    
    if(points >= 2.5):
        reccBuy = "STRONG BUY"
    elif(points >= 1):
        reccBuy = "BUY"
    elif(points > -1):
        reccBuy = "NEUTRAL"
    elif(points > - 2.5):
        reccBuy = "SELL"
    else:
        reccBuy = "STRONG SELL"
    
    data = [[name, calVal, rsiVal, macdVal, adxVal, adxDVal, zscore, kurtosis, maDeriv, maDoubleDeriv, r2Val, obvTrend, obvSlope, priceSlope, points, reccBuy]]
    global overallData
    tempData = pd.DataFrame(data, columns = ["ticker", "calVal", "rsiVal", "macdVal", "adxVal", "adxDVal", "zscore", "kurtosis", "maDeriv", "maDoubleDeriv", "r2Val", "obvTrend", "obvSlope", "priceSlope", "points", "recommendation"])
    overallData = pd.concat([overallData, tempData])
    return tempData
    
def setTicker():
    global overallData
    overallData = overallData.set_index("ticker")    

#modify following section to either a) manually run for certain tickers or b) autorun stocks

#a) manually run tickers
#data = retrieveInfo()
#mainOutput(data)

# #b)autoRun stocks
stockNames = stockList.allMajor()
stockDF = autoRunner(stockNames)
stockDF = stockDF.sort_values("points", ascending=False)
date = datetime.today().strftime('%Y-%m-%d')
date = r"{}".format(date)
print(stockDF)

#b.1) export autoRunStocks to csv

#set to whatever folder in the python directory you wish to save to 
fileLocation = ("stockData/" + date + r".csv")
stockDF.to_csv(fileLocation)
