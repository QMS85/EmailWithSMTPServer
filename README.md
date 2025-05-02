## Sending Email With SMTP Server

This is a Python example of using the built-in ```smtplib``` library to send an email via an SMTP server.

### Explanation of the Code
#### 1. Importing Libraries:

```smtplib```: Provides the functionality to connect to an SMTP server and send emails.
```email.mime```: Used to construct email messages with different MIME types (e.g., text, HTML).

#### 2. Defining SMTP Server Details:

```SMTP_SERVER```: The domain of the SMTP server (e.g., ```smtp.gmail.com``` for Gmail).
```SMTP_PORT```: The port used for connecting securely (587 for TLS).

#### 3. Creating the Email:

```MIMEMultipart```: Allows you to add multiple parts to an email (e.g., plain text, HTML, attachments).
```MIMEText```: Specifies the body of the email (in this case, plain text).

#### 4. Establishing a Connection:

```smtplib.SMTP()```: Opens a connection to the SMTP server.
```server.starttls()```: Starts TLS encryption for secure communication.
```server.login()```: Authenticates with the SMTP server using your email and password.

#### 5. Sending the Email:

```server.sendmail()```: Sends the email from the sender to the recipient.

#### 6. Error Handling:

Uses a ```try-except``` block to catch and display any errors during the email sending process.

### Tips & Tricks
#### 1. Avoid Hardcoding Passwords:

Use environment variables or a secrets manager to store your email password securely.
For Gmail, generate an App Password to use with third-party apps.

#### 2. Use HTML Emails:

You can attach an HTML version of the email body using ```MIMEText(body, "html").```

#### 3. Test Locally:

Use tools like [MailHog](https://github.com/mailhog/MailHog) to test email functionality locally without actually sending emails.

#### 4. SMTP Libraries:

For more advanced use cases, consider libraries like ```yagmail``` or ```smtplib``` with additional features like file attachments.

#### 5. Handle Errors Gracefully:

Implement retry logic for temporary failures (e.g., network issues).

### Further Resources   
#### 1. Python Documentation:

[smtplib Library](https://docs.python.org/3/library/smtplib.html)   
[email.mime Library](https://docs.python.org/3/library/email.mime.html)

#### 2. SMTP Services:

[Gmail SMTP Configuration](https://support.google.com/a/answer/176600?hl=en)   
[SendGrid SMTP API](https://sendgrid.com/docs/API_Reference/SMTP_API/)

#### 3. GitHub Projects:

[Flask-Mail](https://github.com/mattupstate/flask-mail): A Flask extension for sending emails.   
[Postfix SMTP Server](https://github.com/vdukhovni/postfix): Open-source SMTP server.

### Project Ideas  
#### 1. Email Notification System:
Build a system that sends email notifications for events (e.g., reminders, alerts).

#### 2. Bulk Email Sender:
Create a tool to send bulk emails with personalization (e.g., newsletter).

#### 3. Contact Form with Email:
Develop a contact form for a website that sends form submissions via email.

#### 4. Email Scheduler:
Build a tool to schedule and send emails at specific times.

#### 5. Email Error Monitoring:
Develop a system that monitors email delivery and logs errors.
