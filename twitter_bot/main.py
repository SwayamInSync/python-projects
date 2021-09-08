import tweepy
import time
from textblob import TextBlob

auth = tweepy.OAuthHandler('your_API', 'your_secret_api')
auth.set_access_token('access_token',
                      'secret_access_token')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

bot_id = int(api.me().id_str)

mention_id = 1
api.verify_credentials()

while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for tweet in mentions:
        print(tweet.text)
        mention_id = tweet.id
        mention_analysis = TextBlob(tweet.text)
        mention_analysis_score = mention_analysis.sentiment.polarity
        print(mention_analysis_score)
        if tweet.in_reply_to_status_id is None and tweet.author.id != bot_id:
            if mention_analysis_score >= 0 and not tweet.retweeted:
                try:
                    api.retweet(tweet.id)
                    api.create_favorite(tweet.id)
                except Exception as err:
                    print(err)
            else:
                print("Tweet will not be retweeted.\n")
    time.sleep(60*10)
