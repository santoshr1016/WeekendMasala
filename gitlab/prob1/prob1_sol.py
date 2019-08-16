from collections import Counter


filename = "access.log"


def valid_ip(ip):
    if not len(ip):
        return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for item in parts:
        if not item.isdigit():
            return False
        num = int(item)
        if num < 0 or num > 255:
            return False
    return True

ips = list()
with open(filename) as fd:
    for line in fd:
        ip = line.strip().split(" ")[0]

        if valid_ip(ip):
            ips.append(ip)


ip_count = Counter(ips)
top_ten = ip_count.most_common(10)
for item in top_ten:
    print(item)



