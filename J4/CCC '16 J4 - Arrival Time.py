hours, minutes = map(int, input().split(":"))
distance = 120
time = hours * 60 + minutes
counter = 0
while distance > 0:
    if (420 <= time < 600) or (900 <= time < 1140):
        distance -= 0.5
    else:
        distance -= 1
    time += 1
    counter += 1
hours += int(counter/60)
minutes += counter % 60
if hours >= 24:
    hours -= 24
if minutes >= 60:
    minutes -= 60
    hours += 1
print("{:02d}:{:02d}".format(hours, minutes))
