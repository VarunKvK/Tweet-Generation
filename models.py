import pydantic


"""
    The models created are for the twitter_agent
"""
class BLOG_URL(pydantic.HttpUrl):
    url:str=""
    
class BLOG(pydantic.BaseModel):
    blog:str=""
    
class PROMPT(pydantic.BaseModel):
    prompt:str=""
    
class TWEET(pydantic.BaseModel):
    blog:str=""
    url:BLOG_URL
    tweet:str=""
