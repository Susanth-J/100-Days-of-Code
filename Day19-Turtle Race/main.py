from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
bet = screen.textinput("bet", "Chose a color to win: ")

colors = ["red", "blue", "purple", "yellow", "green", "black"]
y_coordinates = [-70, -40, -10, 20, 50, 80]
turtle_list = []

for turtle_num in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_num])
    new_turtle.penup()
    new_turtle.goto(x= -210, y=y_coordinates[turtle_num])
    turtle_list.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if bet == winning_color:
                print(f"your Won! {bet} turtle has won the bet")
            else:
                print(f"You lose! {winning_color} turtle wins")

        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()
