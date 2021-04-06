import requests, json

currency = input()
robj = requests.get(f"http://www.floatrates.com/daily/{currency}.json")

# Print your result for USD and EUR
#print(type(robj.text)) # json string

rates_dict = json.loads(robj.text)
#print(type(rates_dict))
print(rates_dict["usd"])
print(rates_dict["eur"])