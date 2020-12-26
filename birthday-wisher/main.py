##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

my_email = "email@gmail.com"
passw = "your_password"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
bday = data[(data.month == today.month) & (data.day == today.day)]# in pandas use bitwise operator &(and) |(or) for logical operation
name = bday["name"].to_string(index=False)
email = bday["email"].to_string(index=False)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

num = random.randint(1,3)
with open(f"letter_templates/letter_{num}.txt") as letter:
    lines = letter.readlines()
    lines[0].strip()
    lines[0] = lines[0].replace("[NAME]", name)
    message = "".join(lines)


# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=passw)
    connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: HAPPY BIRTHDAY\n\n{message}")
