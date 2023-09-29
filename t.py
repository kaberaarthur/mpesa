from flask import Flask, request, jsonify
import requests
import json
import base64

app = Flask(__name__)

# Define headers
headers = {
    'Content-Type': 'application/json',
  'Authorization': 'Bearer WUWTOcXTSsL4SOWRGaAQt6FZI8fo'
}

# Encode the SecurityCredential using base64
security_credential = "YH2xl7oZfakvHkSCI6ONnyPuD30cWF9wvyXH89G7+orae40/Y3a+4KTuJFYluC4w5F2fEb6pfXCQSZwlrXTIKhDgAVb9HflpPCnBIa9Z74olLkzbJSkWccNqKd/IjqjZRqdBOcldiYcb1PLiND1R/YfsFV6DtFzGd1rJVSa/TeuQNPbl8pKKyoQXp5JQz7a591FiKH4S/382Lslq6xGs/eRe8ESlONub5xPC/bosvZHE3gkZt3X/nyOpMgO+9sthEsDuGdSEV+NAOBhC5WOHmypC2jjQJQtA5PStlnZ9kpxDex5UF7WUOqYRfEGmqkjGK23YJM9wBZYzZqq6Gb2a8w=="
encoded_security_credential = base64.b64encode(security_credential.encode()).decode()

# Define Ngrok URL
ngrok_url = "https://5358-105-163-158-150.ngrok-free.app"

# Define the B2C route and function
@app.route('/b2c', methods=['POST'])
def b2c():
    # Payload data
    payload = {
        "OriginatorConversationID": "0e52a8e4-1c4a-4633-b908-258b43832748",
        "InitiatorName": "testapi",
        "Password": "Safaricom999!*!",
        #"InitiatorPassword": "Safaricom999!*!",
        "SecurityCredential": "B2MS/aDktT/PsaoA0KPBZjriefE2IQGq5nWpFkB0NoERooYhGORB2SmWAtiikTUd5R9hSt3oltETHTKK7gUk9b9giD0+X3WpBMQiaVWF3LBXZAdzzOb0tLf4562ZIQGeWh5ja6p1nrRF1HLN1SUVTUUUCqhClbYgS24GqFfuRleaG8S+dd60fuDR8s6qLqW5/bwiaE/uNZPrtQ6FDFFZPdL6H/jhK87+hyoqk5jY7HVzhQiS636nyjAE79UL5LoLysxjPZerk4q52hrHVf7KnBCqrCYF5zDY+Mgrc2/8vAQvjyyXIxDbOFsJVmiEBZ/BRbE31LE4PpN+06mJoifHFA==",
        "CommandID": "SalaryPayment",
        "Amount": 10,
        "PartyA": 600977,
        "PartyB": 254708374149,
        #"PhoneNumber": 254708374149,
        "BusinessShortCode": 174379,
        "Remarks": "Test remarks",
        "QueueTimeOutURL": f"{ngrok_url}/timeout",
        "ResultURL": f"{ngrok_url}/cb",
        "Occasion": "Driver Withdraw Funds",
        "PassKey": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    }

    # URL to send the request to
    url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"

    # Authentication string
    auth = headers['Authorization']

    # Send the request
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    return response.text, response.status_code

# Define the timeout route and function
@app.route('/timeout', methods=['POST'])
def timeout():
    print("--- request timeout ----")
    request_data = request.json
    print(request_data)
    print("--- end of request timeout ---")
    return jsonify({'message': 'Request timeout received'}), 200

# Define the callback route and function
@app.route('/cb', methods=['POST'])
def cb():
    print("--- callback request ----")
    request_data = request.json
    response = request_data.get('Result', {})

    if 'ResultParameters' in response:
        response['ResultParameters'] = response['ResultParameters'].get('ResultParameter')

    if 'ReferenceData' in response:
        response['ReferenceData'] = response['ReferenceData'].get('ReferenceItem')

    print(response)
    print("--- end of callback request ---")
    return jsonify({'message': 'Callback request received'}), 200

# Define the callback route and function
@app.route('/test', methods=['GET'])
def test():
    print("--- Success Get Request ----")
    return jsonify({'message': 'Get request received'}), 200
    

if __name__ == '__main__':
    app.run(port=5000)  # Change the port as needed
