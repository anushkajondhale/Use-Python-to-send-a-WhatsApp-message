import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Credentials from .env
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = os.getenv("TWILIO_WHATSAPP_NUMBER")  # Example: whatsapp:+14155238886
TO_WHATSAPP = os.getenv("TO_WHATSAPP_NUMBER")        # Example: whatsapp:+919876543210

def send_whatsapp_message(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    msg = client.messages.create(
        body=message,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )
    print(f"✅ WhatsApp message sent! SID: {msg.sid}")

if __name__ == "__main__":
    send_whatsapp_message("Hello from Python! 🚀 #Automation #WhatsApp")
    
