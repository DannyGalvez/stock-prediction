# stock-prediction

This program will ask the client or a stock they would like to predict over the short term,
and provide help in deciding whether to buy or sell in the matter of minutes or hours. 


To execute this program, you will need the following depencies:

• You must be using python 3.6 or above, and Anaconda
  To download Anaconda, visit https://www.anaconda.com/products/individual

• You must have yahoo finance installed on your machine. Run "pip install yfinance" if you do not have this installed

• For text messaging, this program uses Twilio. You must download Twilio, create an account to generate a phone number,
  Authentification code, and SID to hard code into the program. To do all of this, follow the steps:
  ** NOTE: These steps are taken directly from the Twilio Docs. For more information and troubleshooting, visit 
           https://www.twilio.com/docs/sms/quickstart/python

    1.) Create a Twilio trial account here: https://www.twilio.com/try-twilio
        A trial account will only let you send to a single phone number. If you wish to send to more phone numbers, 
        consider upgrading your account

    2.) Execute the following commands:

        MAC: You will need homebrew installed. If you need to install homebrew, visit https://brew.sh/

            Run the commands:
                brew tap twilio/brew && brew install twilio

                twilio login
                **After running this command, enter your account SID and Authentification token found on your Twilio account console

                pip install twilio

        WINDOWS: You will need Node.js, to install visit https://nodejs.org/en/download/

                Run the commands:
                    PS C:\Windows\system32> Set-ExecutionPolicy Bypass -Scope Process

                    Enter 'Y'

                    npm install twilio-cli -g
        
                    twilio login
                    **After running this command, enter your account SID and Authentification token found on your Twilio account console

                    pip install twilio


        LINUX: Before we can install, we need to make sure you have Node.js installed (version 10.12 or above). Even if you already         installed Node yourself, the CLI works best when you install it using nvm. Here's how to get nvm installed on most Linux systems:

            Run the commands:
                curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash

                nvm install --lts
                nvm use <insert version reported from above>

                **Depending on your distribution, you will need to run one of the following commands:
                    Debian/Ubuntu: sudo apt-get install libsecret-1-dev
                    Red Hat-based: sudo yum install libsecret-devel
                    Arch Linux: sudo pacman -S libsecret

                npm install twilio-cli -g

                twilio login
                **After running this command, enter your account SID and Authentification token found on your Twilio account console

                pip install twilio
