
import configuration

import requests

import data

def new_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=order_body,
                         headers=data.headers)

def get_orders_track():
   response = new_order(data.order_body)
   track = str(response.json()["track"])
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK + '?t=' + track)
#response = get_orders_track()