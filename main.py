import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Step 1: Define SMTP server details
SMTP_SERVER = "smtp.gmail.com"  # Gmail's SMTP server
SMTP_PORT = 587  # TLS port
EMAIL_ADDRESS = "your-email@gmail.com"  # Your email address
EMAIL_PASSWORD = "your-email-password"  # Your email password (use app password for Gmail)

# Step 2: Create the email message
def create_email(sender, recipient, subject, body):
    # Create a multipart email (can include both text and HTML)
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    # Add the email body (plain text)
    message.attach(MIMEText(body, "plain"))
    return message

# Step 3: Send the email
def send_email():
    try:
        # Establish a connection to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the server
            
            # Create email content
            recipient = "recipient-email@example.com"
            subject = "Test Email via SMTP"
            body = "Hello, this is a test email sent through Python and SMTP!"
            email_message = create_email(EMAIL_ADDRESS, recipient, subject, body)

            # Send the email
            server.sendmail(EMAIL_ADDRESS, recipient, email_message.as_string())
            print("Email sent successfully!")
            
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()
