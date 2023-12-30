import requests
class Request:
    def MakeRequestToWsCube():
        url = "https://courses.wscubetech.com/"
        r = requests.get(url)
        return r.status_code


