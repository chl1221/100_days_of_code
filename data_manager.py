from inspect import Parameter
import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.data = {}
        self.posturl = os.environ["posturl"]
        self.puturl = os.environ["puturl"]

    def fetch(self) -> list:
        response = requests.get(url=self.posturl)
        response.raise_for_status()
        data = response.json()
        self.data = data["prices"]
        return self.data
    
    def update_iata(self):
        for row in self.data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=f"{self.puturl}/{row['id']}", json=new_data)
            # print(response.text)
