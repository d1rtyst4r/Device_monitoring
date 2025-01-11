import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address_book = ['']  #enter recipuiensrecipient
sender = ''  # Enter sender

def send_mail(device):
    msg = MIMEMultipart()
    subject = device.device_type_and_location + str(device.device_id) + " is off-line"
    body = '\nDevice: ' + device.device_type_and_location + str(device.device_id) +\
              "\nDevice ip: " + device.ip + '\nPlease check!'

    msg['From'] = sender
    msg['To'] = ','.join(address_book)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    # print text
    # Send the message via  SMTP server
    s = smtplib.SMTP('')  # enter SMTP Server
    s.sendmail(sender, address_book, text)
    s.quit()
