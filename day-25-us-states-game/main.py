import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_answer_list = []

while len(correct_answer_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answer_list)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missed_state_list = []
        for state in all_states:
            if state not in correct_answer_list:
                missed_state_list.append(state)
            data_dict = {
                "states": missed_state_list
            }
            result = pandas.DataFrame(data_dict)
            result.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        correct_answer_list.append(answer_state)
        text = turtle.Turtle()  # create an instance of a turtle
        text.hideturtle()  # Hide the turtle arrow
        text.penup()  # Don't draw lines when moving
        row = data[data.state == answer_state]  # Filter the matching state row
        text.goto(row.x.item(), row.y.item())
        text.write(answer_state, align="center", font=("Arial", 12, "normal"))




