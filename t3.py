import requests
​
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer KcvjIwBtQCN1e2VMihPFoAAZfdlv'
}
​
payload = {
    "OriginatorConversationID": "4f743d2f-60bf-4fb3-b0e8-9ff8a36e6f67",
    "InitiatorName": "testapi",
    "SecurityCredential": "C5fjdirHnjovO9rPVouo+eAAncd7YN+SEpAqGc7fBbkBBVSCW9eFlFLwaIuMchRFvVkMQ8bRtFFGb/if874vkyAwaXt01QuF6nDmOEMaGUEsASiGQwVSrgMIexl4aAgvbP1tfL7bM93RBFkLtDNDpRUtBso1NBFolMprdTlCFUO7BLI6/vooGlGKaFCWhwHw9thERcRgFfQd5bC0gjqk9gPtbSLBhYaxyJmo0O2X9U/DofVSg1BybferXnfkRFFtWj/OW38KsN0fUlhfCM0LLpKR+8NgMOdIRxAxW9Stz8r3TDPYjlwCP1zKiYHraCZY5prETjs8YSvlNyxvpDl61Q==",
    "CommandID": "SalaryPayment",
    "Amount": 10,
    "PartyA": 600984,
    "PartyB": 254708374149,
    "Remarks": "Test remarks",
    "QueueTimeOutURL": "https://mydomain.com/b2c/queue",
    "ResultURL": "https://mydomain.com/b2c/result",
    "Occasion": "",
  }
​
response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/b2c/v3/paymentrequest', headers = headers, data = payload)
print(response.text.encode('utf8'))