import datetime as dt
import smtplib
import random

my_email = "email@gmail.com"
passw = "your_password"

today = dt.datetime.now().weekday()
day=""

if today == 0:
    day = "Monday"
elif today == 1:
    day = "Tuesday"
elif today == 2:
    day = "Wednesday"
elif today == 3:
    day = "Thursday"
elif today == 4:
    day = "Friday"
elif today == 5:
    day = "Saturday"
else:
    day = "Sunday"

with open("quotes.txt") as file:
    quotes = file.readlines()
    random_quote = random.choice(quotes)
    message = f"Subject: {day} Motivation Quote\n\n{random_quote}"
    message = message.encode("utf-8")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passw)
        connection.sendmail(from_addr=my_email, to_addrs="targetted_email@gmail.com", msg=message)




#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=passw)
#     connection.sendmail(from_addr=my_email, to_addrs="hawkempire007@gmail.com", msg="Subject: hello\n\nThis is the body")
#

