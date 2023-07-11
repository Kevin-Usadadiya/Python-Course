travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, lists):
    travel_log.append(
        {'country' : country,
         'visits' : visits,
         'cities' : lists
                       })




add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("India", 3, ["Gujarat", "Madhya Pradesh"])
print(travel_log)