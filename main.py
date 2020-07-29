try:
    from twython import Twython
except:
    import os
    os.system("pip3 install twython")
    import twython

from creds import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    message,
    delay
)

t = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

try: 
    t.update_status(status=message)
    print("Tweeted: {}".format(message))
except Exception as e:
    print(e)