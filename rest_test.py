# 400에러가 나는 경우, 보내는 data가 int면 int에 맞게 보내야 한다. string으로 보내면 안된다.
# 401에러가 나는경우는 connection을 유지하지 못해서난다.

import requests
import json
import sys

url = 'http://210.97.42.250:8005/v1.0/attrs'
headers = {'content-type': 'application/json', 'Connection': 'keep-alive'}
session = requests.session()
user_input=0
#해당 세션을 기반으로 요청
class Colors:
    BLACK = '\033[30m'
    Red = '\033[31m'
    Green = '\033[32m'
    Yellow = '\033[33m'
    BLUE = '\033[34m'
    Magenta = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    
def send_auth_info():
    payload = {
    "severity":"0",
    "tpId":"PnC_SMARTWATERCARE.PNC0000",
    "msgType":"Q", 
    "data":"{\"authCode\":\"a142a0493e081636\"}",
    "dataFormat":"application/json", 
    "authToken":"",
    "msgId":"2d90a0b4-0ccd-4104-82dc-4e65d5783404",
    "resMsg":"",
    "version":"1.0",
    "tId":"",
    "sId":"C000000003", 
    "encType":"0",
    "resCode":"",
    "msgCode":"MSGAUTH00002" ,
    "funcType":"002"
    }
    r = session.post(url, data=json.dumps(payload), headers=headers)
    print(Colors.Yellow + "***********(인증키)************" + Colors.RESET)
    # print(r.text)
    rjson = r.json()
    # print("인증키는:")
    auth_key=rjson["data"]["authToken"]
    print(auth_key)
    print(Colors.Yellow + "*****************************" + Colors.RESET)
    return auth_key

def send_thing_data(auth_key):
    data_payload= {
        "severity": "0",
        "tpId": "PnC_SMARTWATERCARE.PNC0000",
        "msgType": "Q",
        "data":"{\"dong_number\": 0 }",
        "dataFormat": "application/json",
        "authToken": str(auth_key),
        "msgId": "b3672817-0333-4fe0-822c-43b0305f47f3",
        "resMsg": "",
        "version": "1.0",
        "tId": "PnC_SMARTWATERCARE.PNC0000",
        "sId": "C000000003",
        "encType": "0",
        "resCode": "200",
        "msgCode": "Basic-AttrGroup",
        "funcType": "021",
        "msgDate": 1614678440159
    }
    
    r2 = session.post(url,data=json.dumps(data_payload),headers=headers)
    print(Colors.Yellow + "***********[return값]******************" + Colors.RESET)
    print(r2.text)
    print(Colors.Yellow + "*****************************" + Colors.RESET)
    # rjson = r2.json()
    # print(rjson)


while user_input != 5:
  print("\n")
  print(Colors.Green + '***************[Rest Client Menu]******************** \n' + Colors.RESET)
  print(Colors.Yellow + "1. just check Authentication(인증키받기)" + Colors.RESET)
  print(Colors.Yellow + "2. sending thing data one time after Authentication(1번 보내기)"+ Colors.RESET)
  print(Colors.Yellow + "3. sending thing data 50times after Authentication(50번 random값 보내기)"+ Colors.RESET)
  print(Colors.Yellow + "4. sending db data continuously after Authentication(db데이터 보내기)"+ Colors.RESET)

  print("\n")
  print(Colors.Red + "5. Quit\n\n"+ Colors.RESET)

  print(Colors.Magenta +"Enter your Selection: " + Colors.RESET)
  user_input = input()

  if user_input == '1':
      auth_key=send_auth_info()
  elif user_input == '2':
      auth_key=send_auth_info()
      send_thing_data(auth_key)
  elif user_input =='3':
      auth_key=send_auth_info()
      num=1
      while num <=50:
          send_thing_data(auth_key)
          num = num+1
  elif user_input == '5':
      print(Colors.Red + "quitting(메뉴끝)\n\n"+ Colors.RESET)
      exit()
  else:
      print("idiot!...select between 1 to 3")
