from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step 1: Add your Twilio credentials
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
client = Client(account_sid, auth_token)


# Step 2: Define a function to send WhatsApp messages
def send_whatsapp_message(to_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",  # Twilio sandbox number
            body=message_body,
            to=f"whatsapp:{to_number}",
        )
        print("Message sent successfully! SID:", message.sid)
    except Exception as e:
        print("Error:", e)


# Step 3: Collect user inputs
recipient_name = input("Enter recipient name: ")
recipient_number = input(
    "Enter recipient number with country code (e.g., +91XXXXXXXXXX): "
)
message_body = input(f"Enter the message you want to send to {recipient_name}: ")

# Step 4: Collect scheduling details
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

# Step 5: Convert inputs to datetime object
scheduled_datetime = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Step 6: Calculate delay
delay_seconds = (scheduled_datetime - current_datetime).total_seconds()

if delay_seconds <= 0:
    print("The specified time is in the past. Please enter a future date and time.")
else:
    print(f"Message scheduled to be sent to {recipient_name} at {scheduled_datetime}")
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message_body)
