import smtplib
import getpass

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "lakshyaagarwal04@outlook.com"
TO_EMAILS = ["100lakshyaagarwal@gmail.com", "lakshya.agarwal2022@vitstudent.ac.in","aaliya.2022@vitstudent.ac.in"]  # List of recipients
PASSWORD = getpass.getpass("Enter password: ")

SUBJECT = "fewfe"
BODY = "eufheufefh"  # Message body

# Compose the email message
MESSAGE = f"Subject: {SUBJECT}\n\n{BODY}"

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

# Send email to each recipient
for TO_EMAIL in TO_EMAILS:
    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    print(f"[*] Email sent to {TO_EMAIL}")

smtp.quit()
