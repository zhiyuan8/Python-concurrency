from src.gmaps import Gmaps

queries = [
   "bookstore near Stanford University",
]

Gmaps.places(queries, max=5)