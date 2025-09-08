from Tweet_Agent.blog_parser import blog_content_parser
from Tweet_Agent.tweet_generator import tweet_generator
from Tweet_Agent.tweet_prompts import tweet_generation_prompt
from Tweet_Agent.tweet_save import save_tweets
from models import BLOG,PROMPT,BLOG_URL

def tweet_pipeline(url:BLOG_URL):
    response=blog_content_parser(url=BLOG_URL(url=url))
    if not response or isinstance(response,str):
        raise ValueError
    blog_title=response["blog_title"]
    summarized_content=response["response"]
    prompt= tweet_generation_prompt(blog_content_summarized_version=BLOG(blog=summarized_content))
    tweets=tweet_generator(prompt=PROMPT(prompt=prompt))
    final_result={
        "blog_title":blog_title,
        "url":url,
        "tweets":tweets
    }
    save_tweets(response=final_result)