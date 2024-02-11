from googleapiclient.discovery import build
import googlemaps
import time
import pandas as pd
print(pd.__version__)

# You need to get an API key from Google Cloud Platform and enable the Places API.
api_key = 'AIzaSyA1s9whQHekafdyg9LtcmMZ7tcdl5JxOwM'
query="bookstore near Stanford University"

start_time = time.time()
# Create a client to the Google Maps API.
gmaps = googlemaps.Client(key=api_key)
client_creation_time = time.time() - start_time
print(f"Time to create client: {client_creation_time:.2f} seconds")

# Use the Places API text search to find the Stanford Shopping Center.
places_result = gmaps.places(query=query)

# Create an empty DataFrame to store place details
places_df = pd.DataFrame(columns=['Name', 'Phone Number', 'Address', 'Business Status'])

# Check if any results were returned
if places_result['status'] == 'OK':
    for idx, res in enumerate(places_result['results']):
        
        # Extract the place ID and make a detailed place request
        place_id = res['place_id']
        
        start_time = time.time()
        place_details = gmaps.place(place_id=place_id)  # call another API
        api_call_time = time.time() - start_time
        print("place_details: ", place_details)
        # Extract details from the place
        phone_number = place_details['result'].get('formatted_phone_number', 'Not Available')
        address = place_details['result'].get('formatted_address', 'Not Available')
        business_status = place_details['result'].get('business_status', 'Not Available')
        name = place_details['result'].get('name', 'Not Available')

        # Append the details to the DataFrame
        place_data = {
            'Name': name,
            'Phone Number': phone_number,
            'Address': address,
            'Business Status': business_status
        }
        # As of pandas 2.0, append (previously deprecated) was removed.
        places_df = pd.concat([places_df, pd.DataFrame([place_data])], ignore_index=True)
else:
    print("Place not found.")

# Output the DataFrame to console
print(places_df)