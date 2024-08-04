from playsound import playsound
import time

# ANSI, manupulating terminal
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        hours_left = time_left // 3600  # seconds in an hour
        minutes_left = time_left // 60  # integer division.  Closest division to the whole number
        seconds_left = time_left % 60  # remainder after division

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")

    playsound("digital-alarm-clock-151920.mp3")


hours = int(input("How many hours to wait: "))
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_time = hours * 3600 + minutes * 60 + seconds

alarm(total_time)
