import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings

class SendGridEmailSend:

    def sendEmail(to_emails, subject=None, html_content=None):
        message = Mail(from_email='jahurul25@gmail.com', to_emails=to_emails, subject=subject, html_content=html_content)

        try: 
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print("Status code:", response.status_code) 
        except Exception as e:
            print(e.message)