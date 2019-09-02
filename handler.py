import tweepy
import json
import boto3

def countDays(event, context):

    # Refer to https://apps.twitter.com/
    consumer_key = "<INSERT_CONSUMER_KEY_TWITTER>"
    consumer_secret = "<INSERT_CONSUMER_SECRET_TWITTER>"

    access_token = "<INSERT_ACCESS_TOKEN_TWITTER>"
    access_token_secret = "<INSERT_TOKEN_SECRET_TWITTER>"

    client = boto3.resource('dynamodb')
    table = client.Table('count_days')
    table.update_item(
        Key = {
            'since': '10-08-2019'
            },
        UpdateExpression = 'SET num_days = num_days +:incr',
        ExpressionAttributeValues = {
            ':incr':1
        }
    )

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    response = table.get_item(
        Key={
            "since": "10-08-2019"
        }
    )

    print(response["Item"])
    items = response["Item"]

    counter = items["num_days"]

    message = "Tag "+str(counter)
    
    api.update_status(status=message)
return 1

