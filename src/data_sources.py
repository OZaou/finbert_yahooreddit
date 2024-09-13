
from rss_feed_parser import fetch_yahoo_rss
from reddit_parser import fetch_reddit_posts

def fetch_data_sources(ticker):
    rss_data = fetch_yahoo_rss(ticker)
    reddit_data = fetch_reddit_posts(ticker)
    
    return {
        'yahoo_rss': rss_data,
        'reddit': reddit_data
    }
