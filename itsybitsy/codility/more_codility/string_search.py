import requests


def getTopicCount(topic):
    url = "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page="
    response = requests.get(url+topic)
    if response.status_code == 200:
        contents = response.text
        print(contents.count("pizza"))
        count = 0
        pos = contents.find(topic)
        while pos != -1:
            count += 1
            pos = contents.find(topic, pos+1)
        return count

print(getTopicCount("pizza"))