rgb = [float(i) for i in input().split()]
r = rgb[0] // 6.375
gb = (rgb[1] + rgb[2])//100
out = abs(r - gb)
print(int(out))