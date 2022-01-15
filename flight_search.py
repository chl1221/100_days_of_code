import requests
import datetime as dt
from flight_data import FlightData
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.tomorrow = dt.date.today() + dt.timedelta(days=1)
        self.sixmonth = dt.date.today() + dt.timedelta(days=180)
        self.locationurl = os.environ["locationurl"]
        self.searchurl = os.environ["searchurl"]
        self.headers = {"apikey": os.environ["apikey"]}
    
    def get_code(self, city: str) -> str:
        parameter = {
            "term": city, 
            "location_types": "city"
        }
        response = requests.get(url=self.locationurl, params=parameter, headers=self.headers)
        return response.json()["locations"][0]["code"]

    def get_flight(self, iata_code) -> object:
        parameter = {
            "fly_from": "LON", 
            "fly_to": iata_code, 
            "date_from": f"{self.tomorrow.strftime('%d/%m/%Y')}",
            "date_to": f"{self.sixmonth.strftime('%d/%m/%Y')}",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(url=self.searchurl, params=parameter, headers=self.headers)
        try:
            flight = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {iata_code}.")
            return None

        flight_data = FlightData(
            price=flight["price"], 
            origin_city=flight["route"][0]["cityFrom"],
            origin_airport=flight["route"][0]["flyFrom"],
            destination_city=flight["route"][0]["cityTo"],
            destination_airport=flight["route"][0]["flyTo"],
            out_date=flight["route"][0]["local_departure"].split("T")[0],
            return_date=flight["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data

# yyo = FlightSearch()
# alist = ["PAR"]
# blist = ["PAR", "BER", "TYO", "JFK"]
# for city in blist:
#     yyo.get_flight(city)