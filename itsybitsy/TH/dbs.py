import requests

response = requests.get("https://status.aws.amazon.com/data.json")
data = dict()
if response.ok:
    data = response.json()

out_dict = dict()

for val in data.values():
    for item in val:
        for k, v in item.items():
            print(k, "->", v)
        print()


for val in data.values():
    for v in val:
        if "service_name" in v:
            if out_dict:
                out_dict.get("service_name").append(v["service_name"])

            else:
                out_dict["service_name"] = []

print(out_dict)
