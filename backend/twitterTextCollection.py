# import tweepy
import tweepy as tw

# your Twitter API key and API secret
my_api_key = "7xrCXohb8vEVJhiP5psmGJz7a"
my_api_secret = "XPiZrZvMxOMsK11c99RmxqNUBt55IPuyjylhxVO55QQnhLtDys"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# search for keywords
search_query = "#hurricane -filter:retweets"

# get tweets from the API
starttime = "2022-09-22"
# needs to upgrade  
label = "https://api.twitter.com/1.1/tweets/search/30day/dev.json"
tweets = tw.Cursor(api.search_30_day(label, auth),
              q=search_query,
              lang="en",
              since=starttime).items(100)


# store the API responses in a list
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)
    
#print("Total Tweets fetched:", len(tweets_copy))
#NOT REALLY NEED TO PRINT OUT BUT USEFUL TO GET
import pandas as pd

# intialize the dataframe
tweets_df = pd.DataFrame()

# populate the dataframe
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        pass
    tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name, 
                                               'user_location': tweet.user.location,\
                                               'user_verified': tweet.user.verified,
                                               'date': tweet.created_at,
                                               'text': text, 
                                               'hashtags': [hashtags if hashtags else None],
                                               'source': tweet.source}))
    tweets_df = tweets_df.reset_index(drop=True)

# show the dataframe
tweets_df.head()