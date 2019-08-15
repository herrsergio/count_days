import tweepy
import json

counter = 5

def countDays(event, context):

    # Refer to https://apps.twitter.com/
    consumer_key = "<INSERT_consumer_key>"
    consumer_secret = "<INSERT_consumer_secret>"

    access_token = "<INSERT_access_token>"
    access_token_secret = "<INSERT_access_token_secret>"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    message = "Tag "+counter
    counter = counter + 1

    api.update_status(status=message)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

