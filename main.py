import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Turtle Race",
                            prompt="guess the winner (red, orange, yellow, green, blue, purple), Who will "
                                   "win the race ?")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []
race_is_on = True
for t1 in range(0, 6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[t1])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=positions[t1])
    all_turtle.append(new_turtle)
if user_bet:
    while race_is_on:
        for t2 in all_turtle:
            t2.forward(random.randint(0, 15))
            if t2.xcor() > 240:
                race_is_on = False
                if t2.pencolor() == user_bet:
                    print(f'hurray you won the race, the {user_bet.title()} turtle came 1st')
                else:
                    print(f'ooh!! you lost the race...,  {colors[all_turtle.index(t2)]} you won the race ')

screen.exitonclick()
