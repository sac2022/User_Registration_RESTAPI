import requests
import random
import math
from .models import Verification, User
from datetime import datetime

api = "https://rest-api.d7networks.com/secure/send"
send_sms_ok = [100, 200]


def send_sms(user):
    print("send_sms called with {}".format(user), flush=True)
    otp = generate_random(6)
    print("otp generated was: {}".format(otp), flush=True)
    db_user = User.objects.only('id').get(id=user['id'])
    verification = Verification.objects.create(email=db_user.email,otp=otp,user=db_user,created_at=datetime.now())
    # full_url = api + "?p=krTQ4oVvcLi01FIaQ3jM0M93iCGrXCdPCjfHqCrXzlyxTH6zCXgfar6z1FVoJVtG&to=" + db_user.phone_number + "&text=" + otp
    # print("full_url {}".format(full_url))
    # response = requests.get(full_url)
    url = "https://http-api.d7networks.com/send"
    querystring = {
        "username": "kxgd4441",
        "password": "DkDQvliv",
        "from": "Sachin",
        "content": "your otp is " + str(otp),
        "dlr-method": "POST",
        "dlr-url": "https://4ba60af1.ngrok.io/receive",
        "dlr": "yes",
        "dlr-level": "3",
        "to": str(db_user.phone_number)
    }
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print("response: {} status_code: {}".format(response, response.status_code), flush=True)
    if response.status_code in send_sms_ok:
        print("response is okay!!", flush=True)
        verification.save()


def generate_random(length):
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(length):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])

    return random_str
