import pandas as pd
import numpy
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas_ta as ta
import mplfinance as mpl
from sklearn.linear_model import LinearRegression

def getY(dataTab):
    data = dataTab
    data = data["Close"]
    y = numpy.array(data)
    return(y)

def getX(dataTab):
    y = getY(dataTab)
    xLen =  xLen = y.size
    x = numpy.arange(xLen)    
    #y = y.reshape(-1, 1)
    x = x.reshape(-1, 1)
    return(x)

def getModel(dataTab):
    x = getX(dataTab)
    y = getY(dataTab)
    model = LinearRegression().fit(x, y)
    return(model)

def getR2(dataTab):
    x = getX(dataTab)
    y = getY(dataTab)
    model = getModel(dataTab)
    rSqVal = model.score(x, y)
    return(rSqVal)

def getPredictions(dataTab):
    x = getX(dataTab)
    model = getModel(dataTab)
    predictions = model.predict(x)
    return(predictions)
    
def getResiduals(dataTab):
    yTrue = getY(dataTab)
    yPredicted = getPredictions(dataTab)
    residuals = numpy.subtract(yPredicted, yTrue)
    return(residuals)

def getAbsoluteResid(dataTab):
    residual = getResiduals(dataTab)
    absoluteResid = numpy.absolute(residual)
    return(absoluteResid)

def getMean(dataTab):
    absoluteResid = getAbsoluteResid(dataTab)
    mean = numpy.mean(absoluteResid)
    return(mean)

def getSTD(dataTab):
    residual = getResiduals(dataTab)
    std = numpy.std(residual)
    return(std)

def getSTDResidual(dataTab):
    meanResid = getMean(dataTab)
    stdResid = getSTD(dataTab)
    avgResidSTD = meanResid/stdResid
    return(avgResidSTD)