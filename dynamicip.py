import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import schedule
import time

# Configuration
IP_FILE = 'ip_address.txt'  # File where the IP will be stored
EMAIL_FROM = 'your_email@example.com'  # Sender's email
EMAIL_TO = 'recipient@example.com'  # Recipient's email
SMTP_SERVER = 'smtp.example.com'  # SMTP server
SMTP_PORT = 587  # SMTP port (usually 587 for TLS)
EMAIL_USER = 'your_email@example.com'  # SMTP login
EMAIL_PASS = 'your_email_password'  # SMTP password

# Function to get the current public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

# Function to get the stored IP address from a file
def get_stored_ip():
    if os.path.exists(IP_FILE):
        with open(IP_FILE, 'r') as file:
            return file.read().strip()
    return None

# Function to update the IP address in the file
def update_ip_in_file(ip):
    with open(IP_FILE, 'w') as file:
        file.write(ip)

# Function to send email notification when the IP changes
def send_email_notification(new_ip):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = "Home | Public IP Address Changed"
        body = f"Your new public IP address is: {new_ip}"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_USER, EMAIL_PASS)
        text = msg.as_string()
        server.sendmail(EMAIL_FROM, EMAIL_TO, text)
        server.quit()

        print(f"Email sent successfully to {EMAIL_TO}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function that checks the IP, updates it if necessary, and sends an email
def check_ip_change():
    print("Checking for IP changes...")
    
    # Step 1: Get the current public IP
    current_ip = get_public_ip()
    if not current_ip:
        print("Could not retrieve current IP.")
        return

    print(f"Current IP: {current_ip}")

    # Step 2: Get the stored IP from the file
    stored_ip = get_stored_ip()
    print(f"Stored IP: {stored_ip}")

    # Step 3: Compare the IPs
    if stored_ip != current_ip:
        print(f"IP has changed from {stored_ip} to {current_ip}")
        
        # Step 4: Update the IP in the file
        update_ip_in_file(current_ip)
        print("IP updated in the file.")

        # Step 5: Send email notification
        send_email_notification(current_ip)
    else:
        print("IP has not changed.")

# Scheduling the IP check daily
def schedule_daily_ip_check_old():
    # schedule.every().day.at("09:00").do(check_ip_change)  # Set to run daily at 9 AM

    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait a minute before checking again

def schedule_daily_ip_check():
    schedule.every(10).seconds.do(check_ip_change)  # Set to run every 10 seconds

    while True:
        schedule.run_pending()  # Check if a scheduled task is due
        time.sleep(1)  # Wait 1 second before checking again (for responsiveness)

# Run the scheduled task
if __name__ == '__main__':
    check_ip_change()  # Initial check
    schedule_daily_ip_check()  # Schedule it to run daily
