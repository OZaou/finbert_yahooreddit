# main.py

from sentiment_analyzer import FinBERTSentimentAnalyzer
from data_sources import fetch_data_sources
from visualization import plot_sentiment
from collections import defaultdict
import logging

def analyze_and_plot_sentiment(ticker):
    analyzer = FinBERTSentimentAnalyzer()


    data = fetch_data_sources(ticker)
    sentiment_counts = defaultdict(lambda: defaultdict(int))

 
    for source, texts in data.items():
        for text in texts:
            sentiment = analyzer.analyze(text)
            sentiment_counts[source][sentiment] += 1

  
    plot_sentiment(sentiment_counts, ticker) 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    tickers = ["AAPL", "TSLA", "MSFT", "AMZN"]

    for ticker in tickers:
        logging.info(f"Analyzing sentiment for {ticker}")
        analyze_and_plot_sentiment(ticker)
