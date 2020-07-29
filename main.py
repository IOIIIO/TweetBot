try:
    from twython import Twython
except:
    import os
    os.system("pip3 install twython")
    import twython
import time
import threading

from creds import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    message,
    delay
)

st = time.time()
t = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

while True:
    try: 
        tic = time.perf_counter()
        t.update_status(status=message)
        toc = time.perf_counter()
        print("Tweeted: {} in {} seconds".format(message, toc-tic))
    except Exception as e:
        print(e)
    time.sleep(float(delay) - ((time.time() - st) % float(delay)))