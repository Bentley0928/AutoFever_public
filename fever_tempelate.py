import requests
import random
import string
# Fill in your details here to be posted to the login form.
temp2 = random.uniform(36, 37)
temp1 = round(temp2, 1)
temp = str(temp1)
payload = {
    'username': 'username',
    'password': 'password'
}

input = {
    'temperature': temp,
    'type': '2',
    'reason': ''
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://tcfsh.feverpass.life/login', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print (p.text)

    # An authorised request.
    r = s.get('https://tcfsh.feverpass.life/')
    print (r.text)

    u = s.post('https://tcfsh.feverpass.life/', data=input)
    print (u.text)
    print(temp)
