from models import PROMPT
from llm import llm_initialize
import json
import re

def tweet_generator(prompt:PROMPT):
    response= llm_initialize(prompt=prompt)
    if not response or not isinstance(response, str):
        raise ValueError
    cleansed = re.sub(r"^```json|```$", "", response.strip())
    try:
        if response and isinstance(response, str):
            # Attempt to parse the response text as JSON
            cleansed_response = json.loads(cleansed)
    except json.JSONDecodeError as e:
        raise ValueError(f"❌ Failed to parse model response as JSON: {e}\nRaw response:\n{response}")
    print("✅Complted the generation of tweets.")
    return cleansed_response
    
    # return {'01': {'genre': 'Contrarian', 'tweet': "Stop confusing busy with brilliant. Greatness isn't built on endless tasks or distraction. It's built on *impact*. Focus ruthlessly on making a real difference, not just staying active. #ImpactOverActivity"}, '02': {'genre': 'Tactical', 'tweet': "Your time is finite. Ruthlessly eliminate distractions. Dedicate precious hours to the work that genuinely creates impact. This isn't just a suggestion; it's the blueprint for true greatness. #NoWastedMinutes #LaserFocus"}, '03': {'genre': 'Mindset Shift', 'tweet': "You can't control every outcome, but you absolutely control your *intention*. Anchor your daily efforts in a pure, unwavering desire to improve lives. That deep-seated purpose is your greatest power. #MindsetShift #PurposeDriven"}}   
