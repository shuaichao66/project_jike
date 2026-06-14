"""
科赫雪花
"""
import math
import turtle
def draw_triangle(x1,y1,x2,y2,x3,y3,t):
    t.up()
    t.setpos(x1,y1)
    t.down()
    t.setpos(x2,y2)
    t.setpos(x3,y3)
    t.setpos(x1,y1)
    t.up()
def drawKouchSF(x1,y1,x2,y2,t):
    """绘制科赫雪花"""
    c=((x1+x2)/2,(y1+y2)/2)
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    r=d/3
    h=r*math.sqrt(3)/2
    n=((y1-y2)/d,(x2-x1)/d)
    p1=((2*x1+x2)/3,(2*y1+y2)/3)
    p2=(c[0]-h*n[0],c[1]-h*n[1])
    p3=((x1+2*x2)/3,(y1+2*y2)/3)
    if d>40:
        drawKouchSF(x1,y1,p1[0],p1[1],t)
        drawKouchSF(p1[0], p1[1],p2[0],p2[1],t)
        drawKouchSF(p2[0],p2[1],p3[0],p3[1],t)
        drawKouchSF(p3[0],p3[1],x2,y2,t)
    else:
        t.up()
        # t.setpos(x1,y1)
        # t.down()
        # t.setpos(x2, y2)
        t.setpos(p1[0],p1[1])
        t.down()
        t.setpos(p2[0],p2[1])
        t.setpos(p3[0],p3[1])
        t.up()
        t.setpos(x1,y1)
        t.down()
        t.setpos(p1[0],p1[1])
        t.up()
        t.setpos(p3[0],p3[1])
        t.down()
        t.setpos(x2,y2)
def main():
    t = turtle.Turtle()
    t.hideturtle()
    # draw_triangle(-100,0,0,-173.2,100,0,t)
    try:
        x1, y1 = -100, -57.7  # 左下
        x2, y2 = 100, -57.7  # 右下
        x3, y3 = 0, 115.4  # 顶点

        drawKouchSF(x1, y1, x2, y2, t)  # 底边
        drawKouchSF(x2, y2, x3, y3, t)  # 右边
        drawKouchSF(x3, y3, x1, y1, t)  # 左边
        turtle.mainloop()
    except:
        print("exception,exiting")
        exit(0)


if __name__ == '__main__':
    main()