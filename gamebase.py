import turtle as t

def square(x,y,size,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    return "DRAW A SQUARE DONE!"

if __name__ == '__main__':
    t.setup(420,420,0,0)
    t.hideturtle()
    t.tracer(0)
    print(square(50,50,10,'green'))
    t.done()
    
