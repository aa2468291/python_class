import datetime, time, subprocess

alert = datetime.datetime(2020, 6, 19, 11, 18, 30)

while datetime.datetime.now() < alert:
    time.sleep(1)
    print('Tick')

print('叮叮叮!放音樂~~')
subprocess.Popen(['start', r'C:\Users\ASUS\Desktop\test.mkv'], shell=True)
