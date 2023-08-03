from random import randint
from django.core.cache import cache
import requests
import json

# get the user_obj as arg, don't fetch it from the User via mobile
# as importing User in this module will triggered an circular import error
# each user's phone no. as a key so we can indentify between multiple users 
# and prevent each user to generate token before 60s
def send_otp_to_mobile(user_obj,phone):
    # if otp already exists, 
    # not exists after timeout
    if cache.get(phone):
        return False, cache.ttl(phone)        # we need redis to use ttl

    try: 
        otp_to_sent = randint(1000,9999)
        cache.set(phone,otp_to_sent,timeout=60)    # generate next otp after 60 seconds
        user_obj.otp = otp_to_sent
        send_otp(user_obj.email,otp_to_sent)
        user_obj.save()
        return True, 0
    
    except Exception as e:
        print(e)

#  send otp to mobile no. 8719805774 using sinch api
def send_otp(email,otp):
    headers = {
        'Authorization': 'Bearer 8ece5c15d3c042fb9b9b61851f33eb44',
        'Content-Type': 'application/json',
    }

    json_data = {
        'from': '447520662424',
        'to': [
            '918719805774',
        ],
        'body': f'email : {email} verify via otp {otp}',
    }

    response = requests.post(
        'https://sms.api.sinch.com/xms/v1/b8f06ee626464d7896d314f7e9b32def/batches',
        headers=headers,
        json=json_data,
)
