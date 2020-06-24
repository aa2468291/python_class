import datetime, time

alert = datetime.datetime(2020, 6, 24, 21, 3, 30)

while datetime.datetime.now() < alert:
    time.sleep(1)
    print('Tick')

print('叮叮叮!時間到啦')
