import requests

response = requests.get("https://status.aws.amazon.com/data.json")
data = dict()
if response.ok:
    data = response.json()

out_dict = dict()

for val in data.values():
    for v in val:
        if "service" in v:
            if out_dict:
                out_dict.get("service").append(v["service"])

            else:
                out_dict["service"] = []

ll = out_dict.get('service')
continents = ("us", "eu", "ap")
ret_dict = dict()
for item in ll:
    s = item.split('-')
    i = 0
    while i < len(s):
        if s[i] in continents:
            service = s[:i]
            region = s[i:]
            region = "-".join(region)
            if len(service) > 0:
                service = "-".join(service)
            if region in ret_dict:
                ret_dict.get(region).append(service)
            else:
                ret_dict[region] = []
            break
        i += 1
for k, v in ret_dict.items():
    print(k, "->", v)








