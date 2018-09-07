from gmail import GMail, Message

mail = GMail("htanh.c4e", "Hoilamgi@1")
msg = Message("Xin nghỉ ốm", to="qhuydtvt@gmail.com",
              text="Sáng nay dậy em phát hiện ra bị sốt")
mail.send(msg)
