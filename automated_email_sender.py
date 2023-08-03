import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Set up the SMTP server details (Gmail in this example)
    smtp_server = 'smtp.gmail.com'
    port = 587

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()

        # Login to your email account
        server.login(sender_email, sender_password)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add the message body
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", str(e))

    finally:
        # Disconnect from the SMTP server
        server.quit()

if __name__ == "__main__":
    # Enter your email credentials and recipient information here
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    receiver_email = 'recipient_email@example.com'
    subject = 'Automated Email'
    message = 'This is an automated email sent using Python.'

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, message)

"""
Before running the script, ensure you have enabled "Less Secure Apps" or generated an "App Password" for your email account if you are using Gmail.
"""