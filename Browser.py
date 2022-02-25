import requests
url = 'http://www.wikipedia.org'
r = requests.get(url)
print(r.text)

#Will get status code
print("Status code:")
print("\t *", r.status_code)

#Display Website header
h = requests.head(url)
print(url)
print("Website Header:")
print("**")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**")

# This will modify the headers user-agent
headers = {
    'User-Agent' : 'Mobile'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)




