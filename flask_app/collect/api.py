import json
import requests
import base64

authUrl = "https://accounts.spotify.com/api/token"
authHeader = {}
authData = {}
clientID = "7e857999b41641aa922e29c9f6b68950"
clientSecret = "095d67f7477c4fa8b6466d3f9bbc3b37"

def getAccessToken(clientID, clientSecret):
   
    message = f"{clientID}:{clientSecret}" 
    message_bytes= message.encode('ascii') 
    base64_bytes = base64.b64encode(message_bytes)  
    base64_message = base64_bytes.decode('ascii')

    authHeader['Authorization'] = "Basic " + base64_message
    authData['grant_type'] = "client_credentials"

    res = requests.post(authUrl, headers = authHeader, data = authData)

    print(res)

    responseObject = res.json()

    accessToken = responseObject['access_token']

    return accessToken

token = getAccessToken(clientID, clientSecret)

"""
Spotify API 사용을 하려고 다 해봤는데
원하는 종류의 플레이리스트를 못찾았다
그래서 걍 Kaggle에서 자료를 찾아보자
"""

