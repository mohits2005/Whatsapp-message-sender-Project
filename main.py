from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv


load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_Watsapp_message(recipent_number, message_body):
    try:
        message=client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipent_number}',
        )
        print(f"Message send successfully! Message SID{message.sid}")
    except Exception as e:
        print(f"An error occured! {e}")
        
name = input("Enter the recipent name: ")
recipent_number = input("Enter the recipent number: ")
message_body= input(f"Enter the message you want to send: ")


date_str = input("Enter the date to send the message(YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24 hours format): ")

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("Specified time is in the past. Please enter a future date and time: ")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}")
    
    time.sleep(delay_seconds)
    
    send_Watsapp_message(recipent_number, message_body)