
import numpy as np
import pandas as pd
import yfinance as yf
import time

# Ask the client what stock they want to perform this algorithm on
stock = input("Enter a stock ticker you would like to predict:")

# These will take some fine tuning to get right and therefore should be immutable
period = '30m'
interval = '1m'

# Start up the program
while True:

    # Pull stock data from market
    data = yf.download(tickers= stock, period= period, interval= interval)

    # Calculate the percent change over the specified interval
    perc_change = (((data['Adj Close'][-1] - data['Adj Close'][0]))/data['Adj Close'][0]) * 100

    # If the percent change is a DECREASE and less than 3% over the specified short term interval, we should 
    # consider selling. Before pulling the trigger on selling, lets put this into a Long Short Term Memory
    # machine learning model to predict an outcome. If the outcome is unfavorable, SELL. If the prediction 
    # shows that it may rebound, lets HOLD
    if (perc_change < -3):
        print (stock, "has incurred a percent decrease of ", perc_change, "percent over the course of", period)

        # Implement Long Short Term Memory algorithm
        print("Put in LSTM model to determine whether we should sell")

    # If the percent change is an INCREASE and 5% or more over the specified short term interval, we should 
    # consider buying. Before pulling the trigger on buying, lets put this into a Long Short Term Memory
    # machine learning model to predict an outcome. If the outcome is favorable, BUY. If the prediction 
    # shows that it may trend back down, ignore
    elif(perc_change >= 5):
        print (stock, "has incurred a percent increse of ", perc_change, "percent over the course of", period)

        # Implement Long Short Term Memory algorithm
        print("Put in LSTM model to determine whether we should buy")


    else:
        print(perc_change)
        print("No notable changes. Will try again in two minutes. Going to sleep.....")
    # Execute the program on two minute intervals
    time.sleep(120)





