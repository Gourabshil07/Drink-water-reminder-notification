import time
# import winsound


from plyer import notification

while True:
    # winsound.Beep(1000,1000)


    notification.notify(
        title='💦Drinking Water',
        message='Sir, Please Drink Water',
        # app_name="python",
        # ticker="this is gourab",
        app_icon= None,  # e.g., 'path/to/icon.ico'
        timeout=10
    )

    time.sleep(1800)

   