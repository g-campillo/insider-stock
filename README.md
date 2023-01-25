# Insider Stock Trades Tracker

### Goal
Whenever a person of high-rank (CEO, CFO, Director, etc.) purchases a share of their company they are legally required to report an SEC 4 form. This form contains information such as how much of the stock was purchased, what price, who purchased and many other things. 

This service is a web scraper that downloads the most recent trade data from `openinsider.com`. The information is sorted by when the trade was executed such that the most recent trades are shown. 

It will send an email to a certain list of specified users when new trades are detected. This service does not rely on a database as it only keeps a specified maximum number of objects in memory (the default is 100). 

### Requirements
To be able to run the service, you must download [Docker Desktop](https://www.docker.com/products/docker-desktop/).

### Setting up your `.env` file
In the project directory, you must create a `.env` file with the following variables:
```
STOCK_URL=http://openinsider.com/screener # Do not change this

EMAIL_USER= #the email address that will be used to send emails
EMAIL_PASSWORD= #the password of the email address
EMAIL_HOST= #the host that will be used to send the email
EMAIL_PORT= #smtp port
EMAIL_SUBJECT= #the subject for the email that will be sent
EMAIL_RECIPIENTS= #comma delimited list of email addresses to receive the updates

ARGS_SLEEP_INTERVAL=60 #amount of seconds to wait between each check of the site
ARGS_LOG_LEVEL=info #log level output (info | debug)
```

### Running the service
Once you've installed Docker and setup your `.env` file, run the following command:

```
docker compose up
```