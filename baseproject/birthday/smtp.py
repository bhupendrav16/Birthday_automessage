import os 
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import schedule
import time 


def send_message(email,name):
    for i in range(len(email)):
        print(email,name )
        schedule.every().day.at("15:57", "Asia/Kolkata").do(message , email = email[i],name =name[i])
    while True:
        schedule.run_pending()
        time.sleep(1)
        print("message called")
        


def message(email,name):
    load_dotenv()
        
    s = "bhupendra.v.brudite@gmail.com"
    p = os.environ.get('EMAIL_PASS')
    r = email

    sub = "Special Day"

    body= f"happy birthday {name}"
    em = EmailMessage()
    em['From']= s 
    em['To'] = r
    em['Subject'] = sub 
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(s,p)
        smtp.sendmail(s,r,em.as_string())
    
    print("messaage sent")
            

    
