from random import randint
from django.core.cache import cache


# get the user_obj as arg, don't fetch it from the User via mobile
# as importing User in this module will triggered an circular import error
def send_otp_to_mobile(user_obj):
    # if otp already exists, 
    # not exists after timeout
    if cache.get("phone"):
        return False

    try: 
        otp_to_sent = randint(1000,9999)
        cache.set("phone",otp_to_sent,timeout=60)    # generate next otp after 60 seconds
        user_obj.otp = otp_to_sent
        user_obj.save()
        return True
    
    except Exception as e:
        print(e)