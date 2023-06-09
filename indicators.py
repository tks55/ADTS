import pandas as pd
import numpy
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas_ta as ta
import mplfinance as mpl
import math
from sklearn.linear_model import LinearRegression


#file with pandasTA indicators

#we can clean this up if we use instance variables

def getRSITab(dataTab):
    rsi14 = dataTab.ta.rsi()
    rsi14 = rsi14.reset_index()
    #print(rsi14)
    return(rsi14)

def getRSIVal(dataTab):
    rsi14Tab = getRSITab(dataTab)
    lenR14 = len(rsi14Tab)
    lastR14 = rsi14Tab.at[lenR14 - 1, "RSI_14"]
    #print(lastR14)
    return(lastR14)

def getRSIMean(dataTab):
    rsi14Tab = getRSITab(dataTab)
    rsiMean = rsi14Tab.mean()["RSI_14"]
    return(rsiMean)

def getRSISTD(dataTab):
    rsi14Tab = getRSITab(dataTab)
    rsiSTD = rsi14Tab.std()["RSI_14"]
    return(rsiSTD)

#IF MACDS > MACDL, buy signal

def getMACDTab(dataTab):
    macd = dataTab.ta.macd()
    macd = macd.reset_index()
    #print(macd)
    return(macd)

def getMACDVal(dataTab):
    macdTab = getMACDTab(dataTab)
    lenMACD = len(macdTab)
    lastMACDS = macdTab.at[lenMACD - 1, "MACD_12_26_9"]
    lastMACDL = macdTab.at[lenMACD - 1, "MACDs_12_26_9"]
    #print(lastMACDS)
    #print(lastMACDL)
    return(lastMACDS - lastMACDL)

def getMACDMean(dataTab):
    macdTab = getMACDTab(dataTab)
    macdSMean = macdTab.mean()["MACD_12_26_9"]
    macdLMean = macdTab.mean()["MACDs_12_26_9"]
    macdMean = macdSMean - macdLMean
    return(macdMean)

def getMACDSTD(dataTab):
    macdTab = getMACDTab(dataTab)
    macdSSTD = macdTab.std()["MACD_12_26_9"]
    macdLSTD = macdTab.std()["MACDs_12_26_9"]
    macdSVar = math.pow(macdSSTD, 2)
    macdLVar = math.pow(macdLSTD, 2)
    macdSTD = math.sqrt(macdSVar + macdLVar)
    return(macdSTD)

def getZSCORE(dataTab):
    zscore = dataTab.ta.zscore()
    zscore = zscore.reset_index()
    #print(zscore)
    lenZSCORE = len(zscore)
    lastZSCORE = zscore.at[lenZSCORE - 1, "ZS_30"]
    #print(lastZSCORE)
    return(lastZSCORE)

def getADXTab(dataTab):
    adx = dataTab.ta.adx()
    adx = adx.reset_index()
    return(adx)

def getADXVal(dataTab):
    adxTab = getADXTab(dataTab)
    lenADX = len(adxTab)
    lastADX = adxTab.at[lenADX - 1, "ADX_14"]
    return(lastADX)
    
def getADXDiff(dataTab):
    adxTab = getADXTab(dataTab)
    lenADX = len(adxTab)
    lastDIP = adxTab.at[lenADX - 1, "DMP_14"]
    lastDIM = adxTab.at[lenADX - 1, "DMN_14"]
    diff = lastDIP - lastDIM
    return(diff)

def getADXDMean(dataTab):
    adxTab = getADXTab(dataTab)
    dipMean = adxTab.mean()["DMP_14"]
    dimMean = adxTab.mean()["DMN_14"]
    adxDMean = dipMean - dimMean
    return(adxDMean)

def getADXDSTD(dataTab):
    adxTab = getADXTab(dataTab)
    dipSTD = adxTab.std()["DMP_14"]
    dimSTD = adxTab.std()["DMN_14"]
    dipVar = math.pow(dipSTD, 2)
    dimVar = math.pow(dimSTD, 2)
    adxDSTD = math.sqrt(dipVar + dimVar)
    return(adxDSTD)

def getKURTTab(dataTab):
    kurt30 = dataTab.ta.kurtosis()
    kurt30 = kurt30.reset_index()
    return(kurt30)

def getKURTVal(dataTab):
    kurtTab = getKURTTab(dataTab)
    lenKURT = len(kurtTab)
    lastKURT = kurtTab.at[lenKURT - 1, "KURT_30"]
    return(lastKURT)

def getOBVTab(dataTab):
    obv = dataTab.ta.obv()
    obv = obv.reset_index()
    return(obv)

def getOBVVals(dataTab, period):
    obvTab = getOBVTab(dataTab)
    lenOBVTab = len(obvTab)
    obvVals = numpy.array([])
    for i in range(period):
        obvCurrVal = obvTab.at[lenOBVTab - period + i, "OBV"]
        obvVals = numpy.append(obvVals, obvCurrVal)
    return(obvVals)

def getPrevDataTabC(dataTab, period):
    data = dataTab["Close"]
    data = data.reset_index()
    lenData = len(data)
    preData = numpy.array([])
    for i in range(period):
        dataCurrVal = data.at[lenData - period + i, "Close"]
        preData = numpy.append(preData, dataCurrVal)
    return(preData)

def getIndexedSeries(period):
    index = numpy.arange(period)
    index = index.reshape(-1, 1)
    return(index)

def getOBVSlope(dataTab, period):
    x = getIndexedSeries(period)
    y = getOBVVals(dataTab, period)
    model = LinearRegression().fit(x, y)
    slope = model.coef_
    return(slope[0])
    
def getPriceSlope(dataTab, period):
    x = getIndexedSeries(period)
    y = getPrevDataTabC(dataTab, period)
    model = LinearRegression().fit(x, y)
    slope = model.coef_
    return(slope[0])
    
def analyzeOBVDivergence(dataTab, period):
    obvSlope = getOBVSlope(dataTab, period)
    priceSlope = getPriceSlope(dataTab, period)
    obvDeterminant = obvSlope * priceSlope
    if(obvDeterminant > 0):
        if(priceSlope > 0):
            return("CONFIRMING TREND UPWARD")
        elif(priceSlope < 0):
            return("CONFIRMING TREND DOWNWARD")
        else:
            return("ERROR")
    elif(obvDeterminant < 0):
        if(priceSlope > 0):
            return("OPPOSING TREND DOWNWARD")
        if(priceSlope < 0):
            return("OPPOSING TREND UPWARD")
        else:
            return("ERROR")
    else:
        return("ERROR")
