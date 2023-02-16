import requests

# Define the API endpoint URL
API_URL = "http://localhost:6001/sentiment"

# Define the input text
input_text = "This movie is amazing!"

# Send a POST request to the API endpoint with the input text as the request body
response = requests.post(API_URL, json={"text": input_text})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON and print the sentiment result
    sentiment = response.json()["sentiment"]
    print(f"The sentiment of the input text is {sentiment}.")
else:
    # Print an error message if the request was unsuccessful
    print("Error: the API request was unsuccessful.")
