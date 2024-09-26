import smtplib
import getpass
import database_query_builder as h
import guipython as gui
#7071LAKSa
emails = h.list_of_emails
print(emails)

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "lakshyaagarwal04@outlook.com"
TO_EMAILS = emails
PASSWORD = getpass.getpass("Enter password: ")

SUBJECT = gui.subject
BODY = gui.body

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