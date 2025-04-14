from celery import Celery

def make_celery(app):
    celery = Celery(
        "Application Jobs",
        broker="redis://localhost:6369/0",
        backend="redis://localhost:6369/0",
        include=["app.tasks.daily", "app.tasks.monthly"],
    )

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():  # Ensure Flask context is available
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    celery.conf.timezone = "Asia/Kolkata"
    
    return celery

# Import and initialize the app properly
from run import app  # Ensure `app` is defined in `run.py`
celery = make_celery(app)  # Pass `app` explicitly



# celery = make_celery(current_app)  # Initialize Celery with Flask app

# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     from app.tasks.daily import daily_reminder_professionals
#     from app.tasks.monthly import monthly_report_customer

#     sender.add_periodic_task(500, daily_reminder_professionals.s(), name="daily_task")
#     sender.add_periodic_task(20, monthly_report_customer.s(), name="monthly_task")

from celery.schedules import crontab

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from app.tasks.daily import daily_reminder_professionals
    from app.tasks.monthly import monthly_report_customer

    # Run daily_reminder_professionals every day at 5 PM
    sender.add_periodic_task(
        crontab(hour=8, minute=33),
        daily_reminder_professionals.s(),
        name="daily_task",
    )

    # Run monthly_report_customer on the first day of every month at 12:00 AM
    sender.add_periodic_task(
        # crontab(hour=8, minute=33),
        crontab(day_of_month=1, hour=0, minute=0),
        monthly_report_customer.s(),
        name="monthly_task",
        )
