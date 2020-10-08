#!/usr/bin/env python3

import requests
response = requests.get('https://www.google.com')

# status code
response.status_code
# raise HTTPError exception
response.raise_for_status()
# True if response is good
response.ok

# Parameters can be set a object
p = {"search": "grey kitten", "max_results": 15}

response = requests.get("https://example.com/path/to/api", params=p)

# Should have final URL'https://example.com/path/to/api?search=grey+kitten&max_results=15'
response.request.url


p = {"description": "white kitten",
     "name": "Snowball",
     "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)


# Body of HTTP message'description=white+kitten&name=Snowball&age_months=6'
response.request.body


response = requests.post("https://example.com/path/to/api", json=p)

# Body of HTTP message b'{"description": "white kitten", "name": "Snowball", "age_months": 6}'
print(response.request.body)
