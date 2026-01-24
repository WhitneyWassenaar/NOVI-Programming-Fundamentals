"""
---Summary---
This file explores the difference between using a dictionary and a list of tuples for booked_ride in user['history'].

In the first version, booked_ride is stored as a dictionary and added to user['history']. Accessing specific items with item['Service'] can trigger IDE warnings, because the presence of keys is not guaranteed at runtime.

In the second version, booked_ride is converted to a list of tuples ([("Service", value), ...]). This allows specific values to be accessed directly via indices (booked_ride[0][1], booked_ride[1][1]), which is fully predictable for the IDE and avoids warnings.

Conclusion:
Changing booked_ride from a dictionary to a list allows safe, index-based access to specific items without IDE warnings.

---End---

user['history']  LIST

LIST-item = booked_ride = {}

user['history'] = [{"Service":service_name, "Distance":distance,"Total price":total}, ]

enumerate(user['history']) = [(1,{"Service":service_name, "Distance":distance,"Total price":total}),(2, {"Service":service_name, "Distance":distance,"Total price":total} ]
"""
service_name = "Uber"
distance = 10
total= 20.00

user = {
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
    print(id_number, item['Service'])

print(user['history'])

service_name = "Uber"
distance = 10
total= 20.00

user = {
    "preference":"",
    "history":[]
}
booked_ride = [("Service", service_name),("Distance", distance),("Total price", total)]

user['history'].append(booked_ride)

for id_number, booked_ride in enumerate(user['history'], start=1):
    print(id_number, booked_ride[0][1])
    print(id_number, booked_ride[1][1])
    print(id_number, booked_ride[2][1])

print(booked_ride)

