from yelpapi import YelpAPI
from django.conf import settings

import json

def search(api_key, latitude, longitude, term):
    yelp_api = YelpAPI(api_key)
    # search_results = yelp_api.search_query(category="bbq", location="austin, tx", term="pulled pork")
    
    lat=latitude
    lng=longitude
    print(lat, lng)
    search_results = yelp_api.search_query(category="bbq", latitude=lat, longitude=lng, term=term)

    nameList = []
    coordinateList = []
    phoneList = []
    restaurantList = []

    for key in search_results:
        if key=="businesses":
            v = search_results[key]
            for business in v:
                name = business["name"]
                coordinates = business["coordinates"]
                location = business["location"]
                phone = business["phone"]
                rating = business["rating"]

                nameList.append(name)

                lat = coordinates["latitude"]
                lng = coordinates["longitude"]

                coordinateList.append( (lat, lng) )
                phoneList.append(phone)

                dictionary={
                    "name":business["name"],
                    "location":business["location"],
                    "phone":business["phone"],
                    "laty":lat,
                    "lonx":lng,
                }
                restaurantList.append(dictionary)
    i = 0
    jsstring = ""
    while i < len(nameList):
        coordinates = coordinateList[i]
        jsstring+="const myCoordinates"+str(i)+" = { lat:"+ str(coordinates[0])+ ", lng:"+ str(coordinates[1])+ "};"
        i += 1

    numItems = i

    i = 0
    while i < numItems:
        jsstring+="new google.maps.Marker({ position: myCoordinates"+ str(i) +", map, title: \"\" });"
        i += 1

    # with open("search.json", "w") as outfile: 
    #     json.dump(restaurantList, outfile)

    return search_results, jsstring
            #for business_key in business:
            #    business_value = business[business_key]
            #    print(business_key, business_value)
            #print("-----")


    # print(type(search_results))


    # for key in search_results:
    #     #print(key, search_results[key])

    #     if key=="businesses":
    #         v = search_results[key]
    #         # return v
    #         for business in v:
    #             print(business["name"])

# search()
    #object_methods = [method_name for method_name in dir(client)