PI = 3.1415926
r = float(input("输入圆半径/cm:"))
h = float(input("输入圆柱高/cm:"))
s = PI * r * h
s_done = round(s,1)
print (f"你所求的圆柱体积为{s_done}")