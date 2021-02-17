from yelpapi import YelpAPI
from django.conf import settings

def search():
    yelp_api = YelpAPI(settings.YELP_API_KEY)
    yelp_api = YelpAPI(api_key)
    search_results = yelp_api.search_query(category="bbq", location="austin, tx")

    lat=""
    lon=""
    #search_results = yelp_api.search_query(category="bbq", latitude=lat, longitude=lon)
    print(type(search_results))


    for key in search_results:
        #print(key, search_results[key])

        if key=="businesses":
            v = search_results[key]
            return v
            # for business in v:
            #     print(business["name"])

    #object_methods = [method_name for method_name in dir(client)