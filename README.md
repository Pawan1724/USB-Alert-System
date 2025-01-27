USB Monitoring Script

This script is designed to monitor the insertion and removal of USB devices on your system and notify you via email whenever a change is detected. It uses Python's psutil library to detect USB events and the smtplib library to send email notifications.

Features

Detects when a USB device is inserted or removed.

Sends email notifications for USB insertion and removal events.

Configurable email sender and receiver details.

Prerequisites

Python 3.x installed on your system.

An email account with an app-specific password for SMTP (e.g., Gmail).

Required Python libraries installed.

Installation

Clone or download this repository.

Install the required dependencies by running:

pip install -r requirements.txt

Usage

Open the script file (usb_monitor.py) and configure the following variables:

sender_email: Your email address (e.g., pawansalikanti1729@gmail.com).

receiver_email: The email address where notifications will be sent.

password: App-specific password for your email account.

Run the script:

python usb_monitor.py

The script will monitor USB device insertion and removal events and send email notifications.

How It Works

The check_for_usb() function scans the system for removable disk partitions using the psutil library.

The monitor_usb() function runs an infinite loop to monitor changes in USB state every 5 seconds.

When a USB device is inserted or removed, an email notification is sent using the send_email_smtp() function.

Sample Email Notifications

Subject: USB Device InsertedBody: A USB device has been inserted into your laptop.

Subject: USB Device RemovedBody: The USB device has been removed from your laptop.

Requirements File

The required libraries for this script are listed in the requirements.txt file:

psutil
smtplib
email

Notes

This script uses Gmail for sending emails. Ensure you have enabled "Allow less secure apps" or generated an app-specific password for your Gmail account.

To modify the monitoring interval, adjust the time.sleep(5) statement in the monitor_usb() function.

License

This project is licensed under the MIT License. Feel free to use and modify it as per your requirements.
