import requests

# Define the URL for the /b2c endpoint
url = "http://localhost:5000/b2c"  # Replace with your actual URL

# Send the POST request
response = requests.post(url)

# Print the response
print("Response Status Code:", response.status_code)
print("Response Content:")
print(response.text)
