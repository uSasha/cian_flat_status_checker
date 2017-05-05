## Script will, login, navigate to correct page, search and match, then email result.
# -*- coding: utf-8 -*- 

# to use it fill in all these variables
reciever_email = 'example@world.io'   # you can write many sepparated by comma
sender_gmail = 'robohelper@gmail.com' # this one should be gmail
sender_password = 'example_password'
ad_url = 'https://www.cian.ru/sale/flat/155647738/'
# here your email password will be visible to anyone

import re
import urllib
import smtplib
import requests
from datetime import datetime
from threading import Timer


def check_cian():
    print "checking..."

    message = "Warning, it seems your advert is no longer available. \r\n Please check this URL: "
    marker = unicode("Объявление снято с публикации","utf-8")

    # sending cookies as well
    s = requests.session()
    result = s.get(ad_url)
    result = result.text
    match1 = re.findall(marker, result)    #we are trying to find marker in "result2"

    if len(match1) == 1:                       #if we find a match
        # send text from gmail account
        body = "" + message + "" + str(url)

        headers = ["From: " + 'Good robot',
                   "Subject: " + 'Cian status',
                   "To: " + 'reciever_email',

                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        session = smtplib.SMTP('smtp.gmail.com', '587')

        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(sender_gmail, sender_password)

        session.sendmail('Robot', reciever_email, headers + "\r\n\r\n" + body)
        session.quit()
    
    print 'done'

# to run it periodically use cron
# simply put script to /home and run in terminal: 
# crontab -e
# and then to run script everyday at 6.00
# 0 6 * * * python /home/cian_ad_check.py
# more details https://ru.wikipedia.org/wiki/Cron 