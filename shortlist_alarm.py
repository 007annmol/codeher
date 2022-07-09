import time,winsound,datetime

print('enter the time in hh:mm')
almtim=input()
currenttime=time.strftime("%H:%M")
print(f"the alarm time is {almtim}")
while almtim!=currenttime:
    currenttime=time.strftime("%H:%M")
    time.sleep(10)
print("current   time:",currenttime)
print("Alarm set time:",almtim)
if almtim==currenttime:
    print("playing alarm")
    winsound.PlaySound("*",winsound.SND_ASYNC)
    print("alarm sound playing")
