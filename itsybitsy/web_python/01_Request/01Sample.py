import requests
from requests import HTTPError, Timeout


def print_result(res):
    print(res.status_code)
    print("#"*33)
    print(res.text)


def main():
    URL = "http://httpbin.org/xml"
    json_data = {
        "key1": "value1",
        "key2": "value2"
    }
    res = requests.get(URL)
    # print(print_result(res))

    res = requests.get(URL, json_data)
    # print(res.text)

    URL = "http://httpbin.org/post"
    res = requests.post(URL, data=json_data)
    # print(print_result(res))

    URL = "http://httpbin.org/get"
    custom_header = {
        "User-agent": "Santosh Kumar / 1.0.0"
    }
    res = requests.get(URL, headers=custom_header)
    # print(print_result(res))

    # URL = "http://httpbin.org/status/404"
    URL = "http://httpbin.org/delay/5"
    try:
        res = requests.get(URL, timeout=2)
        res.raise_for_status()
        print_result(res)
    except HTTPError as err:
        print("Error {0}".format(err))
    except Timeout as err:
        print("Request timed out {0}".format(err))

    # Authentication
    URL = "http://httpbin.org/basic-auth/SanTOSH/passwd"
    

main()