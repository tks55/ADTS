import pandas as pd
import numpy
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas_ta as ta
import mplfinance as mpl

#file with pandasTA indicators

#returns the last value of RSI14 (Most Recent)
def getRSI(dataTab):
    rsi14 = dataTab.ta.rsi()
    rsi14 = rsi14.reset_index()
    #print(rsi14)
    lenR14 = len(rsi14)
    lastR14 = rsi14.at[lenR14 - 1, "RSI_14"]
    #print(lastR14)
    return(lastR14)

#IF MACDS > MACDL, buy signal

def getMACD(dataTab):
    macd = dataTab.ta.macd()
    macd = macd.reset_index()
    #print(macd)
    lenMACD = len(macd)
    lastMACDS = macd.at[lenMACD - 1, "MACD_12_26_9"]
    lastMACDL = macd.at[lenMACD - 1, "MACDs_12_26_9"]
    #print(lastMACDS)
    #print(lastMACDL)
    return(lastMACDS - lastMACDL)

def getZSCORE(dataTab):
    zscore = dataTab.ta.zscore()
    zscore = zscore.reset_index()
    #print(zscore)
    lenZSCORE = len(zscore)
    lastZSCORE = zscore.at[lenZSCORE - 1, "ZS_30"]
    #print(lastZSCORE)
    return(lastZSCORE)
