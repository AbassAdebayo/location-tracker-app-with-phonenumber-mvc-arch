import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import requests
from . import settings


class LocationTrackerConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'location_tracker'
        
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
            
        )
        
        self.accept()
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
           self.group_name,
           self.channel_name
            
        )
        
    def receive(self, text_data):
        data = json.loads(text_data)
        phone_number = data["phone_number"]
        
        
        location_details = self.get_location_details(phone_number)
        
        self.send(text_data=json.dumps({
            
            'location': location_details
        }))
        
    def get_location_details(self, phone_number):
        
        ipinfo_url = f'https://ipinfo.io/json?token={settings.IPINFO_API_TOKEN}'
        ipinfo_response = requests.get(ipinfo_url)

        if ipinfo_response.status_code == 200:
            ipinfo_data = ipinfo_response.json()
            location = ipinfo_data.get('loc')
            if location:
                lat, lng = location.split(',')
                return {
                    'latitude': lat,
                    'longitude': lng,
                    'city': ipinfo_data.get('city'),
                    'region': ipinfo_data.get('region'),
                    'country': ipinfo_data.get('country')
                }
            else:
                error_message = "Error: No location data found in IPinfo response."
        else:
            error_message = f"Error: Unable to retrieve IPinfo data. Status code: {ipinfo_response.status_code}"
                    