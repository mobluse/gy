m = "**v%d %s (%d min):**  "
d = ["ti", "on","fr"]
t = [85, 95, 80]
for i in range(33, 53):
    for j in range(0, 2):
        print(m % (i, d[j], t[j]))
for i in range(1, 25):
    for j in range(0, 2):
        print(m % (i, d[j], t[j]))
