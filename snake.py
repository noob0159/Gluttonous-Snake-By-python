#引用数据库
import turtle as t
from gamebase import square
from random import randrange
import time
#引用变量
snake = [
    [0,0],
    [10,0],
    [20,0],
    [30,0],
    [40,0],
    [50,0],
]
size = 10
apple_color = 'red'
snake_color = 'green'
apple_x = 10*randrange(-19,18)
apple_y = 10*randrange(-19,18)
#延迟
delay = 200
#游戏等级
level = 0
score = 0
#方向
aim_x = 0
aim_y = 10


##函数
def init():
    global snake,size,apple_color,snake_color,apple_x,apple_y,delay,level,score,aim_x,aim_y
    snake = [
    [0,0],
    [10,0],
    [20,0],
    [30,0],
    [40,0],
    [50,0],
    ]
    size = 10
    apple_color = 'red'
    snake_color = 'green'
    apple_x = 10*randrange(-18,18)
    apple_y = 10*randrange(-18,18)
    #延迟
    delay = 200
    #游戏等级
    level = 0
    score = 0
    #方向
    aim_x = 0
    aim_y = 10    
    main()

def change_direction(x,y):
    global aim_x,aim_y
    if (aim_x+x != 0) and (aim_y+y != 0):
        aim_x = x
        aim_y = y

def snake_moving(snake):    
    global apple_x,apple_y,score

    snake.append([snake[-1][0]+aim_x, snake[-1][1]+aim_y])    
    if snake[-1][0] != apple_x or snake[-1][1] != apple_y:
        snake.pop(0)
    else:
        apple_x = 10*randrange(-20,20)
        apple_y = 10*randrange(-20,20)
        score += 1

def level_up():
    global delay,score,level
    if score // 5 > level and level <= 9:
        level += 1
        delay -= 20
    
def generate_apple():
    global apple_x,apple_y,apple_color,size
    square(apple_x,apple_y,size,apple_color)

def game_running():    
    global size,snake,snake_color,delay
    if is_inside() and is_collision():        
        snake_moving(snake)
        level_up()
        t.clear()
        square(-210,-200,410,'black')
        square(-200,-190,390,'white')
        generate_apple()        
        for i in range(len(snake)):
            square(snake[i][0],snake[i][1],size,snake_color)
            
        write_text(text="score:"+str(score),font=('Times',10,'normal'),x=140,y=160)
        write_text(text="level:"+str(level),font=('Times',10,'normal'),x=140,y=170)
        write_text(text="delay:"+str(delay),font=('Times',10,'normal'),x=140,y=180)
        write_text(text="R : resume",font=('Times',10,'normal'),x=-180,y=180)
        write_text(text="W :   up  ",font=('Times',10,'normal'),x=130,y=-150)
        write_text(text="S : down  ",font=('Times',10,'normal'),x=130,y=-160)
        write_text(text="A : left  ",font=('Times',10,'normal'),x=130,y=-170)
        write_text(text="D : right ",font=('Times',10,'normal'),x=130,y=-180)
        t.ontimer(game_running, delay)
        t.update()
    else:
        write_text(text ='Game Over',font=('Times',30,'normal'),x=-100,y=0)
        return 
        
def write_text(text,font,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.write(text,font=font)

def is_inside():
    global snake
    return -190<=snake[-1][0]<=190 and -190<=snake[-1][1]<=190

def is_collision():
    global snake
    for i in range(len(snake)):
        if snake[-1][0]+aim_x == snake[i][0] and snake[-1][1]+aim_y == snake[i][1]:
            return False
    return True

##主程序
def main():
    t.setup(420,420,0)
    t.hideturtle()
    t.tracer(False)        
    t.listen()
    t.onkey(lambda: change_direction(  0, 10),'w')
    t.onkey(lambda: change_direction(-10,  0),'a')
    t.onkey(lambda: change_direction(  0,-10),'s')
    t.onkey(lambda: change_direction( 10,  0),'d')
    t.onkey(lambda: init(),'r')
    game_running()    
    t.done()
      

if __name__ == '__main__':
    main()