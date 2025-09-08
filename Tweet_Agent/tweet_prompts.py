from models import BLOG

def summarize_blog_content(blog_content:BLOG):
    prompt= f"""
        You are given a blog article. Summarize it into a clear, high-impact outline that can be used to generate engaging tweets. Your summary must:

        -Highlight Key Insights
            Capture the strongest arguments, bold claims, unique perspectives, or surprising facts/statistics.
        -Extract Actionable Points 
            Pull out practical tips, strategies, or frameworks that could stand alone as advice.
        -Surface Contrarian or Thought-Provoking Ideas 
            Identify any statements that challenge common wisdom or spark debate.
        -Keep it Punchy and Tweetable 
            Avoid long explanations, introductions, or fluff. Summarize in short, sharp points that can be expanded into tweets.
        -  Preserve the Core Narrative 
            Ensure the summary reflects the author’s main angle or thesis so the tweets stay true to the original message.

        The output should be a structured list of concise insights and talking points, not a generic summary. Focus only on material with potential to become standalone tweets.
        
        BLOG_CONTENT
        {blog_content}
    """
    return prompt

def tweet_generation_prompt(blog_content_summarized_version:BLOG):
    prompt = f"""
            You are a social media strategist. I will provide you with a blog/article. Your task is to extract the most valuable, contrarian, or actionable insights from the content and turn each into a Twitter-ready post.

            Instructions:
            - Extract key insights from the blog.
            - Format each insight as a concise tweet (≤280 characters).
            - Use a punchy, bold, no-fluff tone designed to grab attention.
            - Each tweet should stand alone, but also flow well if used in a thread.
            - Optionally include a CTA or link if relevant (I will provide a link if needed).
            - Do not include any explanation, commentary, or formatting outside the tweets.
            - Return exactly 3 tweets, each with a distinct style or angle.
            - Respond strictly in valid JSON format using this structure:

                {{
                "01": {{
                    "genre": "Style or tone of the tweet (e.g., contrarian, inspirational, tactical)",
                    "tweet": "Tweet content here"
                }},
                "02": {{
                    "genre": "Style or tone of the tweet",
                    "tweet": "Tweet content here"
                }},
                "03": {{
                    "genre": "Style or tone of the tweet",
                    "tweet": "Tweet content here"
                }}
                }}

            Content to summarize:
            {blog_content_summarized_version.blog}
        """    
    return prompt