# TweetBot
### A bot that automatically tweets your message with a set interval.
---------
## Setup
1. Rename creds_clean.py to creds.py
2. Open creds.py in a text editor.
3. Enter your API credentials into the first 4 lines
4. Set your message and interval on the 5th and 6th lines.
5. Install [Python 3](https://www.python.org/downloads/)
6. Run main.py, if pip downloads requirements, let it finish and then run the script again.
7. Profit?
---------
## Example config
```python
consumer_key = 'blabla'
consumer_secret = 'blablabla'
access_token = 'bla-blabla'
access_token_secret = 'blablalba'
messages = ['TweetBot', 'Test', 'Fish', 'Blub']
delay = '15'
photo = {"TweetBot":"/Users/IOIIIO/Desktop/Icon.jpg", "Fish":"D:\\Images\\fish.png"}
```

**Note: Windows paths must use double backslashes to prevent formatting errors in Python**