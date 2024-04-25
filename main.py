import turtle
import pandas

# create the screen and import our .gif
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# call in our data and a black list to be appended with guesses
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# main game loop. checks guesses are in the data and creates a text turtle at
# the specified x, y coords
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", 
                                    prompt="What's another state's name?").title()
# states not guessed are added to learn.csv
    if answer_state == "Exit":
        not_guessed_states = []
        for state in  all_states:
            if state not in guessed_states:
                not_guessed_states.append(state)
        new_data = pandas.DataFrame(not_guessed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        t.goto(x, y)
        t.write(answer_state)
