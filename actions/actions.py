# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


f = open('./data/pizza_options.json', encoding="utf8")
pizza_data = json.load(f)
class ActionShowPizzaTypes(Action):
    def name(self) -> Text:
        return "action_show_pizza_types"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = []
        # print(pizza_option_data["Menu"])
        for option in pizza_data['Menu']:
            buttons.append({'title': option['type'],  'payload': '/choose_pizza_type{"pizza_type": "' + option['type'] + '"}'})
        dispatcher.utter_message(text= 'Menu pizza: ', buttons=buttons)
        return []

class ActionShowPizzaFromType(Action):
    def name(self) -> Text:
        return "action_show_pizza_from_type"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = []
        slot_pizza_type = tracker.get_slot('pizza_type')
        for pizza in pizza_data['Menu']:
            if pizza['type'] == slot_pizza_type:
                for p in pizza['pizza']: 
                    buttons.append({'title': p['name'],  'payload': '/choose_pizza{"pizza": "' + p['name'] + '"}'})
                break
        dispatcher.utter_message(text='các loại pizza {}:'.format(slot_pizza_type), buttons = buttons)
        return[]
        
class ActionShowPizzaTopping(Action):
    def name(self) -> Text:
        return "action_show_pizza_toppings"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = []
        for topping in pizza_data['Topping']:
            buttons.append({'title': topping['name'],  'payload': '/choose_topping{"topping": "' + topping['name'] + '"}'})
        dispatcher.utter_message(text='có các loại toppings: ', buttons = buttons)
        return []

class ActionShowPizzaSize(Action):
    def name(self) -> Text:
        return "action_show_pizza_size"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = []
        for size in pizza_data["Size"]:
            buttons.append({'title' : size['name'], 'payload': '/choose_pizza_size{"pizza_size": "' + size['name'] + '"}'})
        dispatcher.utter_message(text='bạn muốn chọn kích cỡ nào cho pizza của bạn ? ', buttons = buttons)
        return []

class ActionGetUserAddress(Action):
    def name(self) -> Text:
        return "action_get_user_address"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        return []

class ActionShowDrinkOptions(Action):
    def name(self) -> Text:
        return "action_show_drink_options"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = []
        for drink in pizza_data["Drink"]:
            buttons.append({'title' : drink['name'], 'payload': '/choose_drink{"drink": "' + drink['name'] + '"}'})
        dispatcher.utter_message(text='danh sách đồ uống', buttons = buttons)
        return []