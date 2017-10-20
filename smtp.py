import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "f2016244@hyderabad.bits-pilani.ac.in"
my_password = r"fd146403"
you = "ravi.bently98@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "First test"
msg['From'] = me
msg['To'] = you
print "123"
html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)
print "456"
# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
s = smtplib.SMTP_SSL('smtp.gmail.com',587)
print "789"
# uncomment if interested in the actual smtp conversation
s.set_debuglevel(1)
# do the smtp auth; sends ehlo if it hasn't been sent already
s.login(me, my_password)
print "lol"
s.sendmail(me, you, msg.as_string())
s.quit()
