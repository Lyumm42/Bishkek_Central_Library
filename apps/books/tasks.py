from celery import shared_task

@shared_task
def send_reminder_email(user_id):
    print(f"Письмо пользователю {user_id} отправлено.")
