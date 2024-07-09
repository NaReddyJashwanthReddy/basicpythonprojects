import pywhatkit as kit
from plyer import notification 
import time 

def send_whatsapp_msg(phone_no,message ,hour,min):
    kit.sendwhatmsg(phone_no,message,hour,min)

def create_notification(title,message):
    notification.notify(title=title,
                        message=message,
                        timeout=10
                        )

if __name__ == "__main__":
    
    phone_number = "+911234567891"  # Replace with the target phone number
    message = "Hello!"
    hour = 10  # 24-hour format
    minute = 59

    # Send the WhatsApp message
    send_whatsapp_msg(phone_number, message, hour, minute)

    
    time.sleep(30)

    
    create_notification("WhatsApp Message Sent", f"Message sent to {phone_number}: {message}")