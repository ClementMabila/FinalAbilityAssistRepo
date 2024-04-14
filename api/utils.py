# utils.py

import requests

def send_email(subject, message, recipient_email):
    # Mailgun API endpoint
    url = "https://api.mailgun.net/v3/sandbox1c44c8ed38dc48689ff4dfd32cb30a56.mailgun.org/messages"

    # Mailgun API key
    api_key = "4e01423e49dddd4b1a89bf73fcc36dc8-4b670513-8453db0d"

    # Sender's email address
    sender = "Clement <Clementmabila95@gmail.com>"

    # Request parameters
    params = {
        "from": sender,
        "to": recipient_email,
        "subject": subject,
        "text": message
    }

    # Send the email using requests
    response = requests.post(url, auth=("api", api_key), data=params)

    # Check if the email was sent successfully
    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email. Status code: {response.status_code}")
