import yfinance as yf
import time
import threading
# For sending SMS notifications. To configure, see Readme file
import os
from twilio.rest import Client
import logging

# Configure logging format
logging.basicConfig(filename='stock_log.log', filemode='w', format='%(asctime)s -%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

# Launch a new thread for each stock
class pred_stock(threading.Thread):
    
    # Constructor, takes in all necessary information from base class
    def __init__(self, SID, token, deliver_to, send_from, stock):
        threading.Thread.__init__(self)
        self.SID = SID
        self.token = token
        self.deliver_to = deliver_to
        self.send_from = send_from
        self.stock = stock

    # Launch the thread
    def run(self):
        SID = self.SID
        token = self.token
        deliver_to = self.deliver_to
        send_from = self.send_from
        stock = self.stock

        client = Client(self.SID, self.token)

        # These will take some fine tuning to get right and therefore should be immutable
        period = '30m'
        interval = '5m'

        # Start up the program
        while True:

            # Pull stock data from market
            data = yf.download(tickers= stock, period= period, interval= interval)

            # Calculate the percent change over the specified interval
            perc_change = (((data['Adj Close'][-1] - data['Adj Close'][0]))/data['Adj Close'][0]) * 100
            logging.info(f"{stock} - 30 minutes ago this stock was: " + str(data['Adj Close'][0]) + " Currently, this stock is: " + str(data['Adj Close'][-1]))
         



            # If the percent change is a DECREASE and less than 3% over the specified short term interval, we should 
            # consider selling. Before pulling the trigger on selling, lets put this into a Long Short Term Memory
            # machine learning model to predict an outcome. If the outcome is unfavorable, SELL. If the prediction 
            # shows that it may rebound, lets HOLD
            if (perc_change < -2):
                logging.info(f"{stock} - Has incurred a percent decrease of " + str(perc_change) + " percent over the course of " + str(period))

                # Implement Long Short Term Memory algorithm
                #print("Put in LSTM model to determine whether we should sell")

                # Change the "from_" number to your Twilio number and the "to" number
                # to the phone number you signed up for Twilio with, or upgrade your
                # account to send SMS to any phone number
                client.messages.create(to = deliver_to, 
                                    from_ = send_from, 
                                    body = "----SELL NOTICE FROM STOCK AI---- \n Your stock " + str(stock) + " has decreased " + str(perc_change) + " percent in the past " + str(period) + " and is predicted to keep falling. Consider SELLING now.")

                #print("Going to sleep for 10 minutes...")
                time.sleep(600)
                continue

            # If the percent change is an INCREASE and 5% or more over the specified short term interval, we should 
            # consider buying. Before pulling the trigger on buying, lets put this into a Long Short Term Memory
            # machine learning model to predict an outcome. If the outcome is favorable, BUY. If the prediction 
            # shows that it may trend back down, ignore
            elif(perc_change >= 3):
                logging.info(f"{stock} - Has incurred a percent increase of " + str(perc_change) + " percent over the course of " + str(period))

                # Implement Long Short Term Memory algorithm
                #print("Put in LSTM model to determine whether we should buy")

                # Change the "from_" number to your Twilio number and the "to" number
                # to the phone number you signed up for Twilio with, or upgrade your
                # account to send SMS to any phone number
                client.messages.create(to = deliver_to, 
                                    from_ = send_from, 
                                    body = "----BUY NOTICE FROM STOCK AI---- \n Your stock " + str(stock) + " has increased " + str(perc_change) + " percent in the past " + str(period) + " and is predicted to keep rising. Consider BUYING now.")
            
                #print("Going to sleep for 10 minutes...")
                time.sleep(600)
                continue

            else:
                logging.info(f"{stock} - No notable changes. Will try again in two minutes. Going to sleep.....")
            # Execute the program on two minute intervals
            time.sleep(120)