import smtplib
import os

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
   
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date) -> None:
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def send_email(self) -> None:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs="chenghsuanli@umass.edu", 
                msg=f"Subject:Low Price alert!\n\nOnly ${self.price} to fly from\
                     {self.origin_airport} to {self.destination_airport},from {self.out_date}\
                          to {self.return_date}"
            )