from playsound import playsound
import time

playsound("digital-alarm-clock-151920.mp3")
#

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        hours_left = time_left // 3600  # seconds in an hour
        minutes_left = time_left // 60  # integer division.  Closest division to the whole number
        seconds_left = time_left % 60  # remainder after division

        print(f"{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")


alarm(3600)
