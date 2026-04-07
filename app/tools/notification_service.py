import smtplib
from email.message import EmailMessage

def send_email_notification(to_email, subject, content):
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"  # NOT normal password

    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        return "Email sent successfully"
    except Exception as e:
        return str(e)
