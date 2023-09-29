import requests
import base64

# Your Consumer Key and Consumer Secret
consumer_key = 'lg29XgGR4k36DpHMnTmKuGwxqRVBU3NX'
consumer_secret = 'PsQM38icXediD9Ab'

# Encode the credentials in Base64
credentials = f"{consumer_key}:{consumer_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Define the headers with Basic Authentication
headers = {
    'Authorization': f'Basic {encoded_credentials}'
}

# Make the request
url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
response = requests.get(url, headers=headers)

# Print the response
print(response.text)
