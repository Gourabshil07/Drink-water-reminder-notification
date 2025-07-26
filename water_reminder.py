import time
# import winsound


from plyer import notification

while True:
    # winsound.Beep(1000,1000)


    notification.notify(
        title='💦Drinking Water',
        message='Sir, Please Drink Water',
        timeout=10
    )

    time.sleep(1800)

   
