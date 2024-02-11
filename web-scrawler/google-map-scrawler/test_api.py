from googleapiclient.discovery import build
import googlemaps

# You need to get an API key from Google Cloud Platform and enable the Places API.
api_key = 'AIzaSyA1s9whQHekafdyg9LtcmMZ7tcdl5JxOwM'

# Create a client to the Google Maps API.
gmaps = googlemaps.Client(key=api_key)

# Use the Places API text search to find the Stanford Shopping Center.
places_result = gmaps.places(query="Stanford Shopping Center")

# Check if any results were returned
if places_result['status'] == 'OK':
    # Assuming the first result is the desired one
    first_result = places_result['results'][0]
    
    # Extract the place ID and make a detailed place request
    place_id = first_result['place_id']
    place_details = gmaps.place(place_id=place_id)

    # Extract the phone number and address from the detailed place result
    phone_number = place_details['result'].get('formatted_phone_number', 'Not Available')
    address = place_details['result'].get('formatted_address', 'Not Available')

    print(f'Phone Number: {phone_number}')
    print(f'Address: {address}')
else:
    print("Place not found.")