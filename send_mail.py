import smtplib, ssl

port = 465 # for ssl
password = 'password'
sender_mail = 'mymail@gmail.com'
receiver_mail = 'receivermail@gmail.com'

context = ssl.create_default_context()

message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login(sender_mail, password)
        print("Logged in..")
        server.sendmail(sender_mail, receiver_mail, message)
        print("Sent message successfully")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

print("Completed...")
