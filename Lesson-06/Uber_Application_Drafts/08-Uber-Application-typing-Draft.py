from typing import Dict, List
"""
user['history']  LIST

LIST-item = booked_ride = {}

user['history'] = [{"Service":service_name, "Distance":distance,"Total price":total}, ]

enumerate(user['history']) = [(1,{"Service":service_name, "Distance":distance,"Total price":total}),(2, {"Service":service_name, "Distance":distance,"Total price":total} ]
"""
service_name = "Uber"
distance = 10
total= 20.00

user: Dict[str, List[Dict[str, str|int|float]]] = {
    "preference":"",
    "history":[]
}
booked_ride = {
    "Service": service_name,
    "Distance": distance,
    "Total price": total
}

user['history'].append(booked_ride)
for id_number, item in enumerate(user['history']):
    print(type(item))
    print(id_number, item['Service']) # 'Service' heeft GEEN gele streep meer

print(user['history'])

#from typing import Dict, List
#"""
#user['history']  LIST

#LIST-item = booked_ride = {}

#user['history'] = [{"Service":service_name, "Distance":distance,"Total price":total}, ]

#enumerate(user['history']) = [(1,{"Service":service_name, "Distance":distance,"Total price":total}),(2, {"Service":service_name, "Distance":distance,"Total price":total} ]
#"""
#service_name = "Uber"
#distance = 10
#total= 20.00

#user: Dict[str, List[Dict[str, str, str]]] = {
#    "preference":"",
#    "history":[]
#}
#booked_ride = {
#    "Service": service_name,
#    "Distance": distance,
#    "Total price": total
#}

#user['history'].append(booked_ride)
#for id_number, item in enumerate(user['history']):
#    print(type(item))
#    print(id_number, item['Service']) # 'Service' heeft nog steeds gele streep

#print(user['history'])