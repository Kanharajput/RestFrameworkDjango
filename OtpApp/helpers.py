from random import randint
from django.core.cache import cache


# get the user_obj as arg, don't fetch it from the User via mobile
# as importing User in this module will triggered an circular import error
# each user's phone no. as a key so we can indentify between multiple users 
# and prevent each user to generate token before 60s
def send_otp_to_mobile(user_obj,phone):
    # if otp already exists, 
    # not exists after timeout
    if cache.get(phone):
        return False

    try: 
        otp_to_sent = randint(1000,9999)
        cache.set(phone,otp_to_sent,timeout=60)    # generate next otp after 60 seconds
        user_obj.otp = otp_to_sent
        user_obj.save()
        return True
    
    except Exception as e:
        print(e)