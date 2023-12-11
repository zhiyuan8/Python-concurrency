from src.gmaps import Gmaps

queries = [
   "bookstore and gift shops near Stanford University",
]

fields = [
   Gmaps.Fields.PLACE_ID, 
   Gmaps.Fields.NAME,
   Gmaps.Fields.PHONE, 
   Gmaps.Fields.ADDRESS,
   Gmaps.Fields.LINK,
   Gmaps.Fields.DESCRIPTION,
   Gmaps.Fields.MAIN_CATEGORY, 
   # Gmaps.Fields.RATING, 
   # Gmaps.Fields.REVIEWS, 
   Gmaps.Fields.WEBSITE, 
]

# You can scrape a maximum of 120 leads per search
res = Gmaps.places(queries, sort=[Gmaps.  DEFAULT_SORT], fields=fields, has_phone=True, key="AIzaSyA1s9whQHekafdyg9LtcmMZ7tcdl5JxOwM")
print(res)