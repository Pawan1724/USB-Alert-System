import smtplib
import psutil
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "youremail@gmail.com"  # Your email address
receiver_email = "receivermail@gmail.com"   # Receiver's email
password = "APP CODE BY GOOGLE"  # App-specific password

# Function to send an email using SMTP
def send_email_smtp(subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to check for USB devices
def check_for_usb():
    for part in psutil.disk_partitions():
        if 'removable' in part.opts:
            return True
    return False

# Monitor USB insertion and removal
def monitor_usb():
    usb_connected = False  # Track USB state

    print("Monitoring USB insertion and removal...")
    while True:
        usb_present = check_for_usb()

        if usb_present and not usb_connected:
            send_email_smtp("USB Device Inserted", "A USB device has been inserted into your laptop.")
            print("USB inserted!")
            usb_connected = True

        elif not usb_present and usb_connected:
            send_email_smtp("USB Device Removed", "The USB device has been removed from your laptop.")
            print("USB removed!")
            usb_connected = False

        time.sleep(5)

if __name__ == "__main__":
    monitor_usb()
