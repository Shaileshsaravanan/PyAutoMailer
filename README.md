# Automated Email Sender

This is a simple Python script that allows you to send automated emails using the `smtplib` library. You can use this script to send emails to one or multiple recipients with a specified subject and message.

## Prerequisites

Before using the script, make sure you have the following:

1. Python installed on your system.
2. A valid email account with the necessary credentials (email address, password, SMTP server, and port). If you are using Gmail, make sure to enable "Less Secure Apps" or generate an "App Password."

## Getting Started

1. Clone or download this repository to your local machine.

2. Install the required libraries using pip:

```bash
pip install smtplib
```

3. Open the `automated_email_sender.py` file and update the following variables:

   - `sender_email`: Your email address (e.g., 'your_email@gmail.com').
   - `sender_password`: Your email account password or generated "App Password" if using Gmail.
   - `receiver_email`: The recipient's email address (e.g., 'recipient_email@example.com').
   - `subject`: The subject of the email.
   - `message`: The content of the email.

4. Save the changes to the script.

## How to Use

To use the script, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the `automated_email_sender.py` file is located.

3. Run the script:

```bash
python automated_email_sender.py
```

The script will connect to the SMTP server and send the email using the provided credentials. If everything is set up correctly, you should see the message "Email sent successfully!" in the terminal.

## Customize the Script

Feel free to customize the script to suit your needs. You can add more features, such as attachments, HTML content, or error handling to make it more robust and user-friendly.

## Disclaimer

This script is provided as-is without any warranty. Use it responsibly and at your own risk. The script is intended for educational and personal use only. Make sure you have permission from the recipient before sending automated emails.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
