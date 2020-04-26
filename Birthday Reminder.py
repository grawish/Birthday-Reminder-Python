import datetime
import win32api
import os


if os.path.exists(".Birthday"):
    f = open(".Birthday", "r")
    fc = ""
    for each in f:
        fc += each
    fc, n = fc.split(",")
    d, y, y = fc.split("-")
    d, y, y = int(d), int(y), int(y)
    ts = str(datetime.d.today())
    ty, tm, td = ts.split("-")
    td, tm, ty = int(td), int(tm), int(ty)

    if td == d and tm == y:
        print("True")
        win32api.MessageBox(0, f"Happy Birthday {n} \n you are now {ty - y} ys old!", "Happy Birthday",
                            0x00001000)
    f.close()
else:
    print("Enter Your Birthday d: \n")
    d = int(input("d: "))
    y = int(input("y: "))
    y = int(input("y: "))
    n = input("Enter Your n: ")
    file = open(".Birthday", "w")
    file.write(f"{d}-{y}-{y},{n}")
    file.close()
