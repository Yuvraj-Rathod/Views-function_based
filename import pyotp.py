# from twilio.rest import Client

# account_sid = 'YOUR_ACCOUNT_SID'
# auth_token = 'YOUR_AUTH_TOKEN'

# client = Client(account_sid, auth_token)
from twilio.rest import Client

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

client = Client(account_sid, auth_token)

def send_otp(phone_number, otp):
    message = client.messages.create(
        body=f"Your OTP is: {otp}",
        from_='YOUR_TWILIO_PHONE_NUMBER',
        to=phone_number
    )
    print("OTP sent successfully!")

# Example usage:
send_otp("+9619584226", "123456")
