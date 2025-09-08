import requests
import textwrap
from models import BLOG_URL,PROMPT,BLOG
from readability import Document
from llm import llm_initialize
from Tweet_Agent.tweet_prompts import summarize_blog_content

def blog_content_parser(url: BLOG_URL):
    res = requests.get(str(url))
    blog_content = Document(res.text).summary()
    blog_title = Document(res.text).title()

    if len(blog_content) <= 1500:
        summary = summarize_blog_content(blog_content=BLOG(blog=blog_content)).strip()
    else:
        chunks = textwrap.wrap(blog_content, width=1500)
        partial_summaries = []
        for c in chunks:
            response = summarize_blog_content(blog_content=BLOG(blog=c)).strip()
            partial_summaries.append(response)
        summary = "\n\n".join(partial_summaries)

    result = llm_initialize(prompt=PROMPT(prompt=summary))
    print("✅Completed the fetching of blog content.")
    return {
        "blog_title":blog_title,
        "response":result
      }
  
    # return {'blog_title': 'How to Be Great - Zen Habits Website', 'response': "Here's a high-impact outline for generating engaging tweets, structured around the blog article's core message of achieving greatness through compassionate work:\n\n---\n\n**Blog Summary Outline for Tweets:**\n\n*   **Greatness isn't busywork.** It doesn't come from distraction, but from making a real difference in the world. #ImpactOverActivity\n*   **Redefine Your Contribution:** Refocus your current work or carve out time for a dedicated project to impact others. #PurposeDriven\n*   **Be the Example:** Don't just talk about compassion. Be the living example of kindness and empathy for others. #LeadWithHeart\n*   **Intention > Results:** You can't control every outcome, but you *can* control your unwavering intention to improve lives. That's what truly matters. #MindsetShift\n*   **Show Up Daily:** Consistency is key. Bring that compassionate intention to your work every single day. #DailyCommitment\n*   **Carve Out Time Ruthlessly:** Life is limited. Put aside distractions and dedicate precious time to what truly makes a difference. #NoWastedMinutes\n*   **Single-Minded Devotion:** Focus intensely on your core mission. Prioritize ruthlessly; only what supports your impactful work matters. #LaserFocus\n*   **Health Fuels Greatness:** Good health (diet, exercise, sleep) isn't a distraction, it's foundational support for your greatest work. #SelfCareIsProductivity\n*   **Practice for Mastery:** Don't just do the work. Practice your compassionate efforts until you achieve excellence and impact. #PursuitOfGreatness\n*   **The Formula for Greatness:** Compassionate work + good-hearted intention + single-minded devotion = true greatness. #GreatnessDefined"}
