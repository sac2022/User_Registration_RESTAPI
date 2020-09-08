import requests
import random
import math
from .models import Verification, User
from datetime import datetime

api = "https://gateway.sms77.io/api/sms"
send_sms_ok = [100, 200]

def send_sms(user):
    print("send_sms called with {}".format(user), flush=True)
    otp = generate_random(6)
    print("otp generated was: {}".format(otp), flush=True)
    db_user = User.objects.only('id').get(id=user['id'])
    verification = Verification(user['email'], otp, db_user, datetime.now())
    full_url = api + "?p=krTQ4oVvcLi01FIaQ3jM0M93iCGrXCdPCjfHqCrXzlyxTH6zCXgfar6z1FVoJVtG&to=" + db_user.phone_number + "&text=" + otp
    print("full_url {}".format(full_url))
    response = requests.get(full_url)
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