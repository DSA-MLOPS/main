import requests
import streamlit as st

# Define the API endpoint URL
API_URL = "http://localhost:6001/sentiment"

# Define the CSS styles for the sentiment result display
POSITIVE_STYLE = "color: green; font-weight: bold"
NEGATIVE_STYLE = "color: red; font-weight: bold"

# Define the Streamlit app
def app():
    # Define the app title and text input
    st.title("Sentiment Analysis")
    input_text = st.text_input("Enter some text:")

    # Check if the user has entered any input text
    if input_text:
        # Send a POST request to the API endpoint with the input text as the request body
        response = requests.post(API_URL, json={"text": input_text})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON and get the sentiment result
            sentiment = response.json()["sentiment"]

            # Set the sentiment result display style based on the sentiment
            if sentiment == "positive":
                sentiment_style = POSITIVE_STYLE
            else:
                sentiment_style = NEGATIVE_STYLE

            # Display the sentiment result with the appropriate style
            st.markdown(f"Sentiment: <span style='{sentiment_style}'>{sentiment}</span>", unsafe_allow_html=True)
        else:
            # Display an error message if the request was unsuccessful
            st.error("Error: the API request was unsuccessful.")

# Run the Streamlit app
if __name__ == "__main__":
    app()