import pandas as pd
import indicators
import standardize
import pandas_ta as ta

def macdDeriv(dataTab):
    macdTab = indicators.getMACDTab(dataTab)
    macdSTab = macdTab["MACD_12_26_9"]
    macdSDiffTab = macdSTab.diff()
    macdSDiffTab = macdSDiffTab.reset_index()

    # macdLTab = macdTab["MACDs_12_26_9"]
    # macdLDiffTab = macdLTab.diff()
    # print(macdLDiffTab)

    lenMACDSDiff = len(macdSDiffTab)
    daysUp = 0
    for x in range(3):
        lastMACDSDiff = macdSDiffTab.at[lenMACDSDiff - (x + 1), "MACD_12_26_9"]
        if(lastMACDSDiff > 0):
            daysUp = daysUp + 1
    return(daysUp)

def derivInterpret(dataTab):
    days = macdDeriv(dataTab)
    lastMACDDiff = indicators.getMACDVal(dataTab)
    if(lastMACDDiff < 0):
        if(days == 0):
            return("DOWNWARD TREND UNDER")
        elif (days == 1 or days == 2):
            return("SHAKY TREND UNDER")
        elif (days == 3):
            return("UPWARD TREND UNDER")
        else:
            return("ERROR")
    else:
        if(days == 0):
            return("DOWNWARD TREND OVER")
        elif (days == 1 or days == 2):
            return("SHAKY TREND OVER")
        elif (days == 3):
            return("UPWARD TREND OVER")
        else:
            return("ERROR")