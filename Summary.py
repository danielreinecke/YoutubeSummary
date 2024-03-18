import openai
from YoutubeTextGeneration import text as summary

openai.api_key =  Add key here and set it as openai.api_key

messages = [{"role": "system", "content":  "Helpful Teacher"}] 
message =  "Please Summarize the text\n" + summary
if message: 
    messages.append( {"role": "user", "content": message}, ) 
    chat = openai.chat.completions.create( model="gpt-3.5-turbo", messages=messages ) 
    reply = chat.choices[0].message.content 
    print(f"Summary: {reply}") 
