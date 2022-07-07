import requests

print ("hello world")
print ("testing CI/CD BNI")

response =  requests.get("https://www.google.com")

print (response.text)