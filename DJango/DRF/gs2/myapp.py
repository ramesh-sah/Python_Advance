import requests
import json

# Define the URL for student creation
URL = "http://127.0.0.1:8080/stucreate/"

# Data to be sent in the request
data = {
    'name': 'sonam',
    'roll': '300',
    'city': 'ranchi'
}

# Convert data to JSON format
json_data = json.dumps(data)

try:
    # Send a POST request to the specified URL with JSON data
    response = requests.post(url=URL, data=json_data)

    # Check if the response contains JSON content
    if response.headers['content-type'] == 'application/json':
        # Parse and print the JSON response
        parsed_data = response.json()
        print(parsed_data)
    else:
        # Print the response content if not JSON
        print(response.content)

except requests.exceptions.JSONDecodeError as e:
    # Handle JSON decoding error
    print(f'JSON Decode Error: {e}')
except requests.exceptions.RequestException as e:
    # Handle other request-related errors
    print(f'Request Error: {e}')
