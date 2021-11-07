with open("D:/Desktop/qfl - 副本.lrc", "r", encoding="utf-8") as f:
    a = f.readlines()
    for i in range(len(a)):
        if len(a[i]) > 11:
            a[i] = a[i][11:]
print(a)
with open("D:/Desktop/qfl.lrc", "w", encoding="utf-8") as f:
    f.write("".join(a))
