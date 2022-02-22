import requests
url = 'http://www.wikipedia.org'
r = requests.get(url)
print(r.text)

print("Status code:")
print("\t *", r.status_code)
print("Status code:")
print("\t *", r.status_code)

headers = {
    'User-Agent' :'Iphone 8'
}
url2 = 'http://httpbin.org/headers' 
rh = requests.get(url2, headers=headers)
print(rh.text)

