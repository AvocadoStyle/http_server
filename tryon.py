my_url = 'http://127.0.0.1/../somthing/credentials.txt'
s = requests.Session()
r = requests.Request(method='GET', url=my_url)
prep = r.prepare()
prep.url = my_url # actual url you want
response = s.send(prep)