from playsound3 import playsound
import time 



clear="\33[2J"
printonsame="\33[H"

def alarm(seconds):
    time_elasped=0
    print(clear)
    while time_elasped<seconds:
        time.sleep(1)
        time_elasped+=1
        t=seconds-time_elasped
        minutes=t//60
        second=t%60

        print(F"{printonsame}The alarm will ring in {minutes:02d} : {second:02d}")
    playsound("alarm.mp3")

usermin=int(input("Enter the alarm minutes: "))
usersec=int(input("Enter the alarm seconds: "))
total_time=usermin*60+usersec

alarm(total_time)