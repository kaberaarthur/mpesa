import requests
import base64

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer mahkferD1e1xdfAdbOuJtGyMNtvE'
}

# Encode the SecurityCredential using base64
security_credential = "U3mM3riB6fzEkyG0mGYZvBMWvpRybtbY8mQrMZp6Nx9gMU1IZW9pawiyA4vXat7eldYGtk7rpn0kOkvrPhT8G7wZyvXVSYHzCw61WW+YKNM6goY5BeOCNVCkjqgHsZA5XPwjtseWG1ucnAvgak7k61SHcyqQcphJKWezBml0WxVl/1jsfrCeUOmw3qZXO47mfI/TPZeROUTpktUK25yuRISxo4/ZnJ6NEhnTAjAE4duD8IiHKT7X4pl+5pJ1RYaA526UA782LlcQLUHSaW0XHf/OEswsHK4NDv7LtMxZr87Nnx3XlQ/6nYI7uka6ybtEO0e0oUVYDKMbY9eqLjEaAA=="
encoded_security_credential = base64.b64encode(security_credential.encode()).decode()


ngrok_url = "https://ddf3-105-163-156-156.ngrok-free.app"

payload = {
    "OriginatorConversationID": "63591a2b-1418-4061-b012-9b6438a6377d",
    "InitiatorName": "testapi",
    "SecurityCredential": encoded_security_credential,
    "CommandID": "SalaryPayment",
    "Amount": 10,
    "PartyA": 600981,
    "PartyB": 254708374149,
    "Remarks": "Test remarks",
    "QueueTimeOutURL": ngrok_url + "/timeout",
    "ResultURL": ngrok_url + "/cb",
    "Occasion": "Driver Withdraw Funds",
}

response = requests.request("POST", ngrok_url, headers=headers, json=payload)
print(response.text)
