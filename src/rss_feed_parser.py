import feedparser

def fetch_yahoo_rss(ticker):
    feed_url = f"https://finance.yahoo.com/rss/headline?s={ticker}"
    feed = feedparser.parse(feed_url)
    headlines = [entry.title for entry in feed.entries]
    return headlines
