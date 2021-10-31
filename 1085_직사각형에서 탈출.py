x, y, w, h = map(int, input().split())

if w - x <= w / 2:
    a = w - x
else:
    a = x
if h - y <= h / 2:
    b = h - y
else:
    b = y

print(min(a, b))
