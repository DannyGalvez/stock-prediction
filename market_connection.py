
import numpy as np
import pandas as pd
import yfinance as yf
import time

# For sending SMS notifications. To configure, see Readme file
import os
from twilio.rest import Client
# Must create an account via Twilio. Upon account creation, you will be given 
# an Account SID which is the first parameter, and a token
client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

# Ask the client what stock they want to perform this algorithm on
stock = input("Enter a stock ticker you would like to predict:")

# These will take some fine tuning to get right and therefore should be immutable
period = '30m'
interval = '5m'

# Start up the program
while True:

    # Pull stock data from market
    data = yf.download(tickers= stock, period= period, interval= interval)

    # Calculate the percent change over the specified interval
    perc_change = (((data['Adj Close'][-1] - data['Adj Close'][0]))/data['Adj Close'][0]) * 100
    print("30 minutes ago,", stock,"was:", data['Adj Close'][0])
    print("Currently,", stock,"is:", data['Adj Close'][-1])


    # If the percent change is a DECREASE and less than 3% over the specified short term interval, we should 
    # consider selling. Before pulling the trigger on selling, lets put this into a Long Short Term Memory
    # machine learning model to predict an outcome. If the outcome is unfavorable, SELL. If the prediction 
    # shows that it may rebound, lets HOLD
    if (perc_change < 0):
        print (stock, "has incurred a percent decrease of ", perc_change, "percent over the course of", period)

        # Implement Long Short Term Memory algorithm
        print("Put in LSTM model to determine whether we should sell")

        # change the "from_" number to your Twilio number and the "to" number
        # to the phone number you signed up for Twilio with, or upgrade your
        # account to send SMS to any phone number
        client.messages.create(to="+13157508492", 
                            from_="+12532013628", 
                            body="----NOTICE FROM STOCK PREDICTION AI---- \n Your stock " + str(stock) + " has decreased" + str(perc_change) + " percent in the past " + str(period) + " and is predicted to keep falling. Consider SELLING now.")



    # If the percent change is an INCREASE and 5% or more over the specified short term interval, we should 
    # consider buying. Before pulling the trigger on buying, lets put this into a Long Short Term Memory
    # machine learning model to predict an outcome. If the outcome is favorable, BUY. If the prediction 
    # shows that it may trend back down, ignore
    elif(perc_change >= 0):
        print (stock, "has incurred a percent increse of ", perc_change, "percent over the course of", period)

        # Implement Long Short Term Memory algorithm
        print("Put in LSTM model to determine whether we should buy")

        # change the "from_" number to your Twilio number and the "to" number
        # to the phone number you signed up for Twilio with, or upgrade your
        # account to send SMS to any phone number
        client.messages.create(to="+13157508492", 
                            from_="+12532013628", 
                            body="----NOTICE FROM STOCK PREDICTION AI---- \n Your stock " + str(stock) + " has increased " + str(perc_change) + " percent in the past " + str(period) + " and is predicted to keep rising. Consider BUYING now.")


    else:
        print(perc_change)
        print("No notable changes. Will try again in two minutes. Going to sleep.....")
    # Execute the program on two minute intervals
    time.sleep(120)





