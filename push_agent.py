from agents import Agent, ModelSettings, function_tool
from dotenv import load_dotenv
import requests
import os


load_dotenv(override = True)
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

@function_tool
def snd_push_ntf(write_response:str): 
    payload = {"token": pushover_token, "user": pushover_user, "message": write_response}
    response= requests.post(pushover_url,data=payload) 
    print(response.status_code)


lv_send_instructions = f"""
You are a notification manager who sends notification to the user. 
You are provided with the comprehensive report in markdown format.  
Send the output as notification using tool "snd_push_ntf
Once the notification is sent, respond with same output in the response"""

lo_sender_agent= Agent(name="Notificaton Sender", instructions=lv_send_instructions,
                            tools = [snd_push_ntf], model_settings = ModelSettings(tool_choice = "required"))