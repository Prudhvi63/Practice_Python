import json
from urllib import request
url = """http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1"""

response = request.urlopen(url)

data = json.loads(response.read().decode('utf-8'))

print(data)