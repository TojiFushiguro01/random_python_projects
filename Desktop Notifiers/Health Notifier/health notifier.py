import time
from plyer import notification

def break_time():
    notification.notify(
        title="Break Time!",
        message="Drink Some Water.",
        app_name="Health Wiser",
        app_icon="glass of water.png",
        timeout=10,
        toast=False
    )

while True:
    break_time()
    time.sleep(3600.0) # Notify after every 1 hour