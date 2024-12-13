import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
  "question": "How can I request a refill for my prescription at Lamna Healthcare?",
  "chat_history": []
}


body = str.encode(json.dumps(data))

url = 'https://rag-4997-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMy8iLCJpYXQiOjE3MzQwNTI0OTIsIm5iZiI6MTczNDA1MjQ5MiwiZXhwIjoxNzM0MDU3MDk0LCJhY3IiOiIxIiwiYWlvIjoiQWFRQVcvOFlBQUFBYnBxdE9uaTNjRVlJRDRNOVVYanltb1JjOFNWYlROalJaU0VRd0RsQ3Vrajd1M3hqaUFzYTlRVDRGOUw5RGo0VHJKOWFzT3p5Yjh0WTRJRElnRHJnOS9WMkJqd2NoRno3YXl1aS9pS3JpZDZsaWNjLzJJQWVyUmtTMC9iZVVOZFRXUWRnR3Izc0t6ZTJOaVhJRk03QnluMWhYNXYydkliUmxYazJYMHJKUXdCWnRHdHE1eU5vR3A1TFdhc2thTE14ejNSMVVJVllYc05kc0pGcnFGbEtsdz09IiwiYWx0c2VjaWQiOiI1OjoxMDAzMjAwMTRBM0IyNTQxIiwiYW1yIjpbInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiZjhjOTBhZWMtODRmZS00YjZmLWFjYzktYzYyZjM5YjA5ZjM3IiwiZW1haWwiOiJsaW5lc2hnYWplcmFAbWljcm9zb2Z0LmNvbSIsImZhbWlseV9uYW1lIjoiR2FqZXJhIiwiZ2l2ZW5fbmFtZSI6IkxpbmVzaCIsImdyb3VwcyI6WyJiMTMwNDAyMi0wOGU2LTQ0N2QtYjA5NC0xNTM3MDU5N2M2YjYiLCIwMTJjZTc1Yy03ZDg3LTQxY2ItOWM0OC0wMjQ3NmQwYmY4NGYiLCIwOTUzMWE3Mi0yYzNlLTRlMDYtYmUxZS0yNTk2YmQwOGRjZGQiLCI3YmVkNGI4NC1lYmE5LTQ1YTQtYTdiZC05MGM2ODQxNTU1NGIiLCJkMzRjNGViZS00OTg0LTQ5MDMtYTY0ZC04YzIwMjgzZDUxNmIiLCJlMzA5NmRmNy1iNjVjLTRlMzItYWIxYS03YTM1ZGM2ODRmMGEiXSwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjQ3LyIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjY5LjIzMi4yNDkuMjkiLCJuYW1lIjoiTGluZXNoIEdhamVyYSIsIm9pZCI6Ijg2NjFkMmM4LTJmOTktNDFjOS05NzlmLTVmMjQ0YjU3MGU0ZSIsInB1aWQiOiIxMDAzMjAwMkQxQjAyMTM4IiwicmgiOiIxLkFVWUFFOEN6RmdEVGpVYXNaSDdhQ0NDMjAxOXZwaGpmMnhkTW5kY1dOSEVxbkw3eEFLbEdBQS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJOQkZUMkpuRjF6OWxJWUdkbXlxSXlxZkhxSlpPQTFjSFRJYjJjTmRaNHBjIiwidGlkIjoiMTZiM2MwMTMtZDMwMC00NjhkLWFjNjQtN2VkYTA4MjBiNmQzIiwidW5pcXVlX25hbWUiOiJsaW5lc2hnYWplcmFAbWljcm9zb2Z0LmNvbSIsInV0aSI6IjJSY21Yckt1OGtTQnkyWng4UjllQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfaWRyZWwiOiIyIDEifQ.GCBcs8_iOBrqeHiNAnHZTdAtRd4SQzFu2Iz6Kp97wTYMw2CwkLo54BTXP7LKWRfnjktQwnDUGI1DpdykkneHWeBCxi-A0bs-PX0b-kjM6fYX_BsvyuWFmD9_7ZV0t1ANSPpkPJ0sRkGvH8nH6nkcNdwzuoNo9XBmDrah4ijDfrddaEqVGrN7asNWc-AE76gv7XLneYJVtD6s5U3Veb4kPfbMQlSbKG_l3PI-MiefLNHm6VwiojItACS6UUJrYrN6qADiLXosCCxjEkj-Z6W96uOcZ7ClTuJ64qDPNkQkHxQxpyYW5CytRc3ruWmeanJvCODfNW9-bYeIpmP_fdm9Cw'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))