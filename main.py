from turtle import Turtle, Screen
import random
my_screen = Screen()
my_screen.setup(width=500, height=400)
color = ["Red", "Orange", "Yellow", "Green", "Blue"]

speed_list = list(range(0, 11))
list_of_competitors = ["joe", "jesse", "sophie", "isaiah", "lizzy"]
game_on = False
X_COR = -230
y_cor = -150
for num in range(5):
    list_of_competitors[num] = Turtle(shape="turtle")
    list_of_competitors[num].penup()
    list_of_competitors[num].color(color[num])
    list_of_competitors[num].goto(X_COR, y_cor)
    y_cor += 75

user_choice = my_screen.textinput(title="Turtle race", prompt="choose a turtle with the colour that will win") \
    .capitalize()

if user_choice:
    game_on = True


def main():
    global game_on
    for competitor in list_of_competitors:
        if competitor.xcor() > 230:
            if user_choice.capitalize() == competitor.pencolor():
                print("You Won")
            else:
                print("You lose")
            print(f"The {competitor.pencolor()} competitor is the winner!")
            game_on = False
            return game_on
        else:
            competitor.speed(random.choice(speed_list))
            competitor.forward(competitor.speed())


while game_on:
    main()


my_screen.exitonclick()
