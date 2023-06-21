import time
t = int(time.strftime("%H"))
if t < 12:
    print('GOOD MORNING')
elif t > 16:
    print('GOOD EVENING')
elif t > 12:
    print('GOOD AFTERNOON')
else:
    print('invalid')
