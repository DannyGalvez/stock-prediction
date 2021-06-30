
import numpy as np
import pandas as pd
import yfinance as yf
import time
from pred_stock import pred_stock
import logging

# Configure logging format
logging.basicConfig(filename='errors.log', filemode='w', format='%(asctime)s -%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# For sending SMS notifications. To configure, see Readme file
import os
from twilio.rest import Client

# Read in credentials from a credentials.txt file. These credentials are private and should not be shared,
# so credentials.txt should be specified in your .gitignore file and list each element in the following order
# with no other characters, with each element being on a new line: Account SID, Auth Token, Personal phone number,
# Twilio phone number
f = open('credentials.txt')
SID = str(f.readline())
token = str(f.readline())
deliver_number = str(f.readline())
sender_number = str(f.readline())
f.close()

print(SID, token, deliver_number, sender_number)

# Read in stock tickers from a text file. Also added this file to the gitignore. Structure this file such that each 
# line contains a stock ticker, in all caps, with no added characters or spaces. A pred_stock object will be created 
# for each stock ticker in the file and a thread will be launched to predict the data.
with open('my_stock_tickers.txt') as openfileobject:
    for line in openfileobject:
        try:
            start_thread = pred_stock(SID, token, deliver_number, sender_number, str(line))
            start_thread.start()
            print('Launched thread for ' + str(line))
        except Exception as e:
            logging.error(f"{str(line)} - Exception thrown:", exec_info=True)

    



