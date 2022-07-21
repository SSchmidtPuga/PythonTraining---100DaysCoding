##################### Extra Hard Starting Project ######################
import random

import pandas as pd
import datetime as dt
import smtplib

my_email = "spuga123@gmail.com"
password = "ss12721272"

birthdays = pd.read_csv("birthdays.csv")
months = birthdays.month.tolist()
days = birthdays.day.tolist()
names = birthdays.name.tolist()
emails = birthdays.email.tolist()

now = dt.datetime.now()
day_of_the_week = now.day
month = now.month




new_letter = []
email = []
send_email = False

for n in range(0, len(months)):
    if month == int(months[n]):
        if day_of_the_week == int(days[n]):
            name = names[n]
            email = emails[n]

            with open("letter_templates/letter_1.txt") as file1:
                letter1 = file1.read()
            with open("letter_templates/letter_2.txt") as file2:
                letter2 = file2.read()
            with open("letter_templates/letter_3.txt") as file3:
                letter3 = file3.read()

            letters = [letter1, letter2, letter3]
            random_letter = random.choice(letters)
            print(type(random_letter))
            new_letter = random_letter.replace("[NAME]", name)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="spuga123@gmail.com",
                    msg=f"Feliz Cumpleanos\n\n {new_letter}"
                )
