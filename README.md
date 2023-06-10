# ADTS (Automated Derivative Technical Screener)

## Overview
A Python Stock Screener primarily utilizing the pandas-ta and scikit-learn libraries to return various technical statistics (i.e. RSI, MACD, OBV, etc.).

Currently v1.0.0.

Created by [tks55](https://github.com/tks55) and [sirrac](https://github.com/sirrac).

## Features
Given a stock input and a given date to start analysis, the program will output numerous economic statistics:

### Technical Indicators:
- RSI
- MACD
- ADX
- Z-score

### Risk Indicators:
- R^2 (via scikit-learn's Linear Regression)
- Residual Deviation (via scikit-learn's Linear Regression, still in development)
- Kurtosis

### Rate of Change Technical Indicators:
- MACD RoC
- OBV

This can also be done automatically, given specific lists for stock market sectors:
- Top 10 Market Share
- Top 10 Technology
- Top 10 Energy
- Top 10 Industrial
- etc.

### Output to CSV
Given automatic data retrival of stock lists, the outputted dataFrame can be further utilized as a CSV file.

## Future Development
### Debugging Residual Deviation:
Testing and debugging the calculated residual deviation for implementation.

### Graphing Indicators:
Displaying Indicators (i.e. RSI, MACD, etc.) on a graph.

### GUI (Graphical User Interface):
Creating a GUI to better improve user experience (as opposed to using a terminal to input/output data).

### Improving CSV Organization:
Creating methods to sort dataFrames before they are outputted to CSV files.
