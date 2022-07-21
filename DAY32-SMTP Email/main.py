# import smtplib
#
# my_email = "spuga123@gmail.com"
# password = "ss12721272"
#
import datetime as dt
import random
#
with open("quotes.txt") as file:
    all_contents = file.readlines()
    random_quote = random.choice(all_contents)

#
#
# now = dt.datetime.now()
# day_of_the_week = now.weekday()
#
# if day_of_the_week == 3:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr = my_email,
#                             to_addrs = "spuga123@gmail.com",
#                             msg =f"Subject: Hoy es un gran dia \n\n {random_quote}")





# date_of_birth = dt.datetime(year=1998, month=8, day=18)
lost = [1,2,3,4,5]


for n in range(len(lost)-1):
    print(n)