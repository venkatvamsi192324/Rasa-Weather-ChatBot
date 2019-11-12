from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import requests

class ActionBot(Action):
    def name(self):
        return 'action_bot'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '14a328516096bd4fd27444f714f9d8a9'
        #client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        api_address='http://api.apixu.com/v1/current.json?key={}&q={}'.format(api_key,loc)
        current = requests.get(api_address).json()





        
        #current = client.getcurrent(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. The temperature is {} degrees and the wind speed is {} mph.""".format(condition,city,temperature_c,wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]