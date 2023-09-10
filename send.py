# Send the Certificate to respective person through gmail
import smtplib
from email.message import EmailMessage
import imghdr
import ssl


# python3 -m smtpd -c DebuggingServer -n localhost:1025
def mail_send(name, receiver, sender, passwd):
    message = EmailMessage()
    message['Subject'] = 'Certificate of Course Completion'
    message['From'] = sender
    message['To'] = receiver
    message.set_content('CONGRATULATIONS! You have completed the course successfully')

    with open("./Output/%s.jpg" % name, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    message.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP(host='localhost', port=1025) as server:
        # server.login(sender, passwd)
        server.send_message(message)


