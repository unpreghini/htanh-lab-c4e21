from datetime import datetime
from gmail import GMail, Message

mail = GMail("htanh.c4e", "Hoilamgi@1")

content = '''<p>Dear boss,</p>
<p>I felt unwell this morning and it is best for me to stay at home.</p>
<p>Kindly note that I will be on leave today.</p>
<p>Best regards,</p>
<p>Tuan Anh</p>'''

msg = Message("Hoang Tuan Anh - Sick Leave Request",
              "blackmoon.lonely@yahoo.co.uk", html=content)

hour = datetime.now.hour()

while True:
    if hour == 7:
        mail.send(msg)
        break
