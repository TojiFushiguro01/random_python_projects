import datetime
import time
from plyer import notification

def notify_lunch():

    notification.notify(
        title="Lunch Time {}".format(time.strftime("%H:%M:%S",time.localtime())),
        message="Its Time to get something to Eat.", 
        app_name="Daily Routine Schedular", 
        app_icon="icon.png",
        timeout=10,
        toast=False
    )

while True:

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")

    if current_time == "12:00":

        notify_lunch()
        
        # Sleep for 60 seconds to avoid multiple notifications within the same minute
        time.sleep(60)
        
    # Check time every 30 seconds
    time.sleep(30)

      
