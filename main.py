import time
from plyer import  notification

while True:
    notification.notify(
    title = "**Please Drink Water Now 🧞‍♂️",
    message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
    app_icon = "F:\Python\Practice\P2\Drinking Water Notification System\icon.ico",
    timeout = 12
        )
    time.sleep(60 * 60)
