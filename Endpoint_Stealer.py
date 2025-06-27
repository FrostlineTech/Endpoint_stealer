#this is a simple script to steal an API endpoint from a website
#created by Dakota Fryberger Ceo of Frostline Solutions 
# https://frostlinesolutions.com

#Disclaimer: This script is for educational purposes only. 
# Do not use this for malicious purposes. You are responsible for your actions. 
# Use at your own risk.   


import httpx

url = "Https://TestSite.com/api/auth/login/"  #replace with the url of the website you want to steal the API endpoint from
headers = {"Origin": "https://evil-site.com"} #placeholder orgin header, just the orgin the endpoint sends data to 

with httpx.Client() as client:
    response = client.post(url, headers=headers, json={
        "username": "placeholder", #username or email for endpoint if login needed, if using an endpoint like from instagram, use proper login info and you can get the data related to the user such as session token and refresh token
        "password": "placeholder" #password for endpoint if login needed, 
    })
    print("Status Code:", response.status_code)
    print("Access-Control-Allow-Origin:", response.headers.get("access-control-allow-origin")) 
    print("Response Body:", response.text[:500])  # Show first 500 chars
