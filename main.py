import smtplib
import schedule
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT")

def read_tasks():
    if not os.path.exists("tasks.txt"):
        return "No tasks for today!"
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()    
    if not tasks:
        return "No tasks for today!" 
    formatted = "Today's Tasks:\n\n"
    for i, task in enumerate(tasks, start=1):
        formatted += f"{i}. {task.strip()}\n"  
    return formatted

def send_email():
    tasks = read_tasks()
    
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT
    msg['Subject'] = "Your Daily Tasks"
    msg.attach(MIMEText(tasks, 'plain'))
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        
def main():
    print("Daily Task Emailer running...")
    schedule.every().day.at("08:00").do(send_email)
    while True:
        schedule.run_pending()
        time.sleep(60)   
if __name__ == "__main__":
    main()