def euklides(a, b):
    xs = [1,0]
    ys = [0,1]
    sign = 1
    while b != 0:
        r = a%b
        q = a//b
        a=b
        b=r
        xx=xs[1]
        yy=ys[1]
        xs[1]=q*xs[1] + xs[0]
        ys[1]=q*ys[1]+ys[0]
        xs[0]=xx
        ys[0]=yy
        sign = -sign
    x=sign*xs[0]
    y=-sign*ys[0]
    return [a,x,y]

print(euklides(123,202))
