import requests
import json
API_key="907c3c87c332d3c6181267fa616f3a00"
city_ID=input("enter your city")
country_code="GE"
start=input(" enter starting time")
end=input("enter ending time")
url = f'http://history.openweathermap.org/data/2.5/history/city?q={city_ID},{country_code}&type=hour&start={start}&end={end}&appid={API_key}'
r = requests.get(url)
print(r)
print(r.status_code)
print(r.headers)
print(r.headers['Content-Type'])
print(r.text)
result_json = r.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
print(res_structured)

b=res['main']
pressure=b["pressure"]
print("pressure:" + pressure)


