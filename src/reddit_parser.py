import praw
import logging

def fetch_reddit_posts(ticker, limit=1000, subreddit='wallstreetbets'):
    try:
        reddit = praw.Reddit(
    client_id= "UoX9YHbr5O2AulsL2VXCSQ",
    client_secret= "HK4I2PXAEzqmViJVKOfkxCO-AdpEVA",
    user_agent= "testredd"
        )
        subreddit = reddit.subreddit(subreddit)
        query = f"{ticker}"
        posts = [submission.title for submission in subreddit.search(query, limit=limit)]
        return posts
    except Exception as e:
        logging.error(f"Error fetching Reddit posts: {e}")
        return []  
