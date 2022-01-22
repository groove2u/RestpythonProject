import requests
import json


class restCallAPI :

    SERVER_URL = "https://huvit.hict-dev.com"
    list = list()

    def __init__(self):
        print("__init__")
    def send_api(self,url, method,headers,body) :
        try:
            if method == 'GET':
                response = requests.get(url)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
            print("response status %r" % response.status_code)
            print("response text %r" % response.text)

            ret = json.loads(response.text)
            return ret


        except Exception as ex:
            print(ex)

    def getLogin(self) :
        headers = {'Content-Type': 'application/json'}
        body = {
            "id": "test",
            "pwd": "1234"
        }

    def getCCTVInfo(self,param):

        url = self.SERVER_URL + "/public/cctvs/"+param
        headers = {'Content-Type': 'application/json'}
        body = {
            "id": "test",
            "pwd": "1234"
        }

        data = self.send_api(url, "GET", headers, body)

        return data



        #send_api("http://192.168.0.96:9099/test", "POST",headers,body)
        #print("token %r" % token)

# 호출 예시
#send_api("/test", "POST")