from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()

# check the sheet and update IATA code if there is no code
for row in data_manager.fetch():
    if row["iataCode"] == "":
        flightsearch = FlightSearch()
        row["iataCode"] = flightsearch.get_code(row["city"])
data_manager.update_iata()
# print(data_manager.data)
for row in data_manager.data:
    flightsearch = FlightSearch()
    flight = flightsearch.get_flight(row["iataCode"])
    if flight and flight.price < row["lowestPrice"]:
        new_mail = NotificationManager(flight.price, flight.origin_city, flight.origin_airport, flight.destination_city, flight.destination_airport, flight.out_date, flight.return_date)
        new_mail.send_email()