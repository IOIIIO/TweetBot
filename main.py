try:
    from twython import Twython
except:
    import os
    os.system("pip3 install twython")
    import twython
import time
import threading
import random

from creds import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    messages,
    delay,
    photo
)

q = ""
st = time.time()
t = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

while True:
    try: 
        # perf counter start
        tic = time.perf_counter()
        # Pick random message
        k = random.choice(messages)
        # Generate random number and append
        w = random.randint(0, 12345678) # This will eventually cause us to create duplicates.
        r = " [{}]".format(w)
        n = k + r
        # Grab image if message has one and upload
        if k in photo:
            try:
                d = open(photo[k], 'rb')
                try:
                    q = t.upload_media(media=d)
                except Exception as e:
                    print("Failed to upload image. Exception: {}".format(e))
            except Exception as e: 
                print("Failed to open image. Exception: {}".format(e))
        # Send tweet
        if q == "":
            t.update_status(status=n)
            z = "with image"
        else:
            t.update_status(status=n, media_ids=[q['media_id']])
            z = ""
        # perf counter end
        toc = time.perf_counter()
        print("Tweeted: {} in {} seconds {}".format(n, toc-tic, z))
    except Exception as e:
        print(e)
    # Wait before running again
    q = ""
    time.sleep(float(delay) - ((time.time() - st) % float(delay)))