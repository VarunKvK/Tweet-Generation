from models import BLOG_URL
from pipeline import tweet_pipeline
"""
    Loads the blog content
    Passing it to generate tweets
    Recive 3 Tweets of different styles
    Save the output in a different file
"""

if __name__=="__main__":
    url="https://www.wikihow.com/Become-a-Millionaire"
    tweet_pipeline(url=BLOG_URL(url=url))