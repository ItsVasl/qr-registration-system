pip install -r requirements.text
import qrcode
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os

# Load data here
df = pd.read_excel('sample_data.xlsx')

# Email server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv("SMTP_USER")
smtp_password = os.getenv("SMTP_PASS")

def send_email(receiver_email, subject, body, qr_code):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with open(qr_code, 'rb') as qr_img:
        msg_image = MIMEImage(qr_img.read())
        msg.attach(msg_image)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(msg)
    server.quit()

for index, row in df.iterrows():
    if row['status'] == 'done':
        qr_info = f"Student Name: {row['Student Name']}\nParent Name: {row['Parent Name']}\nMail ID: {row['Mail id']}\nNo of Weeks: {row['No of weeks']}\nstatus:{row['status']}"
        qr_img = qrcode.make(qr_info)
        qr_img_filename = f"{row['Student Name']}_QR.png"
        qr_img.save(qr_img_filename)

        send_email(row['Mail id'], 'Registration Complete', 'Thank you for registering! Please present this QR code upon arrival for smooth check-in', qr_img_filename)
    elif row['status'] == 'partially paid':
        qr_info1 = f"Student Name: {row['Student Name']}\nParent Name: {row['Parent Name']}\nMail ID: {row['Mail id']}\nNo of Weeks: {row['No of weeks']}\nstatus:{row['status']}"
        qr_img1 = qrcode.make(qr_info1)
        qr_img_filename1 = f"{row['Student Name']}_QR.png"
        qr_img1.save(qr_img_filename1)
        send_email(row['Mail id'], 'Registration Complete', 'Thank you for registering! Please present this QR code upon arrival for smooth check-in. You made a partial ammount...', qr_img_filename1)
