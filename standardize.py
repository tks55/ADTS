import indicators

def standardRSI(dataTab):
    currentRSI = indicators.getRSIVal(dataTab)
    meanRSI = indicators.getRSIMean(dataTab)
    stdRSI = indicators.getRSISTD(dataTab)
    zNum = currentRSI - meanRSI
    zScore = zNum/stdRSI
    return(zScore)

def standardMACD(dataTab):
    currentMACD = indicators.getMACDVal(dataTab)
    meanMACD = indicators.getMACDMean(dataTab)
    stdMACD = indicators.getMACDSTD(dataTab)
    zNum = currentMACD - meanMACD
    zScore = zNum/stdMACD
    return(zScore)

def standardADXD(dataTab):
    currentADXD = indicators.getADXVal(dataTab)
    meanADXD = indicators.getADXDMean(dataTab)
    stdADXD = indicators.getADXDSTD(dataTab)
    zNum = currentADXD - meanADXD
    zScore = zNum/stdADXD
    return(zScore)