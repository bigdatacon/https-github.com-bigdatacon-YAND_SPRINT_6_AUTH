import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail

sg = sendgrid.SendGridAPIClient(
    apikey=os.environ.get("SENDGRID_API_KEY")
)
from_email = Email("yandextest@bk.ru")
to_email = Email("yandextest@bk.ru")
subject = "Тестовое письмо Sendgrid"
content = Content(
    "text/plain", "Это тестовое письмо, отправленное через Python"
)
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())

# Отладочный вывод
print(response.status_code)
print(response.body)
print(response.headers)