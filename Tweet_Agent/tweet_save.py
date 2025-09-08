import os
import datetime
import json

def save_tweets(response):
    save_dir="generated_tweets"
    os.makedirs(save_dir,exist_ok=True)
    
    time_stamp= datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title= response["blog_title"].replace(" ","_").replace("-","")
    file_name= f"{safe_title}_{time_stamp}"
    file_path=os.path.join(save_dir,file_name)
    blog_url=str(response["url"])
    
    data= {
        "blog_title": response["blog_title"],
        "timestamp": time_stamp,
        "url":blog_url,
        "tweets": response["tweets"]
    }
    
    with open(file_path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
        
    print(f"✅ Tweets saved to: {file_path}")