import random as rand
import turtle as trtl 
 
painter = trtl.Turtle()
scoreturtle = trtl.Turtle()
counter = trtl.Turtle()
score = 0
timer = 30
counter_interval = 1000   
timer_up = False
scoreturtle.hideturtle()
counter.hideturtle()

def countdown():
  counter.speed(0)
  counter.penup()
  counter.goto(-450, 300)
  counter.pendown()
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=("Arial",50, "normal"))
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=("Arial",50, "normal"))
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def write():
  if timer_up == False:
    scoreturtle.clear()
    scoreturtle.penup()
    scoreturtle.speed(0)
    scoreturtle.goto(200,300)
    scoreturtle.pendown()
    scoreturtle.write('Score: ' + str(score), font=("Arial",50, "normal"))
  

wn = trtl.Screen()
write()
wn.ontimer(countdown, counter_interval) 
wn.bgpic("Halloween_Background_3.png")
wn.addshape("Candy.gif")
painter.shape("Candy.gif")
wn.setup(1000,800)
def click(x,y):
  global score
  score = score + 1
  write()
  print('Clicked')
while True:
  if timer_up == False:
    painter.penup()
    painter.goto(rand.randint(-400,400),rand.randint(-400,400))
    painter.pendown()
    painter.onclick(click)
  else:
    break

wn.mainloop()
