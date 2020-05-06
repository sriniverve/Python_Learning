import requests

r = requests.get('https://www.youtube.com')


print(dir(r))
print(r)
print(r.headers)
print(r.status_code)
print(r.json)