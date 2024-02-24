from flask import Flask, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form.get('input_name')
        send_email(input_data)
        return f"Kiritilgan ma'lumot e-mailga yuborildi: {input_data}"
    return render_template('web.html')

def send_email(data):
    sender_email = "qorzubek394@gmail.com"  # O'z e-mail manzilingizni yozing
    receiver_email = "qorzubek394@gmail.com"  # O'z e-mail manzilingizni yozing
    password = "Orzubek2025PC"  # O'z e-mail parolingizni yozing

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Kiritilgan ma'lumot"

    body = f"Kiritilgan ma'lumot: {data}"
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)  # SMTP server va portni o'zgartiring
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
