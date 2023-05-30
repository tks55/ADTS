import indicators
import standardize

def calculate(dataTab):
    sRSI = standardize.standardRSI(dataTab)
    sMACD = standardize.standardMACD(dataTab)
    sADXD = standardize.standardADXD(dataTab)
    zscore = indicators.getZSCORE(dataTab)
    adx = indicators.getADXVal(dataTab)/40
    value = adx * (sRSI + sMACD + sADXD + zscore)
    return(value)